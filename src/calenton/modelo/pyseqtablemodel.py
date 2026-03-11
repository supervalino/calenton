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
# $Id: pyseqtablemodel.py 199 2010-04-13 15:56:54Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/pyseqtablemodel.py $
#
##############################################################################

from ts import SeqTableModel, ForeignKey
from PyQt6 import QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtSql import *

class InsertError (Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return str(self.value)

class PySeqTableModel (SeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase(), parentIdField = ''):
		SeqTableModel.__init__(self, parent, db, parentIdField)

	def addRows(self, fields, data, filters = None, fieldOrder = None):
		if fieldOrder is None:
			fieldOrder = fields
		if filters is None:
			filters = [ {} for i in fields ]
		order = [ fields.index(i) for i in fieldOrder ]
		r = self.record()
		idx = [ r.indexOf(i) for i in fields ]
		fks = [ self.foreignKey(idx[i]) for i in range(len(idx)) ]
		for i in data:
			self.addRowByIndex(idx, fks, i, filters, order)

	def addRow(self, fields, data, filters = {}, fieldOrder = None):
		if fieldOrder is None:
			fieldOrder = fields
		order = [ fields.index(i) for i in fieldOrder ]
		idx = [ self.fieldIndex(i) for i in fields ]
		fks = [ self.foreignKey(idx[i]) for i in range(len(idx)) ]
		self.addRowByIndex(idx, fks, data, filters, order)

	def updateFilters(self, filters, r):
		for i in filters.keys():
			if filters[i] is None:
				filters[i] = r.value(i)

	def addRowByIndex(self, idx, fks, data, filters, order):
		r = self.record()
		for j in range(len(idx)):
			i = order[j]
			f = filters[i].copy()
			c = idx[i]
			self.updateFilters(f, r)
			v = str(data[i]).strip() if data[i] is not None else ''
			if v == '':
				r.setValue(c, None)
				continue
			if fks[i] is not None and isinstance(fks[i], ForeignKey):
				v2 = fks[i].inverseMap(v, f)
				if v2 < 0:
					raise InsertError('No existe clave para ' + v)
				v = v2
			r.setValue(c, v)
		if not self.insertRecord(-1, r):
			raise InsertError("Error al insertar " + str(data))

	def setMultipleParents(self, filters):
		conds = []
		for (key, value) in filters.items():
			if value is None:
				conds.append("%s is null" % (key))
			else:
				conds.append("%s = %d" % (key, value))
		cond = ' and '.join(conds)
		self.setFilter(cond)


