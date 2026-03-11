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
# $Id: fuenteclasificacionlist.py 189 2010-04-09 09:21:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/fuenteclasificacionlist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_fuenteclasificacionlist import *
from .fuenteclasificaciondlg import FuenteClasificacionDlg
from ..widgets.datalist import DataList
from ts import FKItemDelegate

class FuenteClasificacionList (DataList, Ui_FuenteClasificacionListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		app = QApplication.instance()
		if app.databaseInit:
			self.model = app.mFuenteClasificacion
			self.idFuenteClasificacion = -1
			self.tabla.setModel(self.model)
			self.tabla.hideColumn(self.model.fieldIndex("id"))
			self.tabla.setItemDelegateForColumn(self.model.fieldIndex("idfuente"), FKItemDelegate({}, self))
			self.tabla.setItemDelegateForColumn(self.model.fieldIndex("idclasificacion"), FKItemDelegate({}, self))
			self.tabla.selectionModel().selectionChanged.connect(self.tabla_selectionChanged)
			self.cambiaEncabezado(self.model, ['Fuente', 'Clasificación'])
			self.tabla.resizeColumnsToContents()

	@pyqtSlot(bool)
	def on_anade_clicked(self, checked):
		d = FuenteClasificacionDlg(self, self.model)
		if d.add():
			self.model.submitTrans()

	@pyqtSlot(bool)
	def on_elimina_clicked(self, checked):
		self.askAndRemoveRows(self.tabla, self.model)

	@pyqtSlot("const QModelIndex &")
	def on_tabla_doubleClicked(self, index):
		dm = FuenteClasificacionDlg(self, self.model)
		if dm.edit(index.row()):
			self.model.submitTrans()

	@pyqtSlot(bool)
	def on_edita_clicked(self, checked):
		l = self.tabla.selectedIndexes()
		l2 = self.model.selectedRows(l)
		if len(l2) == 1:
			self.on_tabla_doubleClicked(l[0])

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tabla_selectionChanged(self, before, after):
		l = self.tabla.selectionModel().selectedIndexes()
		p=self.model.pendingChanges()
		self.elimina.setEnabled(self.model.eraseActive(l) and not self.model.pendingChanges())
		self.idFuenteClasificacion = self.model.getId(l)
		self.edita.setEnabled(self.idFuenteClasificacion > 0 and not self.model.pendingChanges())
		self.anade.setEnabled(not self.model.pendingChanges())

	@pyqtSlot(bool)
	def on_guarda_clicked(self, checked):
		self.model.submitTrans()
		self.anade.setEnabled(True)

	@pyqtSlot(bool)
	def on_descarta_clicked(self, checked):
		self.model.revertAll()
		self.anade.setEnabled(True)

	@pyqtSlot(bool)
	def on_clipboardFuenteClasificacion_triggered(self, checked):
		self.getDataFromClipboard(checked, self.insertDataFuenteClasificacion)

	def tabla_contextualMenuActions(self):
		return [ self.clipboardFuenteClasificacion ]

	def insertDataFuenteClasificacion(self, data):
		fields = [ 'idfuente', 'idclasificacion' ]
		self.model.addRows(fields, data)

