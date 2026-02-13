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

from pyseqtablemodel import PySeqTableModel
from PyQt4 import QtSql
from PyQt4.QtCore import Qt
from PyQt4.QtSql import *

class Aforo (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db, 'idfuente')
		self.setTable('aforo')
		self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.setSort(self.fieldIndex('nombre'), Qt.AscendingOrder)
		self.app=parent
		
	def canErase(self, id):
		sql = "select count(*) from mapdatocontaminanteaforo where idaforo = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from contaminanteaforo where idaforo = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from valordato where idaforo = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from mapaforozona where idaforo = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		return True
		
	def getIdEscenario(self, idfuente):
		sql = "select idescenario from fuente where id = %d" % (idfuente)
		r2 = self.first(sql)
		if r2.isEmpty():
			return -1
		(idescenario, good) = r2.value(0).toInt()
		if not good:
			return -1
		return idescenario
		
	def getIdNivelZona(self, idzona):
		sql = "select idnivelzona from zona where id = %d" % (idzona)
		r2 = self.first(sql)
		if r2.isEmpty():
			return -1
		(idnivelzona, good) = r2.value(0).toInt()
		if not good:
			return -1
		return idnivelzona

	
