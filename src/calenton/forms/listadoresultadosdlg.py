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
# $Id: listadoresultadosdlg.py 268 2010-05-24 13:01:28Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/listadoresultadosdlg.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_listadoresultadosdlg import *
from .listaresultadodlg import *
from ts import ComboDataModel

class ListadoResultadosDlg (QDialog, Ui_ListadoResultadosDlgClass):
	def __init__(self, parent = None):
		QDialog.__init__(self, parent)
		self.setupUi(self)

		self.app = QApplication.instance()
		if not self.app.databaseInit:
			return
		self.db = self.app.workDb()

		self.gc = QButtonGroup(self)
		self.gc.addButton(self.agregaContaminante)
		self.gc.addButton(self.todosContaminante)
		self.gc.addButton(self.soloContaminante)
		self.gf = QButtonGroup(self)
		self.gf.addButton(self.agregaFuente)
		self.gf.addButton(self.todosFuente)
		self.gf.addButton(self.soloFuente)
		self.gz = QButtonGroup(self)
		self.gz.addButton(self.agregaZona)
		self.gz.addButton(self.todosZona)
		self.gz.addButton(self.soloZona)
		self.gcl = QButtonGroup(self)
		self.gcl.addButton(self.agregaClasificacion)
		self.gcl.addButton(self.todosClasificacion)
		self.gcl.addButton(self.soloClasificacion)

		self.agregaContaminante.setChecked(True)
		self.agregaFuente.setChecked(True)
		self.agregaZona.setChecked(True)
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

		self.mZona = ComboDataModel(self)
		self.on_nivelZona_activated(0)
		self.zona.setModel(self.mZona)

		self.llena_nivelClasificacion()

		self.mClasificacion = ComboDataModel(self)
		self.on_nivelClasificacion_activated(0)
		self.clasificacion.setModel(self.mClasificacion)

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
		self.mZona.setQuery("select id, nombre from zona where idnivelzona = %d order by nombre"
		                    	% (self.idNivelZona),  self.db)

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
		if self.todosContaminante.isChecked():
			cols = [ 'co.nombre', 'sum(cz.valor * coalesce(ec.p, 0.0))' ]
			cn = [ 'Contaminante', '"Toneladas equivalentes"' ]
			tablas = [
				"""contaminante co
					left outer join equivcontaminante ec on
						ec.idescenario = %d and
						ec.idcontaminante = co.id""" % (self.idEscenario) ]
			where = [ 'co.id = cz.idcontaminante' ]
		elif self.soloContaminante.isChecked():
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
		if self.todosFuente.isChecked():
			cols = [ 'f.nombre' ]
			cn = [ 'Fuente' ]
			tablas = [ 'fuente f' ]
			where = [ 'cz.idfuente = f.id',  'f.idescenario = %d' % (self.idEscenario) ]
		elif self.soloFuente.isChecked():
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
		if self.todosZona.isChecked():
			idNivelZona = int(self.nivelZona.currentItemData() or 0)
			idZona = int(self.zona.currentItemData() or 0)
			if idNivelZona == 1:
				cols = [ 'z.nombre' ]
				cn = [ 'Zona' ]
				tablas = [ 'zona z' ]
				where = [ 'cz.idzona = z.id',  'z.idnivelzona = 1' ]
			else:
				cols = [ 'z1.nombre' ]
				cn = [ 'Zona' ]
				tablas = [ 'zona z1',  'relzona rz',  'zona z' ]
				where = [ 'rz.idzonapadre = z1.id', 'cz.idzona = z.id',  'z.idnivelzona = 1',
				         'rz.idzona = z.id',  'z1.idnivelzona = %d' % (idNivelZona) ]
		elif self.soloZona.isChecked():
			idNivelZona = int(self.nivelZona.currentItemData() or 0)
			idZona = int(self.zona.currentItemData() or 0)
			if idNivelZona == 1:
				cols = []
				cn = []
				tablas = []
				where = [ 'cz.idzona = %d' % (idZona) ]
			else:
				cols = []
				cn = []
				tablas = [ 'relzona rz',  'zona z' ]
				where = [ 'rz.idzonapadre = %d' % (idZona), 'cz.idzona = z.id',  'z.idnivelzona = 1',
				         'rz.idzona = z.id' ]
		elif self.agregaZona.isChecked():
			cols = []
			cn = []
			tablas = []
			where = []
		return (cols,  cn,  tablas,  where)

	def hazClasificacion(self):
		if self.todosClasificacion.isChecked():
			clas = str(self.nivelClasificacion.currentItemData() or "")
			cols = [ "cl.codigo || '-' || cl.descripcion" ]
			cn = [ '"Clasificación"' ]
			tablas = [ 'clasificacion cl' ]
			where = []
			if clas[0:4] == "SNAP":
				where.append('cl.idtipoclas = 3')
				if clas == "SNAP1":
					tablas = tablas + [ 'clasificacion cl2' ]
					where = where + [ 'length(cl.codigo) = 2',
					        	'cz.idclasificacion = cl2.id',
							'substr(cl2.codigo, 1, 2) = cl.codigo' ]
				elif clas == "SNAP2":
					tablas = tablas + [ 'clasificacion cl2' ]
					where = where + [ 'length(cl.codigo) = 5',
					        	'cz.idclasificacion = cl2.id',
							'substr(cl2.codigo, 1, 5) = cl.codigo' ]
				elif clas == "SNAP3":
					where = where + [ 'length(cl.codigo) = 8',
					        	'cz.idclasificacion = cl.id' ]
			elif clas[0:4] == "IPCC":
				where.append("cl.idtipoclas = 4")
				tablas = tablas + [ 'clasificacion cl2', 'equivclasificacion ecl', 'clasificacion clo' ]
				if clas == "IPCC1":
					codLen = 1
				elif clas == "IPCC2":
					codLen = 2
				elif clas == "IPCC3":
					codLen = 3
				where = where + [ "length(cl.codigo) = %d" % (codLen),
						"cz.idclasificacion = clo.id",
						"clo.id = ecl.idclasorig",
						"cl2.id = ecl.idclasmap",
						"substr(cl2.codigo, 1, %d) = cl.codigo" % (codLen) ]
		elif self.soloClasificacion.isChecked():
			clas = str(self.nivelClasificacion.currentItemData() or "")
			idClasificacion = int(self.clasificacion.currentItemData() or 0)
			cols = [ "cl.codigo || '-' || cl.descripcion" ]
			cn = [ '"Clasificación"' ]
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
		c = cc + fc + zc + clc + [ 'sum(cz.valor)' ]
		n = cn + fn + zn + cln + [ '"Emisión"' ]
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
		sql = self.hazQuery()
		dlg = ListaResultadoDlg(sql,  self.db,  self)
		dlg.exec()
		# QDialog.accept(self)

