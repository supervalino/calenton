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
# $Id: escenario.py 22 2009-11-12 10:55:05Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/escenario.py $
#
##############################################################################

from ts import SeqTableModel
from PyQt6 import QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtSql import *

class MapAforoZona (SeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		SeqTableModel.__init__(self, parent, db)
		self.setTable('mapaforozona')
		self.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
		self.setSort(self.fieldIndex('id'), Qt.SortOrder.AscendingOrder)
		self.app=parent

	def canErase(self, id):
		return True


