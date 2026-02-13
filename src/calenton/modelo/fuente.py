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
# $Id: fuente.py 156 2010-03-29 16:12:56Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/fuente.py $
#
##############################################################################

from ts import SeqTableModel
from PyQt4 import QtSql
from PyQt4.QtCore import Qt
from ts import ForeignKey
from pyseqtablemodel import PySeqTableModel

class Fuente (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db, 'idescenario')
		self.setTable('fuente')
		self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.setSort(self.fieldIndex('nombre'), Qt.AscendingOrder)
		self.app=parent
		self.setForeignKey('idescenario', ForeignKey('escenario', 'nombre'))
		self.setForeignKey('idorigen', ForeignKey('origen', 'nombre'))
		self.setForeignKey('idmotorcalculo', ForeignKey('motorcalculo', 'nombre'))
		self.setForeignKey('idnivelzona', ForeignKey('nivelzona', 'nombre'))
		self.setForeignKey('idtipodatozona', ForeignKey('tipodatozona', 'nombre'))
		self.setParentId(-1)
		
	def canErase(self, id):
		sql = "select count(*) from fuenteclasificacion where idfuente = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		return True
			
	
