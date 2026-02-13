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
# $Id: listaresultadodlg.py 238 2010-04-30 15:11:43Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/listaresultadodlg.py $
#
##############################################################################

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from ui.Ui_listaresultadodlg import *
from ts import ComboDataModel
from widgets.datalist import DataListBase

class ListaResultadoDlg (QDialog, DataListBase, Ui_ListaResultadoDlgClass):
	def __init__(self,  query,  db,  parent = None):
		QDialog.__init__(self,  parent)
		self.setupUi(self)
		self.addAction(self.actionCopiar)
		QApplication.instance().setOverrideCursor(Qt.WaitCursor)		
		self.db = db
		self.query = query
		self.model = QSqlQueryModel(self)
		self.model.setQuery(query,  db)
		self.tabla.setModel(self.model)
		self.tabla.resizeColumnsToContents()
		self.tabla.resizeRowsToContents()
		QApplication.instance().restoreOverrideCursor()
	
