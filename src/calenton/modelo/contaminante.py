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
# $Id: contaminante.py 191 2010-04-09 11:55:34Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/contaminante.py $
#
##############################################################################

from .pyseqtablemodel import PySeqTableModel
from PyQt6 import QtSql
from PyQt6.QtCore import Qt

class Contaminante (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db)
		self.setTable('contaminante')
		self.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
		self.setSort(self.fieldIndex('nombre'), Qt.SortOrder.AscendingOrder)
		self.setParentId(-1)
		self.select()

	def canErase(self, id):
		sql = "select count(*) from mapadatocontaminante where idcontaminante = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		sql = "select count(*) from equivcontaminante where idcontaminante = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		sql = "select count(*) from mapadatocontaminanteaforo where idcontaminante = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		sql = "select count(*) from mapaaforozona where idcontaminante = %d" % (id)
		n = int(self.first(sql).value(0) or 0)
		if n > 0:
			return False
		return True


