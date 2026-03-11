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
# $Id: cache.py 205 2010-04-19 09:44:21Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/calculo/cache.py $
#
##############################################################################

from PyQt6 import QtSql
from PyQt6 import QtCore
from PyQt6.QtSql import *

class CacheParametros:
	def __init__(self, db, idEscenario = -1):
		self.db = db
		self.idEscenario = idEscenario
		self.l = {}
		self.lc = {}
		self.aforosWithParams = None
		self.g = None

	def clean(self):
		self.l = {}
		self.lc = {}
		self.aforosWithParams = None
		self.g = None

	def setIdEscenario(self, idEscenario):
		self.idEscenario = idEscenario
		self.clean()

	def getParamSet(self, sql):
		q = QSqlQuery(sql, self.db)
		if q.lastError().isValid():
			print(str(q.lastError().text()))
			return None
		r = {}
		while q.next():
			n = str(q.value(0) or "")
			v_raw = q.value(1)
			if v_raw is not None and n:
				try:
					v = float(v_raw)
					r[n] = v
				except (ValueError, TypeError):
					pass
		q.clear()
		return r

	def getGlobalsFromDb(self):
		sql = """select nombre, valor
			from parametro
			where idescenario = %d
			""" % (self.idEscenario)
		self.g = self.getParamSet(sql)

	def getLocalsFromDb(self, idZona):
		sql = """select p.nombre, pz.valor
			from parametro p, parametrozona pz
			where p.id = pz.idparametro and
				pz.idzona = %d and
				p.idescenario = %d
			""" % (idZona, self.idEscenario)
		r = self.getParamSet(sql)
		self.l[idZona] = r

	def globals(self):
		if self.g is None:
			self.getGlobalsFromDb()
		return self.g

	def localsSimple(self, idZona):
		if idZona is None:
			return {}
		if idZona not in self.l:
			self.getLocalsFromDb(idZona)
		return self.l[idZona]

	def getZonaHierarchy(self, idZona):
		sql = """select idzonapadre
			from relzona
			where idzona = :idzona
			"""
		id = idZona
		q = QSqlQuery(self.db)
		if not q.prepare(sql):
			return None
		res = [ idZona ]
		pending = [ idZona ]
		while len(pending) > 0:
			id = pending.pop(0)
			q.bindValue(":idzona", id)
			if not q.exec():
				return None
			while q.next():
				idpadre_raw = q.value(0)
				if idpadre_raw is None:
					return None
				try:
					idpadre = int(idpadre_raw)
				except (ValueError, TypeError):
					return None
				if idpadre not in res:
					if idpadre not in pending:
						pending.append(idpadre)
					res.append(idpadre)
		q.clear()
		if len(res) == 0:
			return []
		a = [ str(i) for i in res ]
		sql = "select id from zona where id in (%s) order by idnivelzona desc" % (','.join(a))
		q = QSqlQuery(sql, self.db)
		if not q.isActive():
			return None
		res = []
		while q.next():
			id_raw = q.value(0)
			if id_raw is None:
				return None
			try:
				id = int(id_raw)
			except (ValueError, TypeError):
				return None
			res.append(id)
		q.clear()
		return res

	def mergeParams(self, globals, locals):
		res = globals.copy()
		for i in locals.keys():
			res[i] = locals[i]
		return res

	def getLocalsCompositeFromDb(self, idZona):
		hier = self.getZonaHierarchy(idZona)
		if hier is None:
			return
		lc = self.globals().copy()
		for i in hier:
			lc = self.mergeParams(lc, self.localsSimple(i))
		self.lc[idZona] = lc

	def locals(self, idZona):
		if idZona is None:
			return {}
		if idZona not in self.lc:
			self.getLocalsCompositeFromDb(idZona)
		return self.lc[idZona]

	def getAforosWithParams(self):
		sql = """select pa.idaforo
			from parametroaforo pa, aforo a, fuente f
			where pa.idaforo = a.id and
				a.idfuente = f.id and
				f.idescenario = %d
			""" % (self.idEscenario)
		q = QSqlQuery(sql, self.db)
		if q.lastError().isValid():
			print(str(q.lastError().text()))
			return None
		r = set()
		while q.next():
			id = int(q.value(0) or 0)
			r.add(id)
		self.aforosWithParams = r
		q.clear()

	def paramsAforo(self, idAforo):
		if self.aforosWithParams is None:
			self.getAforosWithParams()
		if idAforo not in self.aforosWithParams:
			return {}
		sql = """select p.nombre, pa.valor
			from parametro p, parametroaforo pa
			where p.id = pa.idparametro and
				pa.idaforo = %d
			""" % (idAforo)
		return self.getParamSet(sql)

	def zonaAforo(self, idAforo):
		sql = "select idzona from aforo where id = %d" % (idAforo)
		q = QSqlQuery(sql, self.db)
		if q.lastError().isValid():
			print(str(q.lastError().text()))
			return None
		if not q.next():
			return None
		idZona_raw = q.value(0)
		if idZona_raw is None:
			return None
		try:
			idZona = int(idZona_raw)
		except (ValueError, TypeError):
			return None
		q.clear()
		return idZona

	def params(self, idAforo):
		idZona = self.zonaAforo(idAforo)
		l = self.locals(idZona)
		p = self.paramsAforo(idAforo)
		return self.mergeParams(l, p)
