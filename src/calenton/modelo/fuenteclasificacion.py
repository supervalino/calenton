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
# $Id: fuenteclasificacion.py 101 2010-02-12 16:52:01Z picazo $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/fuenteclasificacion.py $
#
##############################################################################

from pyseqtablemodel import PySeqTableModel
from PyQt4 import QtSql
from PyQt4.QtCore import Qt

class FuenteClasificacion (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db)
		self.setTable('fuenteclasificacion')
		self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)
		self.app=parent
		
	def canErase(self, id):
		return True

	
