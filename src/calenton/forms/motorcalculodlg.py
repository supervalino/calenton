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

from PyQt6 import QtWidgets, QtCore
from .ui.Ui_motorcalculodlg import *
from ts import DataDialog

class MotorCalculoDlg (DataDialog, Ui_MotorcalculoDialogClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)

	def putData(self, r):
		self.codigo.setText(str(r.value('codigo') or ""))
		self.nombre.setText(str(r.value('nombre') or ""))
		self.clase.setText(str(r.value('clase') or ""))
		self.descripcion.setText(str(r.value('descripcion') or ""))
		return True

	def getData(self, r):
		if self.codigo.text().strip() == "":
			self.setEditionError(self.tr("El código no puede estar vacío"))
			return False
		if self.nombre.text().strip() == "":
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		if self.clase.text().strip() == "":
			self.setEditionError(self.tr("La clase no puede estar vacía"))
			return False
		r.setValue('codigo', self.codigo.text().strip())
		r.setValue('nombre', self.nombre.text().strip())
		r.setValue('clase', self.clase.text().strip())
		r.setValue('descripcion', self.descripcion.toPlainText().strip())
		return True
