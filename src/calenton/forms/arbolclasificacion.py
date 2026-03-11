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
# $Id: arbolclasificacion.py 189 2010-04-09 09:21:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/arbolclasificacion.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_arbolclasificacion import *
from .tipoclasdlg import TipoClasDlg
from .datodlg import DatoDlg
from ..widgets.datalist import DataList
from ..modelo import arbolclasificacion, dato
class ArbolClasificacion (DataList, Ui_ArbolClasificacionClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		app = QApplication.instance()
		if not app.databaseInit:
			return
		self.db = app.workDb()

		self.mTipoClas = app.mTipoclas
		self.tablaTipos.setModel(self.mTipoClas)
		self.tablaTipos.hideColumn(self.mTipoClas.fieldIndex("id"))
		self.cambiaEncabezado(self.mTipoClas, ['Nombre', 'Descripción'])
		self.tablaTipos.selectionModel().selectionChanged.connect(self.tablaTipos_selectionChanged)
		self.idTipoClas = -1
		self.editaTipos.setEnabled(False)
		self.eliminaTipos.setEnabled(False)

		self.mClasificacion = arbolclasificacion.ArbolClasificacion(self.idTipoClas, self.db, self)
		self.arbolClasificacion.setModel(self.mClasificacion)
		self.arbolClasificacion.selectionModel().selectionChanged.connect(self.arbolClasificacion_selectionChanged)
		self.idClasificacion = -1

		self.mDato = app.mDato
		self.idDato = -1
		self.tablaDato.setModel(self.mDato)
		self.tablaDato.hideColumn(self.mDato.fieldIndex("id"))
		self.cambiaEncabezado(self.mDato, ['Clasificación', 'Nombre', 'Descripción', 'Unidades'])
		self.tablaDato.selectionModel().selectionChanged.connect(self.tablaDato_selectionChanged)
		self.tablaDato.resizeColumnsToContents()

	@pyqtSlot(bool)
	def on_anadeTipos_clicked(self, checked):
		d = TipoClasDlg(self, self.mTipoClas)
		if d.add():
			self.mTipoClas.submitTrans()

	@pyqtSlot(bool)
	def on_eliminaTipos_clicked(self, checked):
		self.askAndRemoveRows(self.tablaTipos, self.mTipoClas)

	@pyqtSlot("const QModelIndex &")
	def on_tablaTipos_doubleClicked(self, index):
		dm = TipoClasDlg(self, self.mTipoClas)
		if dm.edit(index.row()):
			self.mTipoClas.submitTrans()

	@pyqtSlot(bool)
	def on_editaTipos_clicked(self, checked):
		l = self.tablaTipos.selectedIndexes()
		l2 = self.mTipoClas.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaTipos_doubleClicked(l[0])

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaTipos_selectionChanged(self, before, after):
		l = self.tablaTipos.selectionModel().selectedIndexes()
		self.idTipoClas = self.mTipoClas.getId(l)
		self.mClasificacion.setIdTipo(self.idTipoClas)
		self.arbolClasificacion_selectionChanged(QItemSelection(), QItemSelection())
		self.eliminaTipos.setEnabled(self.mTipoClas.eraseActive(l))
		self.editaTipos.setEnabled(self.idTipoClas > 0)


	@pyqtSlot(bool)
	def on_anadeDato_clicked(self, checked):
		d = DatoDlg(self, self.mDato)
		if d.add():
			self.mDato.submitTrans()

	@pyqtSlot(bool)
	def on_eliminaDato_clicked(self, checked):
		self.askAndRemoveRows(self.tablaDato, self.mDato)

	@pyqtSlot("const QModelIndex &")
	def on_tablaDato_doubleClicked(self, index):
		dm = DatoDlg(self, self.mDato)
		if dm.edit(index.row()):
			self.mDato.submitTrans()

	@pyqtSlot(bool)
	def on_editaDato_clicked(self, checked):
		l = self.tablaDato.selectedIndexes()
		l2 = self.mDato.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaDato_doubleClicked(l[0])

	@pyqtSlot(bool)
	def on_guardaDato_clicked(self, checked):
		self.mDato.submitTrans()
		self.anadeDato.setEnabled(True)

	@pyqtSlot(bool)
	def on_descartaDato_clicked(self, checked):
		self.mDato.revertAll()
		self.anadeDato.setEnabled(True)

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaDato_selectionChanged(self, before, after):
		l = self.tablaDato.selectionModel().selectedIndexes()
#		self.eliminaDato.setEnabled(self.mDato.eraseActive(l))
#		self.idDato = self.mDato.getId(l)
#		self.editaDato.setEnabled(self.idDato > 0)

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def arbolClasificacion_selectionChanged(self, before, after):
		l = self.arbolClasificacion.selectionModel().selectedIndexes()
		self.idClasificacion = self.mClasificacion.getId(l)
		self.mDato.setParentId(self.idClasificacion)
		self.tablaDato_selectionChanged(QItemSelection(), QItemSelection())

	def insertDataDato(self, data):
		fields = [ 'idclasificacion','nombre', 'descripcion',  'unidades' ]
		self.mDato.addRows(fields, data)

	@pyqtSlot(bool)
	def on_clipboardDato_triggered(self, checked):
		self.getDataFromClipboard(checked, self.insertDataDato)

	def tablaDato_contextualMenuActions(self):
		return [ self.clipboardDato ]


