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
# $Id: calcula.py 348 2010-11-02 12:53:05Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/calculo/calcula.py $
#
##############################################################################

from PyQt6.QtSql import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from .cache import *
from ..js import motor, bonito
import gc, tempfile, os, sys
import shutil

class CalcException (Exception):
	def __init__(self, aforo, value):
		self.value = value
		if aforo is not None:
			self.value = self.value + ("\nAl calcular aforo '%s'" % (aforo.nombre)) + \
				("\nen fuente '%s'" % (aforo.nombreFuente))

	def __str__(self):
		return str(self.value)

class Dato:
	def __init__(self, idDato, nombre, idClasificacion, valor = 0.0):
		self.idDato = idDato
		self.nombre = nombre
		self.idClasificacion = idClasificacion
		self.valor = valor

	def setValor(self, valor):
		self.valor = valor

	@staticmethod
	def toDict(datos):
		res = {}
		for i in datos:
			res[i.nombre] = i.valor
		return res

	@staticmethod
	def fromIdDato(idDato, db):
		sql = "select nombre, idclasificacion from dato where id = %d" % (idDato)
		q = QSqlQuery(sql, db)
		if not q.isActive() or not q.next():
			raise CalcException(None, "Error al consultar el dato %d" % (idDato))
		nombre = str(q.value(0) or "")
		idclas = int(q.value(1) or 0)
		return Dato(idDato, nombre, idclas)

class Contaminante:
	def __init__(self, idContaminante, nombre):
		self.idContaminante = idContaminante
		self.nombre = nombre

	@staticmethod
	def fromIdContaminante(idContaminante, db):
		sql = "select nombre from contaminante where id = %d" % (idContaminante)
		q = QSqlQuery(sql, db)
		if not q.isActive() or not q.next():
			raise CalcException(None, "Error al consultar el contaminante %d" % (idContaminante))
		nombre = str(q.value(0) or "")
		return Contaminante(idContaminante, nombre)

class Clasificacion:
	def __init__(self, idClasificacion, codigo):
		self.idClasificacion = idClasificacion
		self.codigo = codigo

	@staticmethod
	def fromIdClasificacion(idClasificacion, db):
		sql = "select codigo from clasificacion where id = %d" % (idClasificacion)
		q = QSqlQuery(sql, db)
		if not q.isActive() or not q.next():
			raise CalcException(None, "Error al consultar la clasificacion %d" % (idClasificacion))
		codigo = str(q.value(0) or "")
		return Clasificacion(idClasificacion, codigo)


