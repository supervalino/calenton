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
# $Id: zona.py 150 2010-03-26 01:20:19Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/zona.py $
#
##############################################################################

from pyseqtablemodel import PySeqTableModel
from PyQt4 import QtSql
from PyQt4.QtSql import *
from PyQt4.QtCore import Qt

class Zona (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db, 'idnivelzona')
		self.setTable('zona')
		self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.setSort(self.fieldIndex('nombre'), Qt.AscendingOrder)
		
	def canErase(self, id):
		sql = "select count(*) from relzona where idzona = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from relzona where idzonapadre = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from mapaforozona where idzona = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		return True

	def lZonas(self):
		mListaZonas = []
		for i in range(0,self.rowCount()):
			record = self.record(i)
			mListaZonas.append(record.value("nombre").toString())
		return mListaZonas

	def lPadres(self,id):
		src = """select zona.nombre 
					from zona,relzona 
					where zona.id=relzona.idzonapadre and 
					relzona.idzona= %d
				""" % (id)
		q = QSqlQuery(src, self.database())
		mListaZonas = []
		while q.next():
			mListaZonas.append(q.value("nombre").toString())
		return mListaZonas
