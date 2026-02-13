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
from PyQt4 import QtSql
from PyQt4.QtCore import Qt, QString, QVariant
from PyQt4.QtSql import *

class InsertError (Exception):
	def __init__(self, value):
		self.value = value
		
	def __str__(self):
		return str(self.value)
		
	def __unicode__(self):
		return unicode(self.value)
		
class PySeqTableModel (SeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase(), parentIdField = QString()):
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
			if filters[i].type() == QVariant.Invalid:
				filters[i] = r.value(i)
		
	def addRowByIndex(self, idx, fks, data, filters, order):
		r = self.record()
		for j in range(len(idx)):
			i = order[j]
			f = filters[i].copy()
			c = idx[i]
			self.updateFilters(f, r)
			v = unicode(QString(data[i]).simplified())
			if v == u'':
				r.setValue(c, QVariant(QString()))
				continue
			if fks[i] is not None and isinstance(fks[i], ForeignKey):
				v2 = fks[i].inverseMap(v, f)
				if v2 < 0:
					raise InsertError(u"No existe clave para " + v)
				v = v2
			vv = QVariant(v)
			vv.convert(r.field(c).type())
			r.setValue(c, vv)
		if not self.insertRecord(-1, r):
			raise InsertError("Error al insertar " + str(data))
			
	def setMultipleParents(self, filters):
		conds = []
		for (key, value) in filters.iteritems():
			if value is None:
				conds.append("%s is null" %(key))
			else:
				conds.append("%s = %d" % (key, value))
		cond = ' and '.join(conds)
		self.setFilter(cond)


