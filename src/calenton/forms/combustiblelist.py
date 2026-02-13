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
# $Id: combustiblelist.py 346 2010-10-29 06:43:46Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/combustiblelist.py $
#
##############################################################################

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from ui.Ui_combustiblelist import *
from ts import FKItemDelegate, ComboDataModel, TSqlTableNavigator
from widgets.clasitemdelegate import ClasItemDelegate

class ClasDelegate (TSqlTableNavigator.Delegate):
	def __init__(self, parent, lista):
		TSqlTableNavigator.Delegate.__init__(self, parent)
		self.lista = lista
		
	def couldAdd(self, nav):
		if self.lista.idEscenario > 0:
			return True
		else:
			return False
			
	def newRecord(self, nav):
		r = self.lista.mClasCombustible.record()
		r.setValue('idescenario', self.lista.idEscenario)
		return r
	
class CombustibleList (DataList, Ui_CombustibleListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		
		app = QApplication.instance()
		if not app.databaseInit:
			return
			
		self.app = app
		self.db = app.workDb()
		
		self.idEscenario = -1
		self.mEscenario = ComboDataModel(self)
		self.mEscenario.setQuery("select id, nombre from escenario order by id", self.db)
		self.escenario.setModel(self.mEscenario)

		self.mCombustible = app.mCombustible
		self.mClasCombustible = app.mClasCombustible
		
		self.navCombustible.setModel(app.mCombustible)
		self.navCombustible.tableView().hideColumn(self.mClasCombustible.fieldIndex('id'))
		self.navClasCombustible.setModel(app.mClasCombustible)
		self.navClasCombustible.setDelegate(ClasDelegate(self.navClasCombustible, self))
		self.navClasCombustible.tableView().hideColumn(
				self.mClasCombustible.fieldIndex('id'))
		self.navClasCombustible.tableView().setItemDelegateForColumn(
				self.mClasCombustible.fieldIndex('idescenario'),
				FKItemDelegate({}, self))
		self.navClasCombustible.tableView().setItemDelegateForColumn(
				self.mClasCombustible.fieldIndex("idcombustible"),
				FKItemDelegate({}, self))
		self.navClasCombustible.tableView().setItemDelegateForColumn(
				self.mClasCombustible.fieldIndex("idcontaminante"),
				FKItemDelegate({}, self))
		self.navClasCombustible.tableView().setItemDelegateForColumn(
				self.mClasCombustible.fieldIndex("idclasificacion"),
				FKItemDelegate({'idtipoclas': QVariant(4)}, self))
				
		self.cambiaClasCombustible()
		
	##########################################################################
	# Fuentes
	#
	
	@pyqtSlot("int")
	def on_escenario_activated(self, index):
		self.cambiaClasCombustible()
		
	def cambiaClasCombustible(self):
		self.idEscenario = -1
		ide = self.escenario.currentItemData()
		if ide.isValid and not ide.isNull():
			(i, g) = ide.toInt()
			if g:
				self.idEscenario = i
		self.navClasCombustible.setParentId(self.idEscenario)
		
	######################################################################
	# Contaminantes validados
	#
	
	@pyqtSlot("int", "QSqlRecord &")
	def navCombustible_primeInsert(self, row, record):
		record.setValue('idescenario', self.idEscenario)
		
	
	
