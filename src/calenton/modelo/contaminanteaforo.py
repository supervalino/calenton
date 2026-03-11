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

from .pyseqtablemodel import PySeqTableModel
from PyQt6 import QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtSql import *
from ts import ForeignKey

class ContaminanteAforo (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db, "idaforo")
		self.setTable('contaminanteaforo')
		self.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
		self.setSort(self.fieldIndex('id'), Qt.SortOrder.AscendingOrder)
		self.setForeignKey('idaforo', ForeignKey('aforo', 'nombre'))
		self.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.setForeignKey('idcontaminante', ForeignKey('contaminante', 'nombre'))

		self.setParentId(-1)
		self.app=parent

	def canErase(self, id):
		return False


