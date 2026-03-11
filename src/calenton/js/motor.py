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
##############################################################################

from PyQt6.QtQml import QJSEngine
from PyQt6.QtCore import QObject, pyqtSlot
import math


def isNaN(f):
	return f != f


class JSError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return str(self.value)


class SyntaxError(JSError):
	def __init__(self, msg):
		self.value = str(msg) if msg else "Error desconocido"


class ValueError(JSError):
	def __init__(self, value):
		JSError.__init__(self, str(value) + " no es un número")


class JSHelper(QObject):
	"""Objeto expuesto al motor JS para implementar la función ds()."""

	def __init__(self, parent=None):
		super().__init__(parent)
		self.actualValues = {}

	@pyqtSlot(str, result=float)
	def ds(self, nombre):
		if nombre in self.actualValues:
			v = self.actualValues[nombre]
			return float(v)
		raise KeyError(f"No está definido el dato '{nombre}'")


class Motor:
	"""
	Motor de evaluación de fórmulas JavaScript.

	Reemplaza la implementación original basada en QScriptEngine (eliminado en Qt5)
	con QJSEngine (PySide6.QtQml). La función ds() se expone a través de un
	QObject auxiliar. Los parámetros locales se pasan mediante IIFEs de JavaScript.
	"""

	def __init__(self, db, emulateStack=False):
		self.engine = QJSEngine()
		self.db = db
		self.actualValues = {}
		self._contextStack = []
		# Auxiliar expuesto a JS para la función ds()
		self._helper = JSHelper()
		self.engine.globalObject().setProperty(
			"_helper", self.engine.newQObject(self._helper))
		self.engine.evaluate(
			"function ds(name) { return _helper.ds(name); }")

	def setActualValues(self, values):
		self.actualValues = {str(k): v for k, v in values.items()}
		self._helper.actualValues = self.actualValues

	def ponParametros(self, params):
		"""Añade parámetros al contexto global del motor."""
		for k, v in params.items():
			js_val = self.engine.toScriptValue(v)
			self.engine.globalObject().setProperty(str(k), js_val)

	def nuevoContexto(self, params):
		"""Guarda los valores actuales de las claves y establece nuevos parámetros globales."""
		g = self.engine.globalObject()
		saved = {}
		for k in params:
			prop = g.property(str(k))
			saved[k] = prop
		self._contextStack.append(saved)
		for k, v in params.items():
			g.setProperty(str(k), self.engine.toScriptValue(v))

	def destruyeContexto(self):
		"""Restaura los valores guardados por el último nuevoContexto."""
		if not self._contextStack:
			return
		saved = self._contextStack.pop()
		g = self.engine.globalObject()
		for k, v in saved.items():
			g.setProperty(str(k), v)

	def collectGarbage(self):
		"""Fuerza el GC del motor JS."""
		self.engine.collectGarbage()

	def evaluaFormula(self, formula, params=None):
		"""
		Evalúa una fórmula JavaScript con parámetros opcionales.

		Los parámetros se establecen temporalmente como variables globales
		(igual que hacía QScriptEngine con pushContext/popContext) para que
		engine.toScriptValue() gestione correctamente None→null, nan→NaN, etc.
		"""
		g = self.engine.globalObject()
		saved = {}
		if params:
			for k, v in params.items():
				key = str(k)
				saved[key] = g.property(key)
				g.setProperty(key, self.engine.toScriptValue(v))
		try:
			result = self.engine.evaluate(f"({formula})")
		finally:
			for key, val in saved.items():
				g.setProperty(key, val)

		if result.isError():
			raise SyntaxError(result.toString())
		if not result.isNumber():
			raise ValueError(result.toString())
		r = result.toNumber()
		if isNaN(r):
			raise JSError("El resultado es NaN")
		return r
