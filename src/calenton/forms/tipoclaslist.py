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
# $Id: tipoclaslist.py 189 2010-04-09 09:21:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/tipoclaslist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from .ui.Ui_tipoclaslist import *
from .tipoclasdlg import TipoClasDlg
from ..widgets.datalist import DataList
class TipoclasList (DataList, Ui_TipoclasListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		app = QApplication.instance()
		if app.databaseInit:
			self.model = app.mTipoclas
			self.idTipoclas = -1
			self.tabla.setModel(self.model)
			self.tabla.hideColumn(self.model.fieldIndex("id"))
			self.tabla.selectionModel().selectionChanged.connect(self.tabla_selectionChanged)
			self.cambiaEncabezado(self.model, ['Nombre', 'Descripción'])
			self.tabla.resizeColumnsToContents()

	@pyqtSlot(bool)
	def on_anade_clicked(self, checked):
		d = TipoClasDlg(self, self.model)
		if d.add():
			self.model.submitTrans()

	@pyqtSlot(bool)
	def on_elimina_clicked(self, checked):
		self.askAndRemoveRows(self.tabla, self.model)

	@pyqtSlot(QModelIndex)
	def on_tabla_doubleClicked(self, index):
		dm = TipoClasDlg(self, self.model)
		if dm.edit(index.row()):
			self.model.submitTrans()

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
		self.idTipoclas = self.model.getId(l)
		self.edita.setEnabled(self.idTipoclas > 0)
