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

	def evaluaFormula(self, formula, params=None):
		"""
		Evalúa una fórmula JavaScript con parámetros opcionales.

		Los parámetros se pasan como variables locales mediante una IIFE
		para evitar contaminar el scope global.
		"""
		if params:
			# Serializar los valores numéricos como literales JS
			param_items = [(str(k), v) for k, v in params.items()]
			js_params = ", ".join(k for k, v in param_items)
			js_vals = ", ".join(
				str(v) if isinstance(v, (int, float)) else repr(str(v))
				for k, v in param_items
			)
			wrapped = f"(function({js_params}) {{ return ({formula}); }})({js_vals})"
		else:
			wrapped = f"({formula})"

		result = self.engine.evaluate(wrapped)
		if result.isError():
			raise SyntaxError(result.toString())
		if not result.isNumber():
			raise ValueError(result.toString())
		r = result.toNumber()
		if isNaN(r):
			raise JSError("El resultado es NaN")
		return r
