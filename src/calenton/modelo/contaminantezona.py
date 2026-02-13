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
# $Id: aforo.py 57 2010-01-18 11:42:53Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/aforo.py $
#
##############################################################################

from ts import SeqTableModel
from PyQt4 import QtSql
from PyQt4.QtCore import Qt
from PyQt4.QtSql import *

class ContaminanteZona (SeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		QSqlRelationalTableModel.__init__(self, parent, db)
		self.setTable('contaminantezona')
		self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.setSort(self.fieldIndex('nombre'), Qt.AscendingOrder)
		self.app=parent
		
	def canErase(self, id):
		return True
		
	