class Aforo:
	def __init__(self, db, cache, idAforo):
		self.db = db
		self.cache = cache
		self.idAforo = idAforo
		self.escala = None
		self.consigueDatosPropios()
		self.cacheParams = None
		self.cacheValores = {}
		self.cacheDatos = {}
		self.cacheClasificaciones = None

	def params(self):
		if self.cacheParams is None:
			self.cacheParams = self.cache.params(self.idAforo)
		return self.cacheParams

	def consigueDatosBD(self, idClasificacion):
		QApplication.processEvents()
		sql = """select d.id, d.nombre, d.idclasificacion, vd.valor
			from dato d left outer join valordato vd
				on (vd.iddato = d.id and vd.idaforo = %d)
			where d.idclasificacion in (select * from jerarquia_clasificacion(%d))
			""" % (self.idAforo, idClasificacion)
		q = QSqlQuery(sql, self.db)
		if not q.isActive():
			self.nombre = "%d" % (self.idAforo)
			self.nombreFuente = ""
			raise CalcException(self,
				"Error al consultar los datos de la clasificacion %d " % (idClasificacion))
		res = []
		valores = {}
		while q.next():
			id = int(q.value(0) or 0)
			nombre = str(q.value(1) or "")
			idclas = int(q.value(2) or 0)
			valor = float(q.value(3) or 0.0)
			res.append(Dato(id, nombre, idclas, valor))
			self.cacheValores[id] = valor
		q.clear()
		self.cacheDatos[idClasificacion] = res

	def consigueClasificacionesBD(self):
		sql = "select idclasificacion from fuenteclasificacion where idfuente = %d" % (self.idFuente)
		q = QSqlQuery(sql, self.db)
		if not q.isActive():
			raise CalcException(self, "Error al consultar las clasificaciones " + \
					"para la fuente %d" % (self.idFuente))
		res = []
		while q.next():
			id = int(q.value(0) or 0)
			res.append(id)
		q.clear()
		self.cacheClasificaciones = res

	def clasificaciones(self):
		if self.cacheClasificaciones is None:
			self.consigueClasificacionesBD()
		return self.cacheClasificaciones

	def datos(self, idClasificacion):
		if idClasificacion not in self.cacheDatos:
			self.consigueDatosBD(idClasificacion)
		return self.cacheDatos[idClasificacion]

	def valorDato(self, idClasificacion, idDato):
		if idDato not in self.cacheValores:
			self.consigueDatosBD(idClasificacion)
		return self.cacheValores[idDato]

	def consigueDatosPropios(self):
		QApplication.processEvents()
		sql = """select a.idfuente, a.nombre, f.nombre, a.escala
			from aforo a, fuente f
			where a.id = %d and
				f.id = a.idfuente
			""" % (self.idAforo)
		q = QSqlQuery(sql, self.db)
		self.nombre = ""
		self.nombreFuente = ""
		if not q.isActive():
			raise CalcException(self, "Error en valor al buscar aforo para " + \
					"idaforo = %d" % ( self.idAforo ))
		if not q.next():
			raise CalcException(self, "Error: no existe el aforo para " + \
					"idaforo = %d" % ( self.idAforo ))
		self.idFuente = int(q.value(0) or 0)
		self.nombre = str(q.value(1) or "")
		self.nombreFuente = str(q.value(2) or "")
		escala_raw = q.value(3)
		if escala_raw is not None:
			try:
				self.escala = float(escala_raw)
			except (ValueError, TypeError):
				self.escala = None
		else:
			self.escala = None
		q.clear()

