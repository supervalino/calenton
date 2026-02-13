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
# $Id: mapdatocontaminantedlg.py 216 2010-04-21 11:03:09Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/mapdatocontaminantedlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore, QtScript
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtScript import *
from PyQt4.QtSql import QSqlQuery
from modelo import *
from ui import Ui_mapdatocontaminantedlg
from ts import DataDialog
from ts import ComboDataModel
from js import bonito

import js.motor

class MapDatoContaminanteDlg (DataDialog, Ui_mapdatocontaminantedlg.Ui_MapDatoContaminanteDlgClass):
	def __init__(self, parent, dataModel, idEscenario, idClasificacion, idDato):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.idEscenario = idEscenario
		self.idClasificacion = idClasificacion
		self.idDato = idDato
		self.model=dataModel
		self.app = QApplication.instance()
		if not self.app.databaseInit:
			return
			
		self.db = self.model.database()
		self.cache = self.app.cache
		self.motorJS = self.app.motorJS
		self.cache.setIdEscenario(self.idEscenario)
		self.motorJS.nuevoContexto(self.cache.globals())
		self.todosDatos = self.buscaDatos()
		
		self.mContaminantes = ComboDataModel(self)
		self.mContaminantes.setQuery("select id, nombre from contaminante order by nombre", self.db)
		self.comboContaminante.setModel(self.mContaminantes)
		
		r = self.model.record()
		self.putData(r)
		
	def buscaDatos(self):
		sql = """
			select d.nombre
			from dato d
			where d.idclasificacion in (
				select *
				from jerarquia_clasificacion(%d)
				)
			""" % (self.idClasificacion)
		q = QSqlQuery(sql, self.db)
		if q.lastError().isValid():
			print q.lastError().text()
			return {}
		l = {}
		while q.next():
			n1 = q.value(0).toString()
			if n1.isEmpty():
				continue
			n1 = unicode(n1)
			l[n1] = 1.0
		return l
		
	def closeEvent(self, ev):
		m = self.motorJS
		DataDialog.closeEvent(self, ev)
		if ev.isAccepted():
			m.destruyeContexto()
		
	def prueba(self, miraSiCompleta):
		t = self.editorFormula.toPlainText().trimmed()
		self.motorJS.setActualValues(self.todosDatos)
		# params = { 'ds' : self.todosDatos }
		params = {}
		if self.idDato > 0:
			params['d'] = 1.0
		if t.isEmpty():
			self.valor.setText(QString())
			return
		if miraSiCompleta:
			e = self.motorJS.checkSyntax(t)
			if e.state() == QScriptSyntaxCheckResult.Error:
				self.valor.setText(e.errorMessage())
				return
			elif e.state() == QScriptSyntaxCheckResult.Intermediate:
				self.valor.setText(QString())
				return
		try:
			v = unicode(self.motorJS.evaluaFormula(t, params))
		except js.motor.SyntaxError, ex:
			v = unicode(ex)
		except js.motor.ValueError, ex:
			v = unicode(ex)
		self.valor.setText(QString(v))
		
	@pyqtSlot()
	def on_editorFormula_textChanged(self):
		self.prueba(True)
		
	@pyqtSlot("bool")
	def on_probar_clicked(self, checked):
		self.prueba(False)
		
	@pyqtSlot("bool")
	def on_indenta_clicked(self, checked):
		t = unicode(self.editorFormula.toPlainText().trimmed())
		t2 = bonito.ponBonito(t)
		t2 = QString(t2)
		self.editorFormula.setPlainText(t2)
		
	def getInt(self, variant, default):
		if variant.isNull() or not variant.isValid():
			return default
		(res, good) = variant.toInt()
		if not good:
			return default
		return res
		
	def setDefaultInt(self, record, field, default):
		v = record.value(field)
		if v.isNull() or not v.isValid():
			record.setValue(field, default)
		
	def getNombre(self, sql, variantid, default):
		id = self.getInt(variantid, default)
		sql2 = sql % (id)
		return unicode(self.model.first(sql2).value(0).toString())
		
	def getEscenario(self, r):
		return self.getNombre("select nombre from escenario where id = %d", 
				r.value('idescenario'), self.idEscenario)
		
	def getDato(self, r):
		if self.idDato > 0:
			return self.getNombre("select nombre from dato where id = %d", 
				r.value('iddato'), self.idDato)
		else:
			return self.tr('Fórmula de aforo')
		
	def getClasificacion(self, r):
		return self.getNombre("select codigo || '-' || descripcion from clasificacion where id = %d", 
				r.value('idclasificacion'), self.idClasificacion)
		
	def putData(self, r):
		self.escenario.setText(self.getEscenario(r))
		self.dato.setText(self.getDato(r))
		self.clasificacion.setText(self.getClasificacion(r))
		self.comboContaminante.setCurrentItemData(QtCore.QVariant(self.getInt(r.value('idcontaminante'), -1)))
		self.editorFormula.setPlainText(r.value('formula_expresion').toString())
		return True

	def getData(self, r):
		t = self.editorFormula.toPlainText().trimmed()
		if t.isEmpty():
			self.setEditionError(self.tr('Se debe especificar una fórmula'))
			return False
		(idc, good) = self.comboContaminante.currentItemData().toInt()
		if not good:
			self.setEditionError(self.tr('Se debe indicar un contaminante'))
			return False
		self.setDefaultInt(r, 'idescenario', self.idEscenario)
		self.setDefaultInt(r, 'idclasificacion', self.idClasificacion)
		if self.idDato > 0:
			self.setDefaultInt(r, 'iddato', self.idDato)
		else:
			r.setValue('iddato', QVariant(QString()))
		r.setValue('idcontaminante', idc)
		r.setValue('formula_expresion', t)
		return True
