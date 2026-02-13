#!/usr/bin/python
#-*- coding: utf-8 -*-
##############################################################################
#
# CALENTON
# Programa de procesamiento y generación de informes para datos de emisión
# de contaminantes
#
# (C) LITEC, 2009
# (C) Trustserver SL, 2009
# Todos los derechos reservados
#
# $Id: parametroaforo.py 155 2010-03-29 15:10:33Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/parametroaforo.py $
#
##############################################################################

from pyseqtablemodel import PySeqTableModel
from PyQt4 import QtSql
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QStringList
from PyQt4.QtSql import *
from ts import ForeignKey

class ParametroAforo (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db, 'idaforo')
		self.setTable('parametroaforo')
		self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)
		self.app=parent
		self.db=db
		self.setForeignKey('idaforo', ForeignKey('aforo', 'nombre'))
		self.setForeignKey('idparametro', ForeignKey('parametro', 'nombre'))
		self.setParentId(-1)
		
	def canErase(self, id):
		return True
	
