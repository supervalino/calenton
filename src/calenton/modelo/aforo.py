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
# $Id: aforo.py 198 2010-04-13 15:39:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/aforo.py $
#
##############################################################################

from ts import SeqTableModel
from PyQt6 import QtSql
from PyQt6.QtCore import Qt
from PyQt6.QtSql import *

class Aforo (SeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		SeqTableModel.__init__(self, parent, db, 'idfuente')
		self.setTable('aforo')
		self.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
		self.setSort(self.fieldIndex('nombre'), Qt.SortOrder.AscendingOrder)
		self.app=parent

	def canErase(self, id):
		sql = "select count(*) from mapdatocontaminanteaforo where idaforo = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		sql = "select count(*) from contaminanteaforo where idaforo = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		sql = "select count(*) from valordato where idaforo = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		sql = "select count(*) from mapaforozona where idaforo = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		return True

	def getIdEscenario(self, idfuente):
		sql = "select idescenario from fuente where id = %d" % (idfuente)
		r2 = self.first(sql)
		if r2.isEmpty():
			return -1
		idescenario = r2.value(0)
		if idescenario is None:
			return -1
		return int(idescenario)

	def getIdNivelZona(self, idzona):
		sql = "select idnivelzona from zona where id = %d" % (idzona)
		r2 = self.first(sql)
		if r2.isEmpty():
			return -1
		idnivelzona = r2.value(0)
		if idnivelzona is None:
			return -1
		return int(idnivelzona)


