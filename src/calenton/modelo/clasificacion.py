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
# $Id: clasificacion.py 59 2010-01-18 17:28:55Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/clasificacion.py $
#
##############################################################################

from pyseqtablemodel import PySeqTableModel
from PyQt4 import QtSql
from PyQt4.QtCore import Qt

class Clasificacion (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db)
		self.setTable('clasificacion')
		self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.setSort(self.fieldIndex('codigo'), Qt.AscendingOrder)
		self.app=parent
		
	def canErase(self, id):
		sql = "select count(*) from mapadatocontaminante where idclasificacion = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from mapacontaminanteaforo where idclasificacion = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from contaminanteaforo where idclasificacion = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from valordato where idclasificacion = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from dato where idclasificacion = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		sql = "select count(*) from fuenteclasificacion where idclasificacion = %d" % (id)
		(n, good) = self.first(sql).value(0).toInt()
		if n > 0:
			return False
		return True
		
	
