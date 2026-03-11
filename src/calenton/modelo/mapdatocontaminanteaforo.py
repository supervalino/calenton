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
# $Id: mapdatocontaminanteaforo.py 69 2010-01-20 13:10:20Z picazo $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/mapdatocontaminanteaforo.py $
#
##############################################################################

from ts import SeqTableModel
from PyQt6 import QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtSql import *

class MapDatoContaminanteAforo (SeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		SeqTableModel.__init__(self, parent, db)
		self.setTable('mapdatocontaminanteaforo')
		self.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
		self.setSort(self.fieldIndex('id'), Qt.SortOrder.AscendingOrder)
		self.app=parent

	def canErase(self, id):
		return True


