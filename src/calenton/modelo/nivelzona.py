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
# $Id: nivelzona.py 176 2010-04-07 12:05:26Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/nivelzona.py $
#
##############################################################################

from ts import SeqTableModel
from PyQt6 import QtSql
from PyQt6.QtSql import *
from PyQt6.QtCore import Qt

class NivelZona (SeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		SeqTableModel.__init__(self,  parent, db)
		self.setTable('nivelzona')
		self.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
		self.setSort(self.fieldIndex('id'), Qt.SortOrder.AscendingOrder)

	def canErase(self, id):
		sql = "select count(*) from zona where idnivelzona = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		return True

	def lNivelesZona(self):
		mNivelesZona = []
		for i in range(0, self.rowCount()):
			record = self.record(i)
			mNivelesZona.append(str(record.value("nombre") or ''))
		print(mNivelesZona)
		return mNivelesZona


