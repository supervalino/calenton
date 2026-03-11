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
# $Id: equivcontaminantelist.py 266 2010-05-24 09:31:24Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/equivcontaminantelist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_equivcontaminantelist import *
from .equivcontaminantedlg import EquivContaminanteDlg
from ..widgets.datalist import DataList
class EquivContaminanteList (DataList, Ui_EquivContaminanteListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		self.model = None
		app = QApplication.instance()
		if app.databaseInit:
			self.model = app.mEquivContaminante
			self.idFuente = -1
			self.tabla.setModel(self.model)
			self.tabla.hideColumn(self.model.fieldIndex("id"))
			self.tabla.selectionModel().selectionChanged.connect(self.tabla_selectionChanged)
			self.cambiaEncabezado(self.model, ['Escenario', 'Contaminante', 'Equivalente CO2'])
			self.tabla.resizeColumnsToContents()
			self.tabla.resizeRowsToContents()

	@pyqtSlot(bool)
	def on_anade_clicked(self, checked):
		d = EquivContaminanteDlg(self, self.model)
		if d.add():
			self.model.submitTrans()

	@pyqtSlot(bool)
	def on_elimina_clicked(self, checked):
		self.askAndRemoveRows(self.tabla, self.model)

	@pyqtSlot("const QModelIndex &")
	def on_tabla_doubleClicked(self, index):
		dm = EquivContaminanteDlg(self, self.model)
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
		self.elimina.setEnabled(self.model.eraseActive(l))
		self.idEquivContaminante = self.model.getId(l)
		self.edita.setEnabled(self.idEquivContaminante > 0)


