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
from PyQt4 import QtSql
from PyQt4.QtCore import Qt
from PyQt4.QtSql import *
from ts import ForeignKey

class ContaminanteAforo (SeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		QSqlRelationalTableModel.__init__(self, parent, db, "idaforo")
		self.setTable('contaminanteaforo')
		self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)
		self.setForeignKey('idaforo', ForeignKey('aforo', 'nombre'))
		self.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.setForeignKey('idcontaminante', ForeignKey('contaminante', 'nombre'))
		
		self.setParentId(-1)
		self.app=parent
		
	def canErase(self, id):
		return False
		
	
