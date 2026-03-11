#!/usr/bin/python
#-*- coding: utf-8 -*-
##############################################################################
#
# CALENTON
# Programa de procesamiento y generación de informes para datos de emisión
# de contaminantes
#
# (C) LITEC, 2009-2010
# (C) Trustserver SL, 2009-2010
# Todos los derechos reservados
#
# $Id: maparesultadosdlg.py 360 2010-11-18 22:17:21Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/maparesultadosdlg.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtSql import *
from .ui.Ui_maparesultadosdlg import *
from .listaresultadodlg import *
from ts import ComboDataModel
from qgis.core import QgsApplication, QgsProject, QgsVectorLayer, QgsDataSourceUri, QgsStyle, QgsSymbol, QgsGraduatedSymbolRenderer, QgsRectangle, QgsSymbolLayerUtils

class MapaResultadosDlg (QDialog, Ui_MapaResultadosDlgClass):
	def __init__(self, parent = None):
		QDialog.__init__(self, parent)
		self.setupUi(self)

		self.sql = None

		self.app = QApplication.instance()
		if not self.app.databaseInit:
			return
		self.db = self.app.workDb()

		self.pueblaRampas()

		self.gc = QButtonGroup(self)
		self.gc.addButton(self.agregaContaminante)
		self.gc.addButton(self.soloContaminante)
		self.gf = QButtonGroup(self)
		self.gf.addButton(self.agregaFuente)
		self.gf.addButton(self.soloFuente)
		self.gcl = QButtonGroup(self)
		self.gcl.addButton(self.agregaClasificacion)
		self.gcl.addButton(self.soloClasificacion)

		self.agregaContaminante.setChecked(True)
		self.agregaFuente.setChecked(True)
		self.agregaClasificacion.setChecked(True)

		self.mNivelZona = ComboDataModel(self)
		self.mNivelZona.setQuery("select id, nombre from nivelzona order by id",  self.db)
		self.nivelZona.setModel(self.mNivelZona)

		self.mContaminante = ComboDataModel(self)
		self.mContaminante.setQuery("select id, nombre from contaminante order by nombre", self.db)
		self.contaminante.setModel(self.mContaminante)

		self.mEscenario = ComboDataModel(self)
		self.mEscenario.setQuery("select id, nombre from escenario order by nombre",  self.db)
		self.escenario.setModel(self.mEscenario)

		self.mFuente = ComboDataModel(self)
		self.on_escenario_activated(0)
		self.fuente.setModel(self.mFuente)

		self.llena_nivelClasificacion()

		self.mClasificacion = ComboDataModel(self)
		self.on_nivelClasificacion_activated(0)
		self.clasificacion.setModel(self.mClasificacion)

		self.on_nivelZona_activated(0)

	def pueblaRampas(self):
		self.style = QgsStyle.defaultStyle()
		size = QSize(50, 16)
		self.comboColor.setIconSize(size)
		lr = self.style.colorRampNames()
		for i in lr:
			ramp = self.style.colorRamp(i)
			icon = QgsSymbolLayerUtils.colorRampPreviewIcon(ramp, size)
			self.comboColor.addItem(icon, i)
			ramp = None

	def llena_nivelClasificacion(self):
		self.nivelClasificacion.addItem("SNAP XX",  "SNAP1")
		self.nivelClasificacion.addItem("SNAP XX XX",  "SNAP2")
		self.nivelClasificacion.addItem("SNAP XX XX XX",  "SNAP3")
		self.nivelClasificacion.addItem("IPCC X",  "IPCC1")
		self.nivelClasificacion.addItem("IPCC XX",  "IPCC2")
		self.nivelClasificacion.addItem("IPCC XXX",  "IPCC3")

	@pyqtSlot(int)
	def on_escenario_activated(self,  index):
		self.idEscenario = int(self.escenario.currentItemData() or 0)
		self.mFuente.setQuery("select id, nombre from fuente where idescenario = %d order by nombre"
		                	% (self.idEscenario), self.db)

	@pyqtSlot(int)
	def on_nivelZona_activated(self, index):
		self.idNivelZona = int(self.nivelZona.currentItemData() or 0)

	def condicionClasificacionParcial(self):
		clas = str(self.nivelClasificacion.currentItemData() or "")
		if clas[0:4] == "SNAP":
			cond = "cl.idtipoclas = 3"
			if clas == "SNAP1":
				cond = cond + " and length(cl.codigo) = 2"
			elif clas == "SNAP2":
				cond = cond + " and length(cl.codigo) = 5"
			elif clas == "SNAP3":
				cond = cond + " and length(cl.codigo) = 8"
		elif clas[0:4] == "IPCC":
			cond = "cl.idtipoclas = 4"
			if clas == "IPCC1":
				cond = cond + " and length(cl.codigo) = 1"
			elif clas == "IPCC2":
				cond = cond + " and length(cl.codigo) = 2"
			elif clas == "IPCC3":
				cond = cond + " and length(cl.codigo) = 3"
		return cond

	@pyqtSlot(int)
	def on_nivelClasificacion_activated(self,  index):
		cond = self.condicionClasificacionParcial()
		sql = """select cl.id, cl.codigo || '-' || cl.descripcion
			from clasificacion cl
			where %s
			order by 2
			""" % (cond)
		self.mClasificacion.setQuery(sql,  self.db)

	def hazContaminante(self):
		if self.soloContaminante.isChecked():
			idContaminante = int(self.contaminante.currentItemData() or 0)
			cols = []
			cn = []
			tablas = []
			where = [ 'cz.idcontaminante = %d' % (idContaminante) ]
		elif self.agregaContaminante.isChecked():
			cols = [ 'sum(cz.valor * ec.p)' ]
			cn = [ '"Ton. equiv. CO2"' ]
			tablas = [ 'equivcontaminante ec' ]
			where = [ 'ec.idescenario = f.idescenario',  'ec.idcontaminante = cz.idcontaminante' ]
		return (cols,  cn,  tablas,  where)

	def hazFuente(self):
		if self.soloFuente.isChecked():
			idFuente = int(self.fuente.currentItemData() or 0)
			cols = []
			cn = []
			tablas = [ 'fuente f' ]
			where = [ 'f.id = %d' % (idFuente), 'cz.idfuente = f.id' ]
		elif self.agregaFuente.isChecked():
			cols = []
			cn = []
			tablas = [ 'fuente f' ]
			where = [ 'f.id = cz.idfuente', 'f.idescenario = %d' % (self.idEscenario) ]
		return (cols,  cn,  tablas,  where)

	def hazZona(self):
		self.idNivelZona = int(self.nivelZona.currentItemData() or 0)
		if self.idNivelZona == 1:
			cols = [ 'z.id' ]
			cn = [ 'z_id' ]
			tablas = [ 'zona z' ]
			where = [ 'cz.idzona = z.id',  'z.idnivelzona = 1' ]
		else:
			cols = [ 'z1.id' ]
			cn = [ 'z_id' ]
			tablas = [ 'zona z1',  'relzona rz',  'zona z' ]
			where = [ 'rz.idzonapadre = z1.id', 'cz.idzona = z.id',  'z.idnivelzona = 1',
				 'rz.idzona = z.id',  'z1.idnivelzona = %d' % (self.idNivelZona) ]
		return (cols,  cn,  tablas,  where)

	def hazClasificacion(self):
		if self.soloClasificacion.isChecked():
			clas = str(self.nivelClasificacion.currentItemData() or "")
			idClasificacion = int(self.clasificacion.currentItemData() or 0)
			cols = [ ]
			cn = [ ]
			if clas[0:4] == "SNAP":
				tablas = [ 'clasificacion cl',  'clasificacion cl2' ]
				where = [ 'cz.idclasificacion = cl2.id',
					'substr(cl2.codigo, 1, length(cl.codigo)) = cl.codigo',
					'cl.id = %d' % (idClasificacion) ]
			elif clas[0:4] == "IPCC":
				tablas = [ 'clasificacion cl', 'clasificacion cl2',
					'equivclasificacion ecl', 'clasificacion clo' ]
				where = [ 'cz.idclasificacion = clo.id',
					'clo.id = ecl.idclasorig',
					'cl2.id = ecl.idclasmap',
					'substr(cl2.codigo, 1, length(cl.codigo)) = cl.codigo',
					'cl.id = %d' % (idClasificacion) ]
		elif self.agregaClasificacion.isChecked():
			cols = []
			cn = []
			tablas = []
			where = []
		return (cols,  cn,  tablas,  where)

	def hazQuery(self):
		(cc,  cn, ct,  cw) = self.hazContaminante()
		(fc,  fn, ft,  fw) = self.hazFuente()
		(zc,  zn, zt,  zw) = self.hazZona()
		(clc,  cln, clt,  clw) = self.hazClasificacion()
		c = zc + cc + fc + clc + [ 'sum(cz.valor)' ]
		n = zn + cn + fn + cln + [ '"Emisión"' ]
		if len(c) > 2:
			c = c[0:2]
			n = n[0:2]
		t = ct + ft + zt + clt + [ 'contaminantezona cz' ]
		w = cw + fw + zw + clw + [ ]
		g1 = cc + fc + zc + clc
		g = []
		for i in g1:
			if i[0:4] != "sum(":
				g.append(i)
		ccn = [ "%s as %s" % (str(c[i]), str(n[i])) for i in range(len(c)) ]
		sc = ', '.join(ccn)
		st = ', '.join(t)
		sw = ' and '.join(w)
		sg = ', '.join(g)
		sql = "select %s from %s" % (str(sc),  str(st))
		if len(w) > 0:
			sql = sql + " where %s" % (sw)
		if len(g) > 0:
			sql = sql + " group by %s" % (sg)
		return sql

	def accept(self):
		self.sql = self.hazQuery()
		self.color = self.comboColor.currentText()
#		print self.sql
		QDialog.accept(self)

