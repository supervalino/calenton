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
# $Id: zonalist.py 362 2010-11-30 15:33:05Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/zonalist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_zonalist import *
from .zonadlg import ZonaDlg
from ..widgets.datalist import DataList
from ts import ComboDataModel, FKItemDelegate

class ZonaList (DataList, Ui_ZonaListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		app = QApplication.instance()
		if not app.databaseInit:
			return

		self.db = app.workDb()

		self.model = app.mZonas
		self.model.setParentId(-1)
		self.idZona = -1
		self.tabla.setModel(self.model)
		self.tabla.hideColumn(self.model.fieldIndex("id"))
		self.tabla.selectionModel().selectionChanged.connect(self.tabla_selectionChanged)
		self.cambiaEncabezado(self.model, ['Nivel', 'Nombre'])
		self.tabla.resizeColumnsToContents()
		self.tabla.resizeRowsToContents()

		self.idNivelZona = -1
		self.mNivelZonas = app.mNivelZonas
		self.tablaNiveles.setModel(self.mNivelZonas)
		self.tablaNiveles.hideColumn(self.model.fieldIndex('id'))
		self.tablaNiveles.resizeColumnsToContents()
		self.tablaNiveles.resizeRowsToContents()
		self.tablaNiveles.selectionModel().selectionChanged.connect(
					self.tablaNiveles_selectionChanged)

		self.mDatoZona = app.mDatoZona
		self.tablaDatos.setModel(self.mDatoZona)
		self.tablaDatos.hideColumn(self.mDatoZona.fieldIndex('id'))
		self.cambiaEncabezado(self.mDatoZona, ['Zona', 'Tipo de dato', 'valor'])
#		self.mDatoZona.primeInsert.connect(self.tablaDatos_primeInsert)
		self.tablaDatos.setItemDelegateForColumn(
					self.mDatoZona.fieldIndex("idtipodatozona"),
					FKItemDelegate({'idescenario': -1 }, self))
		self.tablaDatos.setItemDelegateForColumn(
					self.mDatoZona.fieldIndex('idzona'),
					FKItemDelegate({'idnivelzona': -1 }, self))
		self.tablaDatos.selectionModel().selectionChanged.connect(
					self.tablaDatos_selectionChanged)

		self.mParametroZona = app.mParametroZona
		self.tablaParametros.setModel(self.mParametroZona)
		self.tablaParametros.hideColumn(self.mParametroZona.fieldIndex('id'))
		self.cambiaEncabezado(self.mParametroZona, ['Zona', 'Parametro', 'valor'])
#		self.mParametroZona.primeInsert.connect(self.tablaParametros_primeInsert)
		self.mParametroZona.layoutChanged.connect(self.tablaParametros_layoutChanged)
		self.tablaParametros.setItemDelegateForColumn(
					self.mParametroZona.fieldIndex('idzona'),
					FKItemDelegate({'idnivelzona': -1 }, self))
		self.tablaParametros.setItemDelegateForColumn(
					self.mParametroZona.fieldIndex('idparametro'),
					FKItemDelegate({'idescenario': -1 }, self))
		self.tablaParametros.selectionModel().selectionChanged.connect(
					self.tablaParametros_selectionChanged)

		self.idEscenario = -1
		self.idEscenarioParam = -1
		self.mEscenario = ComboDataModel(self)
		self.mEscenario.setQuery("select id, nombre from escenario order by id", self.db)
		self.escenario.setModel(self.mEscenario)
		self.escenarioParam.setModel(self.mEscenario)

		self.cambiaDatos()

	@pyqtSlot(bool)
	def on_anade_clicked(self, checked):
		d = ZonaDlg(self, self.model)
		if d.add():
			self.model.submitTrans()
		self.ordenaZonas()

	@pyqtSlot(bool)
	def on_elimina_clicked(self, checked):
		self.askAndRemoveRows(self.tabla, self.model)
		self.ordenaZonas()

	@pyqtSlot(QModelIndex)
	def on_tabla_doubleClicked(self, index):
		dm = ZonaDlg(self, self.model)
		if dm.edit(index.row()):
			self.model.submitTrans()
		self.ordenaZonas()


	@pyqtSlot(bool)
	def on_edita_clicked(self, checked):
		l = self.tabla.selectedIndexes()
		l2 = self.model.selectedRows(l)
		if len(l2) == 1:
			self.on_tabla_doubleClicked(l[0])

	@pyqtSlot(QItemSelection, QItemSelection)
	def tabla_selectionChanged(self, before, after):
		l = self.tabla.selectionModel().selectedIndexes()
		self.elimina.setEnabled(self.model.eraseActive(l))
		self.idZona = self.model.getId(l)
		self.edita.setEnabled(self.idZona > 0)
		self.cambiaDatos()
		self.cambiaParametros()

	@pyqtSlot(QItemSelection, QItemSelection)
	def tablaNiveles_selectionChanged(self, before, after):
		l = self.tablaNiveles.selectionModel().selectedIndexes()
		self.idNivelZona = self.mNivelZonas.getId(l)
		self.tablaDatos.itemDelegateForColumn(self.mDatoZona.fieldIndex('idzona')
				).setFilterValue('idnivelzona', self.idNivelZona)
		self.tablaParametros.itemDelegateForColumn(self.mParametroZona.fieldIndex('idzona')
				).setFilterValue('idnivelzona', self.idNivelZona)
		self.model.setParentId(self.idNivelZona)
		self.tabla.resizeColumnsToContents()
		self.tabla.resizeRowsToContents()
		self.tabla_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(int)
	def on_escenario_activated(self, index):
		self.cambiaDatos()

	def cambiaDatos(self):
		ide = self.escenario.currentItemData()
		self.idEscenario = -1
		if ide is not None:
			try:
				self.idEscenario = int(ide)
			except (ValueError, TypeError):
				self.idEscenario = -1
		self.tablaDatos.itemDelegateForColumn(
				self.mDatoZona.fieldIndex('idtipodatozona')
				).setFilterValue('idescenario', self.idEscenario)
		self.mDatoZona.revertAll()
		self.mDatoZona.setFilter("""
			idzona = %d and
			idtipodatozona in (
				select id from tipodatozona where idescenario = %d
				)
			""" % (self.idZona, self.idEscenario))
		self.tablaDatos_selectionChanged(QItemSelection(), QItemSelection())
		self.tablaDatos.resizeColumnsToContents()
		self.tablaDatos.resizeRowsToContents()

	def tablaDatos_contextualMenuActions(self):
		if self.idNivelZona > 0 and self.idEscenario > 0:
			return [ self.clipboardDatos ]
		else:
			return None

	@pyqtSlot(bool)
	def on_anadeDatos_clicked(self, checked):
		row = self.mDatoZona.rowCount()
		if self.idZona > 0:
			r = self.mDatoZona.record()
			r.setValue('idzona', self.idZona)
			self.mDatoZona.insertRecord(row, r)
		else:
			self.mDatoZona.insertRow(row)
		idx = self.mDatoZona.index(row, 1)
		if row == 0:
			self.tablaDatos.resizeColumnsToContents()
			self.tablaDatos.resizeRowsToContents()
		self.tablaDatos.setCurrentIndex(idx)
		self.tablaDatos.edit(idx)

	@pyqtSlot(bool)
	def on_guardaDatos_clicked(self, checked):
		self.mDatoZona.submitTrans()
		self.tablaDatos_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(bool)
	def on_descartaDatos_clicked(self, checked):
		self.cambiaDatos()

	@pyqtSlot(bool)
	def on_eliminaDatos_clicked(self, checked):
		self.askAndRemoveRows(self.tablaDatos, self.mDatoZona)
		self.cambiaDatos()

	@pyqtSlot(int, QSqlRecord)
	def tablaDatos_primeInsert(self, row, record):
		if self.idZona > 0:
			record.setValue('idzona', self.idZona)

	@pyqtSlot(QItemSelection, QItemSelection)
	def tablaDatos_selectionChanged(self, before, after):
		l = self.tablaDatos.selectionModel().selectedIndexes()
		self.guardaDatos.setEnabled(self.mDatoZona.pendingChanges())
		self.descartaDatos.setEnabled(self.mDatoZona.pendingChanges())
		self.escenario.setEnabled(not self.mDatoZona.pendingChanges())
		self.anadeDatos.setEnabled(self.idZona > 0 and self.idEscenario > 0)
		self.eliminaDatos.setEnabled(len(l) > 0)
		self.tab.setLocked(self.mDatoZona.pendingChanges())

	def insertDataDatos(self, data):
		fields = [ 'idzona', 'idtipodatozona', 'dato' ]
		filters = [ { 'idnivelzona': self.idNivelZona },
					{ 'idescenario': self.idEscenario },
					{}]
		order = [ 'idzona', 'idtipodatozona', 'dato' ]
		try:
			self.mDatoZona.addRows(fields, data, filters, order)
		finally:
			self.tablaDatos.resizeColumnsToContents()
			self.tablaDatos.resizeRowsToContents()
			self.tablaDatos_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(bool)
	def on_clipboardDatos_triggered(self, checked):
		self.getDataFromClipboard(checked, self.insertDataDatos)

	@pyqtSlot(int)
	def on_escenarioParam_activated(self, index):
		self.cambiaParametros()

	def cambiaParametros(self):
		ide = self.escenarioParam.currentItemData()
		self.idEscenarioParam = -1
		if ide is not None:
			try:
				self.idEscenarioParam = int(ide)
			except (ValueError, TypeError):
				self.idEscenarioParam = -1
		self.tablaParametros.itemDelegateForColumn(
				self.mParametroZona.fieldIndex('idparametro')
				).setFilterValue('idescenario', self.idEscenario)
		self.mParametroZona.revertAll()
		self.mParametroZona.setFilter("""
			idzona = %d and
			idparametro in (
				select id from parametro where idescenario = %d
				)
			""" % (self.idZona, self.idEscenarioParam))
		self.tablaParametros_selectionChanged(QItemSelection(), QItemSelection())
		self.tablaParametros.resizeColumnsToContents()
		self.tablaParametros.resizeRowsToContents()

	def tablaParametros_contextualMenuActions(self):
		if self.idNivelZona > 0 and self.idEscenarioParam > 0:
			return [ self.clipboardParametros ]
		else:
			return None

	@pyqtSlot(bool)
	def on_anadeParametros_clicked(self, checked):
		row = self.mParametroZona.rowCount()
		if self.idZona > 0:
			r = self.mParametroZona.record()
			r.setValue('idzona', self.idZona)
			self.mParametroZona.insertRecord(row, r)
		else:
			self.mParametroZona.insertRow(row)
		idx = self.mParametroZona.index(row, 1)
		if row == 0:
			self.tablaParametros.resizeColumnsToContents()
			self.tablaParametros.resizeRowsToContents()
		self.tablaParametros.setCurrentIndex(idx)
		self.tablaParametros.edit(idx)

	@pyqtSlot(bool)
	def on_eliminaParametros_clicked(self, checked):
		self.askAndRemoveRows(self.tablaParametros, self.mParametroZona)
		self.cambiaDatos()

	@pyqtSlot(bool)
	def on_guardaParametros_clicked(self, checked):
		self.mParametroZona.submitTrans()
		self.tablaParametros_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(bool)
	def on_descartaParametros_clicked(self, checked):
		self.cambiaParametros()

	@pyqtSlot()
	def tablaParametros_layoutChanged(self):
		print("Hola")

	@pyqtSlot(int, QSqlRecord)
	def tablaParametros_primeInsert(self, row, record):
		if self.idZona > 0:
			record.setValue('idzona', self.idZona)

	@pyqtSlot(QItemSelection, QItemSelection)
	def tablaParametros_selectionChanged(self, before, after):
		l = self.tablaParametros.selectionModel().selectedIndexes()
		self.guardaParametros.setEnabled(self.mParametroZona.pendingChanges())
		self.descartaParametros.setEnabled(self.mParametroZona.pendingChanges())
		self.escenarioParam.setEnabled(not self.mParametroZona.pendingChanges())
		self.anadeParametros.setEnabled(self.idZona > 0 and self.idEscenarioParam > 0)
		self.eliminaParametros.setEnabled(len(l) > 0)
		self.tab.setLocked(self.mParametroZona.pendingChanges())

	def insertDataParametros(self, data):
		fields = [ 'idzona', 'idparametro', 'valor' ]
		filters = [ { 'idnivelzona': self.idNivelZona },
					{ 'idescenario': self.idEscenario },
					{}]
		order = [ 'idzona', 'idparametro', 'valor' ]
		try:
			self.mParametroZona.addRows(fields, data, filters, order)
		finally:
			self.tablaParametros.resizeColumnsToContents()
			self.tablaParametros.resizeRowsToContents()
			self.tablaParametros_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(bool)
	def on_clipboardParametros_triggered(self, checked):
		self.getDataFromClipboard(checked, self.insertDataParametros)
