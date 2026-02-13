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
# $Id: temporal.py 351 2010-11-15 17:47:19Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/calculo/temporal.py $
#
##############################################################################

from PyQt4.QtSql import *
from PyQt4.QtCore import *

class TablaTemporal:
	def __init__(self, db):
		self.backend = -1
		self.db = db
		self.numTemps = 0
		self.tablas = []
		
	def getBackend(self):
		if self.backend > 0:
			return self.backend
		sql = "select pg_backend_pid()"
		q = QSqlQuery(sql, self.db)
		if not q.isActive() or not q.next():
			self.backend = -1
			return -1
		self.backend = q.value(0).toInt()[0]
		return self.backend
		
	def tabla(self):
		b = self.getBackend()
		self.numTemps = self.numTemps + 1
		tabla = "temp.ctt_%d_%d" % (b, self.numTemps)
		sql = "drop table if exists %s" % (tabla)
		self.db.exec_(sql)
		self.tablas.append(tabla)
		return tabla
		
	def tablaMapa(self, sql):
		t = self.tabla()
		sql = "create table %s as %s" % (t, sql)
		print sql
		self.db.exec_(sql)
		return t
		
	def quitaTabla(self, tabla):
		if tabla in self.tablas:
			sql = "drop table if exists %s"
			self.db.exec_(sql)
			self.tablas.remove(tabla)
		
	def quitaTodas(self):
		for i in self.tablas:
			sql = "drop table if exists %s"
			self.db.exec_(sql)
		self.tablas = []
	
