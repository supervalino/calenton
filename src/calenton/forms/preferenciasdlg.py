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
# $Id: preferenciasdlg.py 256 2010-05-19 10:36:03Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/preferenciasdlg.py $
#
##############################################################################

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtSql
from ui.Ui_preferenciasdlg import *

class PreferenciasDlg (QDialog, Ui_PreferenciasDlgClass):
	class DataError(Exception):
		def __init__(self, mensaje):
			self.mensaje = mensaje
		
	def __init__(self, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.initDatabase()
		self.initScript()
	
	def initDatabase(self):
		s = QSettings()
		(puerto, good) = s.value("db/puerto", 5432).toInt()
		if not good:
			puerto = 5432
		self.puerto.setText(str(puerto))
		self.servidor.setText(s.value("db/servidor").toString())
		self.basedatos.setText(s.value("db/basedatos").toString())
		self.usuario.setText(s.value("db/usuario").toString())
		self.password.setText(s.value("db/password").toString())
		
	def initScript(self):
		s = QSettings()
		ss = s.value("script/stackable").toBool()
		if ss:
			ss2 = Qt.Checked
		else:
			ss2 = Qt.Unchecked
		self.checkScriptStackable.setCheckState(ss2)
		sb = s.value("script/beautifier").toBool()
		if sb:
			sb2 = Qt.Checked
		else:
			sb2 = Qt.Unchecked
		self.beautifier.setCheckState(sb2)
		
	def tomaValor(self, componente, mensaje = None, puedeVacio = False):
		valor = componente.text().trimmed()
		if (not puedeVacio) and valor.isEmpty():
			QMessageBox.warning(self, self.tr("Error"), mensaje, QMessageBox.Ok)
			raise DataError(mensaje)
		return valor
		
	def tomaValorEntero(self, componente, mensaje = None, puedeVacio = False, valorVacio = -1):
		s = self.tomaValor(componente, mensaje, puedeVacio)
		valor = valorVacio
		if not s.isEmpty():
			(valor, good) = s.toInt()
			if not good:
				QMessageBox.warning(self, self.tr("Error"), mensaje, QMessageBox.Ok)
				raise DataError(mensaje)
		return valor
		
	def recogeBaseDatos(self):
		servidor = self.tomaValor(self.servidor, self.tr("Se debe indicar el servidor de base de datos"))
		basedatos = self.tomaValor(self.basedatos, self.tr("Se debe indicar la base de datos"))
		usuario = self.tomaValor(self.usuario, self.tr("Se debe indicar el usuario"))
		password = self.tomaValor(self.password)
		puerto = self.tomaValorEntero(self.puerto, self.tr("Se debe indicar el puerto del servidor"))	
		return (servidor, puerto, basedatos, usuario, password)
		
	def tomaBaseDatos(self):
		(servidor, puerto, basedatos, usuario, password) = self.recogeBaseDatos()
		s = QSettings()
		s.setValue("db/puerto", puerto)
		s.setValue("db/servidor", servidor)
		s.setValue("db/basedatos", basedatos)
		s.setValue("db/usuario", usuario)
		s.setValue("db/password", password)
		
	def tomaScript(self):
		s = QSettings()
		ss2 = self.checkScriptStackable.checkState()
		ss = (ss2 == Qt.Checked)
		s.setValue("script/stackable", ss)
		sb2 = self.beautifier.checkState()
		sb = (sb2 == Qt.Checked)
		s.setValue("script/beautifier", sb)
		
	@pyqtSlot("bool")
	def on_probar_clicked(self, checked):
		try:
			(servidor, puerto, basedatos, usuario, password) = self.recogeBaseDatos()
		except DataError:
			return
		db = QtSql.QSqlDatabase.addDatabase('QPSQL', '__test')
		db.setDatabaseName(basedatos)
		db.setHostName(servidor)
		db.setUserName(usuario)
		db.setPassword(password)
		db.setPort(puerto)
		if db.open():
			QMessageBox.information(self, self.tr("Éxito"),
					self.tr("Conexión correcta"), QMessageBox.Ok)
		else:
			QMessageBox.warning(self, self.tr("Error"),
					self.tr("No se ha podido conectar a la base de datos: %1").arg(db.lastError().text()),
					QMessageBox.Ok)
		db.close()
		db = None
		QtSql.QSqlDatabase.removeDatabase("__test")
		
	def aplica(self):
		try:
			self.tomaBaseDatos()
			self.tomaScript()
		except:
			pass
		
	@pyqtSlot("QAbstractButton *")
	def on_botones_clicked(self, button):
		if self.botones.buttonRole(button) == QDialogButtonBox.ApplyRole:
			self.aplica()
		
	def accept(self):
		try:
			self.tomaBaseDatos()
			self.tomaScript()
			QDialog.accept(self)
		except:
			pass
	
