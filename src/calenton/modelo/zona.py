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

from ts import SeqTableModel
from PyQt6 import QtSql
from PyQt6.QtSql import *
from PyQt6.QtCore import Qt

class Zona (SeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		SeqTableModel.__init__(self, parent, db, 'idnivelzona')
		self.setTable('zona')
		self.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
		self.setSort(self.fieldIndex('nombre'), Qt.SortOrder.AscendingOrder)

	def canErase(self, id):
		sql = "select count(*) from relzona where idzona = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		sql = "select count(*) from relzona where idzonapadre = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		sql = "select count(*) from mapaforozona where idzona = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		return True

	def lZonas(self):
		mListaZonas = []
		for i in range(0, self.rowCount()):
			record = self.record(i)
			mListaZonas.append(str(record.value("nombre") or ''))
		return mListaZonas

	def lPadres(self, id):
		src = """select zona.nombre
					from zona,relzona
					where zona.id=relzona.idzonapadre and
					relzona.idzona= %d
				""" % (id)
		q = QSqlQuery(src, self.database())
		mListaZonas = []
		while q.next():
			mListaZonas.append(str(q.value("nombre") or ''))
		return mListaZonas
