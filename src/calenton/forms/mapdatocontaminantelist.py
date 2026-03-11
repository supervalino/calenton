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
# $Id: mapdatocontaminantelist.py 189 2010-04-09 09:21:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/mapdatocontaminantelist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_mapdatocontaminantelist import *
from .mapdatocontaminantedlg import MapDatoContaminanteDlg
from ..widgets.datalist import DataList
from ts import FKItemDelegate
from ts import ComboDataModel
from ..modelo import arbolclasificacion
from ..modelo import dato
class MapDatoContaminanteList (DataList, Ui_MapDatoContaminanteListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		app = QApplication.instance()
		if not app.databaseInit:
			return

		self.db = app.workDb()

		self.idEscenario = -1
		self.idTipoClas = -1
		self.idClasificacion = -1
		self.idDato = -1

		self.model = app.mMapDatoContaminante
		self.model.setMultipleParents({ 'iddato': self.idDato })
		self.idSel = -1

		self.mMapDatoContaminanteClas = app.mMapDatoContaminanteClas
		self.mMapDatoContaminanteClas.setMultipleParents({ 'idclasificacion': -1 })
		self.idMapDatoContaminanteClas = -1

		self.cambiaEncabezado(self.model,
					['Escenario', 'Dato', 'Clasificación',
						'Contaminante', 'idformula', 'Formula'])
		self.tablaMap.setModel(self.model)
		self.tablaMap.hideColumn(self.model.fieldIndex("id"))
		self.tablaMap.hideColumn(self.model.fieldIndex("idformula"))
		self.tablaMap.setItemDelegateForColumn(self.model.fieldIndex("idescenario"),
					FKItemDelegate({}, self))
		self.tablaMap.setItemDelegateForColumn(self.model.fieldIndex("iddato"),
					FKItemDelegate({}, self))
		self.tablaMap.setItemDelegateForColumn(self.model.fieldIndex("idclasificacion"),
					FKItemDelegate({}, self))
		self.tablaMap.setItemDelegateForColumn(self.model.fieldIndex("idcontaminante"),
					FKItemDelegate({}, self))
		self.tablaMap.selectionModel().selectionChanged.connect(self.tablaMap_selectionChanged)
		self.tablaMap.resizeColumnsToContents()
		self.tablaMap.resizeRowsToContents()

		self.cambiaEncabezado(self.mMapDatoContaminanteClas,
					['Escenario', 'Dato', 'Clasificación',
						'Contaminante', 'idformula', 'Formula'])
		self.tablaMapClas.setModel(self.mMapDatoContaminanteClas)
		self.tablaMapClas.hideColumn(self.mMapDatoContaminanteClas.fieldIndex("id"))
		self.tablaMapClas.hideColumn(self.mMapDatoContaminanteClas.fieldIndex("iddato"))
		self.tablaMapClas.hideColumn(self.mMapDatoContaminanteClas.fieldIndex("idformula"))
		self.tablaMapClas.setItemDelegateForColumn(self.mMapDatoContaminanteClas.fieldIndex("idescenario"),
					FKItemDelegate({}, self))
		self.tablaMapClas.setItemDelegateForColumn(self.mMapDatoContaminanteClas.fieldIndex("idclasificacion"),
					FKItemDelegate({}, self))
		self.tablaMapClas.setItemDelegateForColumn(self.mMapDatoContaminanteClas.fieldIndex("idcontaminante"),
					FKItemDelegate({}, self))
		self.tablaMapClas.selectionModel().selectionChanged.connect(self.tablaMapClas_selectionChanged)
		self.tablaMapClas.resizeColumnsToContents()
		self.tablaMapClas.resizeRowsToContents()

		self.mEscenario = app.mEscenario
		self.tablaEscenario.setModel(self.mEscenario)
		self.tablaEscenario.resizeColumnsToContents()
		self.tablaEscenario.resizeRowsToContents()
		self.tablaEscenario.selectionModel().selectionChanged.connect(
					self.tablaEscenario_selectionChanged)

		self.mDato = dato.Dato(self, self.db)
		self.mDato.setParentId(self.idClasificacion)
		self.mDato.select()
		self.tablaDato.setModel(self.mDato)
		self.tablaDato.resizeColumnsToContents()
		self.tablaDato.resizeRowsToContents()
		self.tablaDato.selectionModel().selectionChanged.connect(
					self.tablaDato_selectionChanged)

		self.mClasificacion = arbolclasificacion.ArbolClasificacion(self.idTipoClas, self.db, self)
		self.arbolClasificacion.setModel(self.mClasificacion)
		self.arbolClasificacion.selectionModel().selectionChanged.connect(
							self.arbolClasificacion_selectionChanged)

		self.modelTipo = ComboDataModel(self)
		self.modelTipo.setQuery("select id, nombre from tipoclas order by id", self.db)
		self.comboTipoClasificacion.setModel(self.modelTipo)

	######################################################################
	# Escenario
	#

	@pyqtSlot(QItemSelection, QItemSelection)
	def tablaEscenario_selectionChanged(self, after, before):
		l = self.tablaEscenario.selectionModel().selectedIndexes()
		self.idEscenario = self.mEscenario.getId(l)
		self.model.setMultipleParents({ 'iddato' : self.idDato, 'idescenario' : self.idEscenario })
		self.tablaMap_selectionChanged(QItemSelection(), QItemSelection())

	######################################################################
	# Clasificación
	#

	@pyqtSlot(int)
	def on_comboTipoClasificacion_currentIndexChanged(self, index):
		ide = self.comboTipoClasificacion.currentItemData()
		if ide is not None:
			try:
				self.idTipoClas = int(ide)
			except (ValueError, TypeError):
				self.idTipoClas = -1
		else:
			self.idTipoClas = -1
		self.mClasificacion.setIdTipo(self.idTipoClas)
		self.arbolClasificacion_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(QItemSelection, QItemSelection)
	def arbolClasificacion_selectionChanged(self, after, before):
		l = self.arbolClasificacion.selectionModel().selectedIndexes()
		self.idClasificacion = self.mClasificacion.getId(l)
		self.cambiaMapClas()
		self.mDato.setParentId(self.idClasificacion)
		self.tablaDato.resizeColumnsToContents()
		self.tablaDato.resizeRowsToContents()
		self.tablaDato_selectionChanged(QItemSelection(), QItemSelection())

	######################################################################
	# Dato
	#

	@pyqtSlot(QItemSelection, QItemSelection)
	def tablaDato_selectionChanged(self, after, before):
		l = self.tablaDato.selectionModel().selectedIndexes()
		self.idDato = self.mDato.getId(l)
		self.cambiaMap()

	######################################################################
	# Fórmulas por dato
	#

	@pyqtSlot(QItemSelection, QItemSelection)
	def tablaMap_selectionChanged(self, after, before):
		l = self.tablaMap.selectionModel().selectedIndexes()
		p = self.model.pendingChanges()
		t = self.idEscenario > 0 and self.idClasificacion > 0 and self.idDato > 0 and not p
		self.elimina.setEnabled(self.model.eraseActive(l) and t)
		self.idSel = self.model.getId(l)
		self.edita.setEnabled(self.idSel > 0 and t)
		self.anade.setEnabled(t)

	def cambiaMap(self):
		self.model.setMultipleParents({ 'iddato' : self.idDato, 'idescenario' : self.idEscenario })
		self.tablaMap.hideColumn(self.model.fieldIndex('id'))
		self.tablaMap.hideColumn(self.model.fieldIndex('idformula'))
		self.tablaMap.resizeColumnsToContents()
		self.tablaMap.resizeRowsToContents()
		self.tablaMap_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(QModelIndex)
	def on_tablaMap_doubleClicked(self, index):
		dm = MapDatoContaminanteDlg(self, self.model, self.idEscenario, self.idClasificacion, self.idDato)
		if dm.edit(index.row()):
			self.model.submitTrans()

	@pyqtSlot(bool)
	def on_anade_clicked(self, checked):
		d = MapDatoContaminanteDlg(self, self.model, self.idEscenario, self.idClasificacion, self.idDato)
		if d.add():
			self.model.submitTrans()

	@pyqtSlot(bool)
	def on_elimina_clicked(self, checked):
		self.askAndRemoveRows(self.tablaMap, self.model)

	@pyqtSlot(bool)
	def on_guardar_clicked(self, checked):
		self.model.submitTrans()
		self.anade.setEnabled(True)

	@pyqtSlot(bool)
	def on_descartar_clicked(self, checked):
		self.model.select()
		self.model.revertAll()
		self.anade.setEnabled(True)

	@pyqtSlot(bool)
	def on_edita_clicked(self, checked):
		l = self.tablaMap.selectedIndexes()
		l2 = self.model.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaMap_doubleClicked(l[0])

	def insertDataMapDataContaminante(self, data):
		fields = [ 'idescenario', 'iddato', 'idclasificacion', 'idcontaminante', 'formula_expresion' ]
		filters = [ {},
					{ 'idclasificacion': None },
					{},
					{},
					{} ]
		order = [ 'idescenario', 'idclasificacion', 'iddato', 'idcontaminante', 'formula_expresion' ]
		self.model.addRows(fields, data, filters, order)

	@pyqtSlot(bool)
	def on_clipboardMapDatoContaminante_triggered(self, checked):
		self.getDataFromClipboard(checked, self.insertDataMapDataContaminante)


	def tablaMap_contextualMenuActions(self):
		return [ self.clipboardMapDatoContaminante ]

	######################################################################
	# Fórmulas por clasificación
	#

	@pyqtSlot(QItemSelection, QItemSelection)
	def tablaMapClas_selectionChanged(self, after, before):
		l = self.tablaMapClas.selectionModel().selectedIndexes()
		p = self.mMapDatoContaminanteClas.pendingChanges()
		t = self.idEscenario > 0 and self.idClasificacion > 0 and not p
		self.eliminaMapClas.setEnabled(self.mMapDatoContaminanteClas.eraseActive(l) and t)
		self.idMapDatoContaminanteClas = self.mMapDatoContaminanteClas.getId(l)
		self.editaMapClas.setEnabled(self.idMapDatoContaminanteClas > 0 and t)
		self.anadeMapClas.setEnabled(t)

	def cambiaMapClas(self):
		self.mMapDatoContaminanteClas.setMultipleParents({
						'idclasificacion' : self.idClasificacion,
						'idescenario' : self.idEscenario })
		self.tablaMapClas.hideColumn(self.mMapDatoContaminanteClas.fieldIndex('id'))
		self.tablaMapClas.hideColumn(self.mMapDatoContaminanteClas.fieldIndex('iddato'))
		self.tablaMapClas.hideColumn(self.mMapDatoContaminanteClas.fieldIndex('idformula'))
		self.tablaMapClas.resizeColumnsToContents()
		self.tablaMapClas.resizeRowsToContents()
		self.tablaMapClas_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(QModelIndex)
	def on_tablaMapClas_doubleClicked(self, index):
		dm = MapDatoContaminanteDlg(self, self.mMapDatoContaminanteClas,
					self.idEscenario, self.idClasificacion, -1)
		if dm.edit(index.row()):
			self.mMapDatoContaminanteClas.submitTrans()

	@pyqtSlot(bool)
	def on_anadeMapClas_clicked(self, checked):
		d = MapDatoContaminanteDlg(self, self.mMapDatoContaminanteClas, self.idEscenario,
					self.idClasificacion, -1)
		if d.add():
			self.mMapDatoContaminanteClas.submitTrans()

	@pyqtSlot(bool)
	def on_eliminaMapClas_clicked(self, checked):
		self.askAndRemoveRows(self.tablaMapClas, self.mMapDatoContaminanteClas)

	@pyqtSlot(bool)
	def on_guardarMapClas_clicked(self, checked):
		self.mMapDatoContaminanteClas.submitTrans()
		self.cambiaMapClas()

	@pyqtSlot(bool)
	def on_descartarMapClas_clicked(self, checked):
		self.mMapDatoContaminanteClas.revertAll()
		self.cambiaMapClas()

	@pyqtSlot(bool)
	def on_editaMapClas_clicked(self, checked):
		l = self.tablaMapClas.selectedIndexes()
		l2 = self.mMapDatoContaminanteClas.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaMapClas_doubleClicked(l[0])

	def insertDataMapClasDataContaminante(self, data):
		fields = [ 'idescenario', 'idclasificacion', 'idcontaminante', 'formula_expresion' ]
		self.model.addRows(fields, data)

	@pyqtSlot(bool)
	def on_clipboardMapClasDatoContaminante_triggered(self, checked):
		self.getDataFromClipboard(checked, self.insertDataMapClasDataContaminante)


	def tablaMapClas_contextualMenuActions(self):
		return [ self.clipboardMapClasDatoContaminante ]
