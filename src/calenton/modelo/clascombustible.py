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
# $Id: clascombustible.py 346 2010-10-29 06:43:46Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/clascombustible.py $
#
##############################################################################

from .pyseqtablemodel import PySeqTableModel, ForeignKey
from PyQt6 import QtSql
from PyQt6.QtCore import Qt

class ClasCombustible (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db, "idescenario")
		self.setTable('clascombustible')
		self.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
		self.setForeignKey('idescenario', ForeignKey('escenario', 'nombre'))
		self.setForeignKey('idcombustible', ForeignKey('combustible', 'nombre'))
		self.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.setForeignKey('idcontaminante', ForeignKey('contaminante', 'nombre'))
		self.setSort(self.fieldIndex('nombre'), Qt.SortOrder.AscendingOrder)
		self.setParentId(-1)
		self.select()

	def canErase(self, id):
		return True


