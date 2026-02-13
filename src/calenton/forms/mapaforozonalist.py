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
# $Id: mapaforozonalist.py 198 2010-04-13 15:39:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/mapaforozonalist.py $
#
##############################################################################

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from ui.Ui_mapaforozonalist import *
from mapaforozonadlg import MapAforoZonaDlg
from widgets.datalist import DataList
from ts import FKItemDelegate

class MapAforoZonaList (DataList, Ui_MapAforoZonaListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		app = QApplication.instance()
		if app.databaseInit:
			self.model = app.mMapAforoZona
			self.idSel = -1
			self.model.select()
			self.tablaMap.setModel(self.model)
			self.tablaMap.hideColumn(self.model.fieldIndex("id"))
			self.tablaMap.setItemDelegateForColumn(self.model.fieldIndex("idaforo"), FKItemDelegate({}, self))
			self.tablaMap.setItemDelegateForColumn(self.model.fieldIndex("idzona"), FKItemDelegate({}, self))
			self.cambiaEncabezado(self.model, ['Aforo', 'Zona','Valor'])
			self.tablaMap.selectionModel().selectionChanged.connect(self.tablaMap_selectionChanged)
			self.tablaMap.resizeColumnsToContents()
			self.tablaMap.show()
		
	@pyqtSlot("bool")
	def on_anade_clicked(self, checked):
		d = MapAforoZonaDlg(self, self.model)
		if d.add():
			self.model.submitTrans()
		
	@pyqtSlot("bool")
	def on_elimina_clicked(self, checked):
		self.askAndRemoveRows(self.tablaMap, self.model)
		
	@pyqtSlot("bool")
	def on_guardar_clicked(self, checked):
		self.model.submitTrans()
		self.anade.setEnabled(True)
		
	@pyqtSlot("bool")
	def on_descartar_clicked(self, checked):
		self.model.revertAll()
		self.anade.setEnabled(True)
		
	@pyqtSlot("const QModelIndex &")
	def on_tablaMap_doubleClicked(self, index):
		dm = MapAforoZonaDlg(self, self.model)
		if dm.edit(index.row()):
			self.model.submitTrans()
		
	@pyqtSlot("bool")
	def on_edita_clicked(self, checked):
		l = self.tablaMap.selectedIndexes()
		l2 = self.model.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaMap_doubleClicked(l[0])
		
	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaMap_selectionChanged(self, after, before):
		l = self.tablaMap.selectionModel().selectedIndexes()
		p=self.model.pendingChanges()
		self.elimina.setEnabled(self.model.eraseActive(l) and not self.model.pendingChanges())
		self.idSel = self.model.getId(l)
		self.edita.setEnabled(self.idSel > 0 and not self.model.pendingChanges())
		self.anade.setEnabled(not self.model.pendingChanges())
		
	def tablaMap_contextualMenuAction(self):
		return [ self.insertFromClipboard, self.deleteAll, self.surfaceGeneration, 
				self.one2OneGeneration ]
	
	

