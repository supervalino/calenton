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
# $Id: parametrozona.py 155 2010-03-29 15:10:33Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/parametrozona.py $
#
##############################################################################

from .pyseqtablemodel import PySeqTableModel, ForeignKey
from PyQt6 import QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtSql import *

class ParametroZona (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db, 'idzona')
		self.setTable('parametrozona')
		self.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
		self.setSort(self.fieldIndex('id'), Qt.SortOrder.AscendingOrder)
		self.app=parent
		self.db=db
		self.setForeignKey('idzona', ForeignKey('zona', 'nombre'))
		self.setForeignKey('idparametro', ForeignKey('parametro', 'nombre'))
		self.setParentId(-1)

	def canErase(self, id):
		return True