class CalculaEscenario:
	def __init__(self, idEscenario, db, cache, motorJS, avisador):
		self.db = db
		self.cache = cache
		self.motorJS = motorJS
		self.idEscenario = idEscenario
		self.cacheContaminantes = {}
		self.cacheFormulas = {}
		self.cacheFormulaClasificacion = {}
		self.cacheFormulaContaminante = {}
		self.cacheAforosContaminanteValidado = None
		self.avisador = avisador
		self.calculados = 0
		self.total = 0
		self.informe = u""
		self.generaInforme = False
		self.informeAFichero = False
		self.ficheroInforme = None
		self.nombreFicheroInforme = None
		s = QSettings()
		self.embellece = bool(s.value("script/beautifier", False))

	def limpiaCacheParcial(self):
		self.cacheContaminantes = {}
		self.cacheFormulas = {}
		self.cacheFormulasClasificacion = {}
		self.cacheFormulasContaminante = {}

	def daMensaje(self, msg):
		if self.avisador is None:
			return
		if not self.avisador.daMensaje(msg, self.calculados):
			raise CalcException(None, "Cancelada")

	def iniciaFicheroDebug(self):
		self.informeAFichero = True
		(fileno, self.nombreFicheroInforme) = tempfile.mkstemp(text = True)
		self.ficheroInforme = os.fdopen(fileno, "w+", encoding='utf-8')
		self.ficheroInforme.write(self.informe)
		self.ficheroInforme.flush()

	def debug(self, msg):
		if self.generaInforme:
			if self.informeAFichero:
				m = msg + u"\n"
				self.ficheroInforme.write(m)
			else:
				self.informe = self.informe + msg + u"\n"
				if len(self.informe) > 5000:
					self.iniciaFicheroDebug()

	def debugException(self, type, value, tback):
		if self.generaInforme:
			traceback.print_exception(tback, None, self.ficheroInforme)

	def getInforme(self):
		if self.informeAFichero and self.ficheroInforme is not None:
			with open(self.nombreFicheroInforme, encoding='utf-8') as f2:
				res = f2.read()
			return res
		else:
			return self.informe

	def guardaInforme(self, nombreFichero):
		if self.informeAFichero and self.ficheroInforme is not None:
			shutil.copy(self.nombreFicheroInforme, nombreFichero)
		else:
			with open(nombreFichero, "w+", encoding='utf-8') as f2:
				f2.write(self.informe)

	def limpiaInforme(self, genera):
		self.informe = u""
		self.generaInforme = genera
		self.informeAFichero = False
		self.ficheroInforme = None
		self.nombreFicheroInforme = None

	def descartaInforme(self):
		if self.ficheroInforme is not None:
			self.ficheroInforme.close()
			os.unlink(self.nombreFicheroInforme)
		self.limpiaInforme(False)

	def terminaInforme(self):
		if self.ficheroInforme is not None:
			self.ficheroInforme.close()

	def ejecutaSql(self, sql, aforo = None):
		QApplication.processEvents()
		q = self.db.exec(sql)
		if not q.isActive():
			raise CalcException(aforo, q.lastError().text())
		return q

	def borra(self):
		sql = """delete
			from contaminante
			where idaforo in (
				select a.id
				from aforo a, fuente f
				where a.idfuente = f.id and
					f.idescenario = %d
				)
			""" % (self.idEscenario)
		self.ejecutaSql(sql).clear()

	def insertaContaminanteAforo(self, aforo, idContaminante, idClasificacion, valor):
		sql = """insert
			into contaminanteaforo (
				id, idaforo, idclasificacion, idcontaminante, valor)
			values (
				nextval('seq_contaminanteaforo'), %d, %d, %d, %f)
			""" % (aforo.idAforo, idClasificacion, idContaminante, valor)
		self.ejecutaSql(sql, aforo).clear()

	def consigueAforosContaminanteValidado(self):
		sql = """select distinct a.id
			from contaminantevalidadoaforo cv, aforo a, fuente f
			where f.idescenario = %d and
				a.idfuente = f.id and
				cv.idaforo = a.id
			""" % (self.idEscenario)
		q = self.ejecutaSql(sql)
		r = set()
		while q.next():
			id = int(q.value(0) or 0)
			r.add(id)
		q.clear()
		self.cacheAforosContaminanteValidado = r

	def intentaContaminanteValidado(self, aforo, idContaminante, idClasificacion):
		if self.cacheAforosContaminanteValidado is None:
			self.consigueAforosContaminanteValidado()
		if aforo.idAforo not in self.cacheAforosContaminanteValidado:
			return None
		sql = """select valor
			from contaminantevalidadoaforo
			where idaforo = %d and
				idcontaminante = %d and
				idclasificacion = %d
			""" % (aforo.idAforo, idContaminante, idClasificacion)
		q = self.ejecutaSql(sql, aforo)
		if q.next():
			v_raw = q.value(0)
			if v_raw is None:
				q.clear()
				raise CalcException(aforo, "Error en valor al buscar contaminantevalidadoaforo para " + \
						"idaforo = %d, idcontaminante = %d, idclasificacion = %d" % (
						aforo.idAforo, idContaminante, idClasificacion))
			try:
				v = float(v_raw)
			except (ValueError, TypeError):
				q.clear()
				raise CalcException(aforo, "Error en valor al buscar contaminantevalidadoaforo para " + \
						"idaforo = %d, idcontaminante = %d, idclasificacion = %d" % (
						aforo.idAforo, idContaminante, idClasificacion))
			self.debug(u"\t\tContaminante Validado: %f" % (v))
			return v
		q.clear()
		return None

	def consigueFormula(self, aforo, idFormula):
		sql = "select expresion from formula where id = %d" % (idFormula)
		q = self.ejecutaSql(sql, aforo)
		if not q.next():
			raise CalcException(aforo, "Error en valor al buscar fórmula con id = %d" % (
					idFormula))
		expresion = str(q.value(0) or "")
		q.clear()
		self.cacheFormulas[idFormula] = expresion

	def ejecutaFormula(self, aforo, idClasificacion, idContaminante, idFormula, idDato = None):
		if idFormula not in self.cacheFormulas:
			self.consigueFormula(aforo, idFormula)
		expresion = self.cacheFormulas[idFormula]
		datos = Dato.toDict(aforo.datos(idClasificacion))
		# params = { 'ds' : datos }
		params = {}
		self.motorJS.setActualValues(datos)
		if idDato is not None:
			params['d'] = aforo.valorDato(idClasificacion, idDato)
		try:
			if self.generaInforme:
				if self.embellece:
					bonita = bonito.ponBonito(expresion)
				else:
					bonita = expresion
				bonita = bonita.replace("\n", "\n\t\t\t\t")
				self.debug(u"\t\t\tFórmula: \n\t\t\t\t%s" % (bonita))
			v = self.motorJS.evaluaFormula(expresion, params)
			self.debug(u"\t\t\t\tResultado: %f" % (v))
			return v
		except Exception as e:
			mensaje = str(e)
			clasificacion = Clasificacion.fromIdClasificacion(idClasificacion, self.db)
			contaminante = Contaminante.fromIdContaminante(idContaminante, self.db)
			mensaje = mensaje + (u"\nen clasificacion %s, contaminante %s" % (
						clasificacion.codigo, contaminante.nombre))
			if idDato is not None:
				dato = Dato.fromIdDato(idDato, self.db)
				mensaje = mensaje + (u"\ndato '%s'" % (dato.nombre))
			raise CalcException(aforo, mensaje)

	def consigueFormulaClasificacion(self, aforo, idContaminante, idClasificacion):
		clave = "%d-%d" % (idContaminante, idClasificacion)
		if clave in self.cacheFormulaClasificacion:
			return self.cacheFormulaClasificacion[clave]
		sql = """
			select idformula
			from mapdatocontaminante
			where idclasificacion = %d
				and idcontaminante = %d
				and idescenario = %d
				and iddato is null
			""" % (idClasificacion, idContaminante, self.idEscenario)
		q = self.ejecutaSql(sql, aforo)
		if not q.next():
			self.cacheFormulaClasificacion[clave] = None
			return None
		idFormula_raw = q.value(0)
		q.clear()
		if idFormula_raw is None:
			raise CalcException(aforo, "Error en valor al buscar fórmula de clasificación para " + \
					"idcontaminante = %d, idclasificacion = %d" % (
					idContaminante, idClasificacion))
		try:
			idFormula = int(idFormula_raw)
		except (ValueError, TypeError):
			raise CalcException(aforo, "Error en valor al buscar fórmula de clasificación para " + \
					"idcontaminante = %d, idclasificacion = %d" % (
					idContaminante, idClasificacion))
		self.cacheFormulaClasificacion[clave] = idFormula
		return idFormula

	def intentaFormulaClasificacion(self, aforo, idContaminante, idClasificacion):
		idFormula = self.consigueFormulaClasificacion(aforo, idContaminante, idClasificacion)
		if idFormula is None:
			return None
		self.debug(u"\t\tTengo fórmula de clasificación")
		return self.ejecutaFormula(aforo, idClasificacion, idContaminante, idFormula)

	def consigueFormulaContaminante(self, aforo, idContaminante, idClasificacion):
		clave = "%d-%d" % (idContaminante, idClasificacion)
		if clave in self.cacheFormulaContaminante:
			return self.cacheFormulaContaminante[clave]
		sql = """select d.id, m.idformula
			from dato d, mapdatocontaminante m
			where d.idclasificacion in (select * from jerarquia_clasificacion(%d)) and
				m.idclasificacion in (select * from jerarquia_clasificacion(%d)) and
				d.id = m.iddato and
				m.idcontaminante = %d and
				m.idescenario = %d
			""" % (idClasificacion, idClasificacion, idContaminante, self.idEscenario)
		q = self.ejecutaSql(sql, aforo)
		res = []
		while q.next():
			idDato = int(q.value(0) or 0)
			idFormula = int(q.value(1) or 0)
			res.append([idDato, idFormula])
		q.clear()
		self.cacheFormulaContaminante[clave] = res
		return res

	def intentaFormulaContaminante(self, aforo, idContaminante, idClasificacion):
		lista = self.consigueFormulaContaminante(aforo, idContaminante, idClasificacion)
		res = 0.0
		if self.generaInforme:
			listaDatos = {}
		for i in lista:
			idDato = i[0]
			idFormula = i[1]
			if self.generaInforme:
				dato = Dato.fromIdDato(idDato, self.db)
				self.debug(u"\t\tCalculo para el dato '%s'" % (dato.nombre))
			v = self.ejecutaFormula(aforo, idClasificacion, idContaminante, idFormula, idDato)
			if v is None:
				return None
			res = res + v
			if self.generaInforme:
				nombre = dato.nombre
				while nombre in listaDatos:
					nombre = nombre + " - DUP!"
				listaDatos[nombre] = v
		if self.generaInforme:
			contaminante = Contaminante.fromIdContaminante(idContaminante, self.db)
			self.debug(u"\t\tResumen para el contaminante '%s'" % (contaminante.nombre))
			for k, v in listaDatos.items():
				self.debug(u"\t\t\t%s\t%f" % (k, v))
		return res

	def calculaContaminanteAforo(self, aforo, idContaminante, idClasificacion):
		if self.generaInforme:
			contaminante = Contaminante.fromIdContaminante(idContaminante, self.db)
			clasificacion = Clasificacion.fromIdClasificacion(idClasificacion, self.db)
			self.debug(u"\tCalculo el contaminante '%s' para la clasificacion '%s'"
					% (contaminante.nombre, clasificacion.codigo))
		v = self.intentaContaminanteValidado(aforo, idContaminante, idClasificacion)
		if v is not None:
			return v
		v = self.intentaFormulaClasificacion(aforo, idContaminante, idClasificacion)
		if v is not None:
			return v
		v = self.intentaFormulaContaminante(aforo, idContaminante, idClasificacion)
		if v is not None:
			return v
		return 0.0

	def actualizaContaminanteAforo(self, aforo, idContaminante, idClasificacion):
		v = self.calculaContaminanteAforo(aforo, idContaminante, idClasificacion)
		if v is None or v == 0.0:
			return
		escala = aforo.escala
		if aforo.escala is None:
			escala = 1.0
		v = v * escala
		if self.generaInforme:
			contaminante = Contaminante.fromIdContaminante(idContaminante, self.db)
			clasificacion = Clasificacion.fromIdClasificacion(idClasificacion, self.db)
			self.debug(u"\tContaminante '%s' para la clasificacion '%s', escala %f: %f"
					% (contaminante.nombre, clasificacion.codigo, escala, v))
		self.insertaContaminanteAforo(aforo, idContaminante, idClasificacion, v)

	def consigueContaminantesBD(self, idClasificacion):
		sql = """select distinct m.idcontaminante
			from mapdatocontaminante m
			where m.idclasificacion in (select * from jerarquia_clasificacion(%d)) and
				m.idEscenario = %d
			""" % (idClasificacion, self.idEscenario)
		q = self.ejecutaSql(sql)
		res = []
		while q.next():
			id = int(q.value(0) or 0)
			res.append(id)
		q.clear()
		self.cacheContaminantes[idClasificacion] = res

	def contaminantes(self, idClasificacion):
		if idClasificacion not in self.cacheContaminantes:
			self.consigueContaminantesBD(idClasificacion)
		return self.cacheContaminantes[idClasificacion]

	def calculaClasificacion(self, aforo, idClasificacion):
		if self.generaInforme:
			clasificacion = Clasificacion.fromIdClasificacion(idClasificacion, self.db)
			self.debug(u"Calculo la clasificacion '%s'" % (clasificacion.codigo))
			datos = Dato.toDict(aforo.datos(idClasificacion))
			for i in datos.keys():
				self.debug(u"\tDato '%s': %f" % (i, datos[i]))
			self.debug(u"Termino clasificación '%s'" % (clasificacion.codigo))
		contaminantes = self.contaminantes(idClasificacion)
		for i in contaminantes:
			self.actualizaContaminanteAforo(aforo, i, idClasificacion)

	def intCalculaAforo(self, idAforo):
		aforo = Aforo(self.db, self.cache, idAforo)
		if self.generaInforme:
			self.debug(u"Calculo aforo '%s'" % (aforo.nombre))
			p = aforo.params()
			for i in p.keys():
				self.debug(u"\tParámetro '%s', valor: %f" % (i, p[i]))
		self.daMensaje("Calculando fuente %s, \naforo %s" % (aforo.nombreFuente, aforo.nombre))
		params = aforo.params()
		self.motorJS.nuevoContexto(params)
		try:
			clas = aforo.clasificaciones()
			for i in clas:
				self.calculaClasificacion(aforo, i)
		except:
			(type, value, tback) = sys.exc_info()
			self.debugException(type, value, tback)
			raise
		finally:
			self.motorJS.destruyeContexto()
		self.debug(u"Termino correctamente %s" % (aforo.nombre))
		self.calculados = self.calculados + 1

	def intCalculaFuente(self, idFuente):
		sql = "select id from aforo where idfuente = %d" % (idFuente)
		q = self.ejecutaSql(sql)
		while q.next():
			id = int(q.value(0) or 0)
			self.intCalculaAforo(id)
		q.clear()

	def calculaTodo(self):
		sql = "select id from fuente where idescenario = %d" % (self.idEscenario)
		q = self.ejecutaSql(sql)
		while q.next():
			id = int(q.value(0) or 0)
			print("Calculando fuente %d" % (id))
			self.intCalculaFuente(id)
			self.limpiaCacheParcial()
			self.motorJS.collectGarbage()
			gc.collect()
		q.clear()

	def borraDatosZona(self):
		sql = """delete
			from datozona
			where idzona in (
					select id
					from zona
					where idnivelzona > 1
					) and
				idtipodatozona in (
					select id
					from tipodatozona
					where idescenario = %d
					)
			""" % (self.idEscenario)
		self.ejecutaSql(sql).clear()

	def borraEscenario(self):
		self.daMensaje("Borrando datos anteriores")
		sql = """delete
			from contaminanteaforo
			where idaforo in (
				select a.id
				from aforo a, fuente f
				where a.idfuente = f.id and
					f.idescenario = %d
					)
			""" % (self.idEscenario)
		self.ejecutaSql(sql).clear()
		sql = """delete
			from contaminantezona
			where idfuente in (
				select id
				from fuente
				where idescenario = %d
				)
			""" % (self.idEscenario)
		self.ejecutaSql(sql).clear()
		self.borraDatosZona()
		self.calculados = self.calculados + 1

	def borraAforo(self, idAforo):
		sql = "delete from contaminanteaforo where idaforo = %d" % (idAforo)
		self.ejecutaSql(sql).clear()

	def borraFuente(self, idFuente):
		sql = """delete
			from contaminanteaforo
			where idaforo in (
				select id
				from aforo
				where idfuente = %d
				)
			""" % (idFuente)
		self.ejecutaSql(sql).clear()
		self.calculados = self.calculados + 1

	def calculaNumAforos(self):
		sql = """select count(*)
			from aforo a, fuente f
			where a.idfuente = f.id and
				f.idescenario = %d
			""" % (self.idEscenario)
		q = self.ejecutaSql(sql)
		if q.next():
			self.total = int(q.value(0) or 0) + 1
		self.avisador.setNumAforos(self.total)

	def calculaNumAforosFuente(self, idFuente):
		sql = """select count(*)
			from aforo a
			where a.idfuente = %d
			""" % (idFuente)
		q = self.ejecutaSql(sql)
		if q.next():
			self.total = int(q.value(0) or 0) + 1
		self.avisador.setNumAforos(self.total)

	def calculaDatosZona(self):
		sql = """insert into datozona (id, idzona, idtipodatozona, dato)
			select nextval('seq_datozona'), zp.id, tdz.id, sum(dz.dato)
			from tipodatozona tdz, datozona dz, zona z, relzona rz, zona zp
			where tdz.idescenario = %d and
				dz.idtipodatozona = tdz.id and
				dz.idzona = z.id and
				z.idnivelzona = 1 and
				rz.idzona = z.id and
				rz.idzonapadre = zp.id
			group by zp.id, tdz.id
			""" % (self.idEscenario)
		self.ejecutaSql(sql).clear()

	def mapeaContaminantesAZona(self):
		sql = """insert into contaminantezona (id, idcontaminante,
					idfuente, idzona, idclasificacion, valor)
			select nextval('seq_contaminantezona'), ca.idcontaminante,
					a.idfuente, a.idzona, ca.idclasificacion, sum(valor)
			from contaminanteaforo ca, aforo a, zona z, fuente f
			where a.id = ca.idaforo and
				z.id = a.idzona and
				z.idnivelzona = 1 and
				f.id = a.idfuente and
				f.idescenario = %d
			group by ca.idcontaminante, a.idfuente, a.idzona, ca.idclasificacion
			""" % (self.idEscenario)
		self.ejecutaSql(sql).clear()
		sql = """create temporary table contaminantezona_tmp
			(like contaminantezona including indexes)""";
		self.ejecutaSql(sql).clear()
		sql = """insert into contaminantezona_tmp (id, idcontaminante,
						idfuente, idzona, idclasificacion,
						valor)
			select nextval('seq_contaminantezona'), t.idcontaminante,
						t.idfuente, z.id, t.idclasificacion,
						sum(t.valor * dz.dato / dzp.dato)
			from zona z, relzona rz, datozona dz, datozona dzp, (
				select ca.idcontaminante as idcontaminante,
					a.idfuente as idfuente,
					a.idzona as idzona,
					ca.idclasificacion as idclasificacion,
					coalesce(a.idtipodatozona, f.idtipodatozona) as idtipodatozona,
					sum(valor) as valor
				from contaminanteaforo ca, aforo a, zona z, fuente f
				where a.id = ca.idaforo and
					f.id = a.idfuente and
					z.id = a.idzona and
					z.idnivelzona > 1 and
					f.idescenario = %d
				group by idcontaminante, idfuente, idzona, idclasificacion,
					coalesce(a.idtipodatozona, f.idtipodatozona)
				) as t
			where t.idzona = rz.idzonapadre and
				z.id = rz.idzona and
				z.idnivelzona = 1 and
				dzp.idzona = t.idzona and
				dz.idzona = z.id and
				dzp.idtipodatozona = t.idtipodatozona and
				dz.idtipodatozona = t.idtipodatozona and
				dz.dato > 0
			group by t.idcontaminante, t.idfuente, z.id, t.idclasificacion
			""" % (self.idEscenario)
		self.ejecutaSql(sql).clear()
		sql = """update contaminantezona cz
			set valor = cz.valor + coalesce((
				select czt.valor
				from contaminantezona_tmp czt
				where czt.idcontaminante = cz.idcontaminante and
					czt.idfuente = cz.idfuente and
					czt.idzona = cz.idzona and
					czt.idclasificacion = cz.idclasificacion
				), 0.0)
			"""
		self.ejecutaSql(sql).clear()
		sql = """delete
			from contaminantezona_tmp czt
			where exists (
				select 1
				from contaminantezona cz
				where czt.idcontaminante = cz.idcontaminante and
					czt.idfuente = cz.idfuente and
					czt.idzona = cz.idzona and
					czt.idclasificacion = cz.idclasificacion
				)
			"""
		self.ejecutaSql(sql).clear()
		sql = """insert into contaminantezona (id, idcontaminante, idfuente, idzona, idclasificacion, valor)
			select id, idcontaminante, idfuente, idzona, idclasificacion, valor
			from contaminantezona_tmp
			"""
		self.ejecutaSql(sql).clear()
		sql = "drop table if exists contaminantezona_tmp"
		self.ejecutaSql(sql).clear()

	def borraTablasTemporales(self):
		sql = "drop table if exists contaminantezona_tmp"
		self.ejecutaSql(sql).clear()

	def calcula(self):
		try:
			self.calculados = 0
			self.limpiaInforme(False)
			self.cache.setIdEscenario(self.idEscenario)
			self.calculaNumAforos()
			self.borraEscenario()
			self.calculaTodo()
			self.calculaDatosZona()
			self.mapeaContaminantesAZona()
			if self.avisador is not None:
				self.avisador.reset()
		finally:
			self.borraTablasTemporales()

	def calculaAforo(self, idAforo):
		try:
			QApplication.instance().setOverrideCursor(Qt.WaitCursor)
			self.limpiaInforme(True)
			self.cache.setIdEscenario(self.idEscenario)
			self.borraAforo(idAforo)
			self.intCalculaAforo(idAforo)
		except Exception as e:
			self.debug(u'\nSe ha producido un error: \n' + str(e))
			raise
		finally:
			self.terminaInforme()
			self.borraTablasTemporales()
			QApplication.instance().restoreOverrideCursor()

	def calculaFuente(self, idFuente):
		try:
			self.limpiaInforme(False)
			self.cache.setIdEscenario(self.idEscenario)
			self.calculaNumAforosFuente(idFuente)
			self.borraFuente(idFuente)
			self.intCalculaFuente(idFuente)
			if self.avisador is not None:
				self.avisador.reset()
		finally:
			self.borraTablasTemporales()
