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
# $Id: valordato.py 183 2010-04-08 13:51:33Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/valordato.py $
#
##############################################################################

from pyseqtablemodel import PySeqTableModel
from PyQt4 import QtSql
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QStringList
from PyQt4.QtSql import *

class ValorDato (PySeqTableModel):
	def __init__(self, parent, db = QtSql.QSqlDatabase()):
		PySeqTableModel.__init__(self, parent, db, 'idaforo')
		self.setTable('valordato')
		self.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)
		self.app=parent
		self.db=db
		
	def canErase(self, id):
		return True
		
	def isValidPaste(self,mFuenteClasificacion,idFuente):
		if self.isDirty(self.index(0,0)):
			msj=QStringList()
			clasFuenteValida=[]
			clasDatoValida=[]
			mFuenteClasificacion.setFilter("idFuente=%d" % (idFuente))
			lFuenteClasificacion = []
			for i in range(0,mFuenteClasificacion.rowCount()):
				lFuenteClasificacion.append(mFuenteClasificacion.record(i).value("idclasificacion").toInt())
			for i in range(0,self.rowCount()):
				clasFuenteValida.insert(i,0)
				clasDatoValida.insert(i,0)
				rValorDato = self.record(i)
				if rValorDato.value("idclasificacion").toInt() in lFuenteClasificacion:
					clasFuenteValida[i]=1
					sql = """
						select d.id, d.idclasificacion
						from dato d
						where %d = d.id
							and %d in (
								select * 
								from jerarquia_clasificacion(d.idclasificacion)
								)
							and %d = d.idclasificacion
						""" % (rValorDato.value("iddato").toInt()[0], 
								rValorDato.value("idclasificacion").toInt()[0], 
								rValorDato.value("idclasificacion").toInt()[0])
					q = QSqlQuery(sql, self.db)
					while q.next():
						clasDatoValida[i]=1
			error = False
			for i in range(0,mFuenteClasificacion.rowCount()):
				if clasFuenteValida[i] == 0:
					msj.append(self.tr("La clasificación de la fuente %d no es válida" % (i+1)))
					error = True
				if clasDatoValida[i] == 0:
					msj.append(self.tr("La clasificación de la fuente %d no es válida" % (i+1)))
					error = True
			return (not error,msj)
	
