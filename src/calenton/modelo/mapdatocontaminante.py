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
# $Id: mapdatocontaminante.py 226 2010-04-28 12:02:28Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/mapdatocontaminante.py $
#
##############################################################################

from .pyseqtablemodel import PySeqTableModel
from PyQt6 import QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtSql import *
from .formula import FormulaOne2One
from ts import ForeignKey
from .fkdato import FKDato

class MapDatoContaminante (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase(), sinDato = False):
		PySeqTableModel.__init__(self, parent, db)
		self.setTable('mapdatocontaminante')
		self.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
		self.setSort(self.fieldIndex('id'), Qt.SortOrder.AscendingOrder)
		self.formula = FormulaOne2One()
		self.sinDato = sinDato
		self.addRowControl(self.formula)
		self.setForeignKey('idescenario', ForeignKey('escenario', 'nombre'))
		self.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.setForeignKey('iddato', FKDato('dato', 'nombre'))
		self.setForeignKey('idcontaminante', ForeignKey('contaminante', 'nombre'))
		self.setFilter("1=2")
		self.select()

	def getIdEscenario(self, r):
		idescenario = r.value("idescenario")
		if idescenario is None:
			return -1
		try:
			idescenario = int(idescenario)
		except (ValueError, TypeError):
			return -1
		if idescenario <= 0:
			idescenario = -1
		return idescenario

	def canErase(self, id):
		return True

	def setMultipleParents(self, filters):
		if self.sinDato:
			filters['iddato'] = None
		PySeqTableModel.setMultipleParents(self, filters)

