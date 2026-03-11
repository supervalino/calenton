#!/usr/bin/python
#-*- coding: utf-8 -*-
##############################################################################
#
# CALENTON
# Programa de procesamiento y generación de informes para datos de emisión
# de contaminantes
#
# (C) LITEC, 2009
# (C) Trustserver SL, 2009
# Todos los derechos reservados
#
# $Id: contaminanteaforolist.py 198 2010-04-13 15:39:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/contaminanteaforolist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_contaminanteaforolist import *
from .contaminanteaforodlg import ContaminanteAforoDlg
from ..widgets.datalist import DataList
from ts import FKItemDelegate

class ContaminanteAforoList (DataList, Ui_ContaminanteAforoListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		self.model = None
		app = QApplication.instance()
		if app.databaseInit:
			self.model = app.mContaminanteAforo
			self.idSel = -1
			self.model.setParentId(-1)
			self.tabla.setModel(self.model)
			self.tabla.hideColumn(self.model.fieldIndex("id"))
			self.tabla.setItemDelegateForColumn(self.model.fieldIndex("idaforo"), FKItemDelegate({}, self))
			self.tabla.setItemDelegateForColumn(self.model.fieldIndex("idcontaminante"), FKItemDelegate({}, self))
			self.tabla.setItemDelegateForColumn(self.model.fieldIndex("idclasificacion"), FKItemDelegate({}, self))
			self.cambiaEncabezado(self.model, ['Contaminante','Aforo', 'Clasificación','Valor'])
			self.tabla.selectionModel().selectionChanged.connect(self.tabla_selectionChanged)
			self.tabla.resizeColumnsToContents()
			self.tabla.show()

	@pyqtSlot(bool)
	def on_anade_clicked(self, checked):
		d = ContaminanteAforoDlg(self, self.model)
		if d.add():
			self.model.submitTrans()

	@pyqtSlot(bool)
	def on_elimina_clicked(self, checked):
		self.askAndRemoveRows(self.tabla, self.model)

	@pyqtSlot(bool)
	def on_guardar_clicked(self, checked):
		self.model.submitTrans()
		self.anade.setEnabled(True)

	@pyqtSlot(bool)
	def on_descartar_clicked(self, checked):
		self.model.revertAll()
		self.anade.setEnabled(True)

	@pyqtSlot("const QModelIndex &")
	def on_tabla_doubleClicked(self, index):
		dm = ContaminanteAforoDlg(self, self.model)
		if dm.edit(index.row()):
			self.model.submitTrans()

	@pyqtSlot(bool)
	def on_edita_clicked(self, checked):
		l = self.tabla.selectedIndexes()
		l2 = self.model.selectedRows(l)
		if len(l2) == 1:
			self.on_tabla_doubleClicked(l[0])

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tabla_selectionChanged(self, after, before):
		l = self.tabla.selectionModel().selectedIndexes()
		p=self.model.pendingChanges()
		self.elimina.setEnabled(self.model.eraseActive(l) and not self.model.pendingChanges())
		self.idSel = self.model.getId(l)
		self.edita.setEnabled(self.idSel > 0 and not self.model.pendingChanges())
		self.anade.setEnabled(not self.model.pendingChanges())


