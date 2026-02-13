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
# $Id: equivcontaminante.py 266 2010-05-24 09:31:24Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/equivcontaminante.py $
#
##############################################################################

from ts import SeqTableModel, ForeignKey
from PyQt4 import QtSql
from PyQt4.QtCore import Qt

class EquivContaminante (SeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		SeqTableModel.__init__(self, parent, db)
		self.setTable('equivcontaminante')
		self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)
		self.app=parent
		self.setForeignKey('idescenario', ForeignKey('escenario', 'nombre'))
		self.setForeignKey('idcontaminante', ForeignKey('contaminante', 'nombre'))
		self.select()
		
	def canErase(self, id):
		return True
		
	
	
