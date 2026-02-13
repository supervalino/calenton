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
# $Id: dato.py 97 2010-02-09 18:38:37Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/dato.py $
#
##############################################################################

from pyseqtablemodel import PySeqTableModel
from PyQt4 import QtSql
from PyQt4.QtCore import Qt
from PyQt4.QtSql import *

class Dato (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db, 'idclasificacion')
		self.setTable('dato')
		self.idClasificacion = -1
		self.setParentId(self.idClasificacion)
		self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.setSort(self.fieldIndex('idclasificacion'), Qt.AscendingOrder)
		self.app=parent
		
	def canErase(self, id):
		sql = "select idclasificacion from dato where id = %d" % (id)
		(idclas, good) = self.first(sql).value(0).toInt()
		if idclas != self.idClasificacion:
			return False
		sql = "select count(*) from mapdatocontaminante where iddato = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from mapdatocontaminanteaforo where iddato = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from valordato where iddato = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		return True
		
	def getListAncestors(self, idClasificacion):
		sql = "select idpadre from clasificacion where id = :id"
		id = idClasificacion
		ids = []
		q = QSqlQuery(self.database())
		q.prepare(sql)
		while id is not None:
			ids.append(id)
			q.bindValue(':id', id)
			q.exec_()
			id = None
			if q.next():
				idv = q.value(0)
				if not idv.isNull():
					(id, good) = idv.toInt()
					if not good:
						id = None
		return ids
		
	def setParentId(self, parentId):
		l = self.getListAncestors(parentId)
		l2 = ','.join(map(str, l))
		filter = "idclasificacion in (%s)" % l2
		self.setFilter(filter)
		self.select()
		self.idClasificacion = parentId
	
