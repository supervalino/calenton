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
# $Id: graphiclist.py 352 2010-11-15 22:59:33Z picazo $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/graphiclist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_graphiclist import *
from .graphicdlg import GraphicDlg
from ..widgets.datalist import DataList
from ts import ComboDataModel
from ..informe.funciones import *
#from ..informe.colores import miColor
import cairo
import pycha.bar
import pycha.stackedbar
import pycha.pie
import pycha.line

from configobj import ConfigObj

#from ts import FKItemDelegate

class GraphicList (DataList, Ui_GraphicListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		app = QApplication.instance()
		self.tabla.selectionModel().selectionChanged.connect(self.tabla_selectionChanged)
		self.work = QSqlDatabase.database('work')
#		self.cambiosSinGuardar = 0
		self.idEscenario = -1
		self.mEscenario = ComboDataModel(self)
		self.mEscenario.setQuery("select id, nombre from escenario order by id", self.work)
		self.escenario.setModel(self.mEscenario)

		self.dirGrap = QDir("reports/%s" % (app.informeActivo()))
		self.cargaTabla()

	def cargaTabla(self):
		self.dirGrap.setNameFilters(["g_*.dat"])
		self.listaGrapF = self.dirGrap.entryList()
		self.nGrap = len(self.listaGrapF)
		self.tabla.setRowCount(self.nGrap)
		self.tabla.setColumnCount(1)
		encabezado = [self.tr("Fichero")]
		#<< self.tr("Descripción") << self.tr("SQL")
		self.tabla.setHorizontalHeaderLabels(encabezado)
		if self.nGrap==0 :
			return
		for i in range(0,self.nGrap):
			nombre=self.listaGrapF[i].split(".")[0]
			self.tabla.setItem(i, 0, QTableWidgetItem(self.listaGrapF[i]))
		self.tabla.resizeColumnsToContents()
		self.tabla.resizeRowsToContents()
		self.elimina.setEnabled(False)
		self.edita.setEnabled(False)
		self.crear.setEnabled(False)
		self.anade.setEnabled(False) # quitar cuando este hecho el dialogo editar

	def filasSeleccionadas(self):
		filas = []
		i = -1
		for g in self.tabla.selectedIndexes():
			filas.append(g.row())
		ln = reduce(lambda l, x: x not in l and l.append(x) or l, filas, [])
		ln.sort()
		return ln

	def creaGrap(self, i):
		nombre=self.tabla.item(i, 0).text().split(".")[0]
		nombreF=self.dirGrap.filePath(nombre) + ".eps"
		nombreDat=self.dirGrap.filePath(nombre) + ".dat"
		cfg = leeConf(nombreDat, 'g')

		if not cfg['ipcc'] == '0':
			cfg['sql'],cfg['filas'] = self.sqlTipoB_listaIPCC(cfg['ipcc'], cfg['contaminantes'], cfg['provincia'])

		ds0 = dataSetGlobal(cfg, self.idEscenario, self.work)

		if len(ds0) == 0:
			QMessageBox.warning(self, self.tr("Error al crear la gráfica"),
					self.tr("No hay datos"),
					QMessageBox.StandardButton.Ok)
			return

		if '1' in cfg['tipo']:
			grafPychart(nombreF, ds0, cfg)
		elif '2' in cfg['tipo']:
			grafPycha(nombreF, ds0, cfg)

	def sqlTipoB_listaIPCC(self, ipcc, contaminantes, lProvincia):
		sql_cls2 = "select codigo from clasificacion where idtipoclas=4 and codigo~'^%s' order by codigo" % ipcc
		q = QSqlQuery(sql_cls2, self.work)
		lista_ipcc = []
		while q.next():
			lista_ipcc.append(str(q.value(0) or ""))
		fila = []
		filas = {}
		sql_lista = {}
		n=0
		sql_cte = ''' cte.nombre='%s' ''' % contaminantes.pop(0)
		for cte in contaminantes:
			sql_cte = sql_cte + ''' or cte.nombre='%s' ''' % cte
		for i in lista_ipcc:
			sql = ''
			sqln = 'sql'+ dosCifras(n)
			n = n + 1
			ipcc_fila = i
			if not len(lProvincia) == 0:
				for j in lProvincia:
					sql = sql + ''',(select sum(cz.valor * coalesce(ec.p, 0.0))
								FROM contaminantezona cz, contaminante cte, clasificacion cl, equivcontaminante ec
								where cz.idfuente in (select id from fuente where idescenario = _ESCENARIO_)
									and cz.idzona in
										(select idzona from relzona,zona z where
											idzonapadre=z.id and z.nombre='PROVINCIA DE %s')
									and cte.id=cz.idcontaminante
									and ec.idescenario = _ESCENARIO_
									and ec.idcontaminante = cte.id
									and cl.id=cz.idclasificacion
									and cl.id in (select cl.id from clasificacion cl, clasificacion clo, equivclasificacion ecl
													where clo.codigo = '%s'
													and cl.id = ecl.idclasorig
													and clo.id = ecl.idclasmap)
									and (%s) )''' % (j, ipcc_fila, sql_cte)
			else:
				sql = ''',(select sum(cz.valor * coalesce(ec.p, 0.0))
							FROM contaminantezona cz, contaminante cte, clasificacion cl, equivcontaminante ec
							where cz.idfuente in (select id from fuente where idescenario = _ESCENARIO_)
								and cte.id=cz.idcontaminante
								and ec.idescenario = _ESCENARIO_
								and ec.idcontaminante = cte.id
								and cl.id=cz.idclasificacion
								and cl.id in (select cl.id from clasificacion cl, clasificacion clo, equivclasificacion ecl
												where clo.codigo = '%s'
												and cl.id = ecl.idclasorig
												and clo.id = ecl.idclasmap)
								and (%s) )''' % (ipcc_fila, sql_cte)

			vars()[sqln] = '''select (select codigo from clasificacion
						where idtipoclas=4
						and codigo='%s') %s
						''' % (ipcc_fila, sql)
			sql_lista[sqln]= vars()[sqln]
			fila.append(sqln)

#		filas['fila1'] = fila
		return sql_lista, fila


	def escribeDat(self, d):
		nombre = d.nombre.text().strip()
		nombreDat=self.dirGrap.filePath(nombre) + ".dat"
		config = ConfigObj(str(nombreDat), encoding='UTF8')
		config['titulo'] = str(d.titulo.text().strip())
		config['nombreX'] = str(d.nombreX.text().strip())
		config['nombreY'] = str(d.nombreY.text().strip())
		if d.barras.isChecked():
			tipo = self.tr("barras")
		elif d.barrasAc.isChecked():
			tipo = self.tr("barrasAc")
		elif d.tarta.isChecked():
			tipo = self.tr("tarta")
		elif d.lineas.isChecked():
			tipo = self.tr("lineas")
		else:
			tipo = barras
		config['tipo'] = tipo
		config['descripcion'] = str(d.descripcion.toPlainText().strip())
		config['sql'] = str(d.sql.toPlainText().strip())
		config.write()
		self.cargaTabla()

	@pyqtSlot(int)
	def on_escenario_activated(self, index):
		self.idEscenario = -1
		ide = self.escenario.currentItemData()
		if ide is not None:
			i = int(ide or 0)
			if i:
				self.idEscenario = i

	@pyqtSlot(bool)
	def on_anade_clicked(self, checked):
		d = GraphicDlg(self)
		if d.exec():
			nombre = d.nombre.text().strip()
			nombreF=self.dirGrap.filePath(nombre) + ".eps"
			nombreDat=self.dirGrap.filePath(nombre) + ".dat"
			F=QFile(nombreF)
			F.open(QFile.WriteOnly)
			F.close()
			self.escribeDat(d)
			self.cargaTabla()


	@pyqtSlot(bool)
	def on_elimina_clicked(self, checked):
		res = QMessageBox.question(self, self.tr("¿Está seguro?"),
				self.tr("¿Desea eliminar los gráficos seleccionados?\n" +
					"Esta operación es permanente e irreversible"),
				QMessageBox.StandardButton.Yes | QMessageBox.Escape,
				QMessageBox.StandardButton.No | QMessageBox.Default)
		if res != QMessageBox.StandardButton.Yes:
			return
		for i in self.filasSeleccionadas():
			nombre=self.tabla.item(i, 0).text().split(".")[0]
			nombreF=self.dirGrap.filePath(nombre) + ".eps"
			nombreD=self.dirGrap.filePath(nombre) + ".txt"
			nombreS=self.dirGrap.filePath(nombre) + ".sql"
			F = QFile(nombreF)
			if not F.remove(nombreF):
				self.cargaTabla()
				return
			F = QFile(nombreD)
			F.remove(nombreD)
			F = QFile(nombreS)
			F.remove(nombreS)
		self.cargaTabla()


	@pyqtSlot(bool)
	def on_crear_clicked(self, checked):
		if self.idEscenario == -1:
			QMessageBox.warning(None, self.tr("Falta escenario"),
					self.tr("Es necesario primero elegir un escenario"),
					QMessageBox.StandardButton.Ok)
			return False
		for i in self.filasSeleccionadas():
			self.creaGrap(i)

	@pyqtSlot(bool)
	def on_crearTodas_clicked(self, checked):
		if self.idEscenario == -1:
			QMessageBox.warning(None, self.tr("Falta escenario"),
					self.tr("Es necesario primero elegir un escenario"),
					QMessageBox.StandardButton.Ok)
			return False
		for i in range(self.nGrap):
			self.creaGrap(i)

	@pyqtSlot("const QModelIndex &")
	def on_tabla_doubleClicked(self, index):
		True
#		i = index.row()
#		nombreBase0 = self.tabla.item(i, 0).text().split(".")[0]
#		nombreDat=self.dirGrap.filePath(nombreBase0) + ".dat"
#		config = ConfigObj(str(nombreDat), encoding='UTF8')
#		d = GraphicDlg(self)
#		d.nombre.setText(nombreBase0)
#		d.descripcion.setText(config['descripcion'])
#		d.sql.setText(config['sql'])
#		d.titulo.setText(config['titulo'])
#		d.nombreX.setText(config['nombreX'])
#		d.nombreY.setText(config['nombreY'])
#		tipo = config['tipo']
#		if tipo == "barras":
#			d.barras.setChecked(True)
#		if tipo == "barrasAc":
#			d.barrasAc.setChecked(True)
#		if tipo == "tarta":
#			d.tarta.setChecked(True)
#		if tipo == "lineas":
#			d.lineas.setChecked(True)
#		if d.exec():
#			nombreBase = d.nombre.text().strip()
#			nombreF=self.dirGrap.filePath(nombreBase0) + ".eps"
#			nombreDat=self.dirGrap.filePath(nombreBase0) + ".dat"
#			F=QFile(nombreF)
#			F.rename(self.dirGrap.filePath(nombreBase) + ".eps")
#			self.escribeDat(d)
#			self.cargaTabla()

	@pyqtSlot(bool)
	def on_edita_clicked(self, checked):
		l = self.tabla.selectedIndexes()
		if len(self.filasSeleccionadas()) == 1:
			self.on_tabla_doubleClicked(l[0])

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tabla_selectionChanged(self, after, before):
		l = self.filasSeleccionadas()
#		self.elimina.setEnabled(len(l) > 0)
#		self.edita.setEnabled(len(l) == 1)
		self.crear.setEnabled(len(l) > 0)
