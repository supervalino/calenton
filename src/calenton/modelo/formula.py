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
# $Id: formula.py 118 2010-03-01 17:00:05Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/formula.py $
#
##############################################################################

from PyQt4 import QtSql
from PyQt4.QtCore import Qt, QVariant
from PyQt4.QtSql import *
from ts import RelOne2One

class FormulaOne2One (RelOne2One):
	def __init__(self):
		RelOne2One.__init__(self, "idformula", "formula")
		self.addColumnData("idescenario", "formula_idescenario", False)
		self.addColumn("expresion", "formula_expresion")
		self.nIdEscenario = self.internalColumn("idescenario")
		
	def primeInsert(self, row, r):
		RelOne2One.primeInsert(self, row, r)
		self.setCacheValue(row, self.nIdEscenario, QVariant(self.table().getIdEscenario(r)))
		
	def beforeInsert(self, r):
		(row, good) = r.value(self.idColumnName()).toInt()
		if good and (row < 0):
			row = self.decodeRowFromId(row)
			self.setCacheValue(row, self.nIdEscenario, QVariant(self.table().getIdEscenario(r)))
		RelOne2One.beforeInsert(self, r)
		
	def afterUpdate(self, row, r):
		self.setCacheValue(row, self.nIdEscenario, QVariant(self.table().getIdEscenario(r)))
		RelOne2One.afterUpdate(self, row, r)
		
	def reloadMetadata(self):
		RelOne2One.reloadMetadata(self)
		self.nIdEscenario = self.internalColumn('idescenario')
