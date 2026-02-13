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
# $Id: motor.py 211 2010-04-20 10:22:52Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/js/motor.py $
#
##############################################################################

from PyQt4.QtScript import *
from PyQt4.QtSql import QSqlQuery
from PyQt4.QtCore import QString

import types
import copy
import math

def isNaN(f):
	return (f != f)

class JSError (Exception):
	def __init__(self, value):
		self.value = value
		
	def __str__(self):
		return str(self.value)
		
	def __unicode__(self):
		return unicode(self.value)
		
class SyntaxError (JSError):
	def __init__(self, error):
		if error.isError():
			self.value = unicode(error.toString())
		else:
			self.value = u"Error desconocido"

class ValueError (JSError):
	def __init__(self, value):
		JSError.__init__(self, unicode(value) + u" no es un número")

class Motor (QScriptEngine):
	@staticmethod
	def myDS(context, engine):
		if context.argumentCount() != 1:
			return context.throwError(QString(u"ds necesita un argumento"))
		nombre = unicode(context.argument(0).toString())
		if engine.actualValues.has_key(nombre):
			return QScriptValue(engine.actualValues[nombre])
		mensaje = u"No está definido el dato '%s'" % (nombre)
		return context.throwError(QString(mensaje))
			
	def __init__(self, db, emulateStack):
		QScriptEngine.__init__(self)
		self.db = db
		self.nestLevel = 0
		self.emulateStack = emulateStack
		self.actualValues = {}
		fun = self.newFunction(Motor.myDS)
		self.globalObject().setProperty("ds", fun)
		if self.emulateStack:
			actual = []
			self.stack = [ actual ]
			
	def setActualValues(self, values):
		self.actualValues = {}
		for i in values.keys():
			self.actualValues[unicode(i)] = values[i]
		
	def ponValores(self, var, values):
		for i in values.keys():
			var.setProperty(QString(i), self.creaValor(values[i]))
			
	def creaValor(self, v):
		if type(v) == types.DictType:
			r = self.newArray()
			# self.ponValores(r, v)
			return r
		else:
			return QScriptValue(v)
		
	def ponParametros(self, params):
		ctx = self.currentContext()
		ao = ctx.activationObject()
		if self.emulateStack:
			c = copy.deepcopy(params)
			last = self.stack[len(self.stack) - 1]
			last.append(c)
		self.ponValores(ao, params)
		
	def rehazContexto_interna(self):
		if not self.emulateStack:
			return
		ctx = self.currentContext()
		ao = ctx.activationObject()
		for actual in self.stack:
			for params in actual:
				self.ponValores(ao, params)
		
	def nuevoContexto(self, params = None):
		self.pushContext()
		self.nestLevel = self.nestLevel + 1
		if self.emulateStack:
			self.rehazContexto_interna()
			self.stack.append([])
		if params is not None:
			self.ponParametros(params)
		
	def destruyeContexto(self):
		if self.nestLevel > 0:
			self.popContext()
			if self.emulateStack:
				self.stack.pop()
			self.nestLevel = self.nestLevel - 1
		
	def vuelveAContextoGlobal(self):
		while self.nestLevel > 0:
			self.destruyeContexto()
			
	def evaluaFormula(self, formula, params = None):
		self.nuevoContexto(params)
		res = self.evaluate(formula)
		self.destruyeContexto()
		if self.hasUncaughtException():
			e = self.uncaughtException()
			raise SyntaxError(e)
		if not res.isNumber():
			raise ValueError(res)
		r = res.toNumber()
		if isNaN(r):
			raise JSError(u"El resultado es NaN")
		return r
