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
# $Id: motorcalculodlg.py 59 2010-01-18 17:28:55Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/motorcalculodlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from ui.Ui_motorcalculodlg import *
from ts import DataDialog

class MotorCalculoDlg (DataDialog, Ui_MotorcalculoDialogClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		
	def putData(self, r):
		self.codigo.setText(r.value('codigo').toString())
		self.nombre.setText(r.value('nombre').toString())
		self.clase.setText(r.value('clase').toString())
		self.descripcion.setText(r.value('descripcion').toString())
		return True
		
	def getData(self, r):
		if self.codigo.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El código no puede estar vacío"))
			return False
		if self.nombre.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		if self.clase.text().trimmed().isEmpty():
			self.setEditionError(self.tr("La clase no puede estar vacía"))
			return False			
		r.setValue('codigo', self.codigo.text().trimmed())
		r.setValue('nombre', self.nombre.text().trimmed())
		r.setValue('clase', self.clase.text().trimmed())
		r.setValue('descripcion', self.descripcion.toPlainText().trimmed())
		return True
