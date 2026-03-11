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
# $Id: contaminantedlg.py 59 2010-01-18 17:28:55Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/contaminantedlg.py $
#
##############################################################################

from PyQt6 import QtWidgets, QtCore, QtGui
from .ui.Ui_contaminantedlg import *
from ts import DataDialog

class ContaminanteDlg (DataDialog, Ui_ContaminanteDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)

	def putData(self, r):
		self.nombre.setText(str(r.value('nombre') or ""))
		self.descripcion.setText(str(r.value('descripcion') or ""))
		self.unidades.setText(str(r.value('unidades') or ""))
		return True

	def getData(self, r):
		if self.nombre.text().strip() == "":
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		if self.unidades.text().strip() == "":
			self.setEditionError(self.tr("Las unidades no pueden estar vacías"))
			return False
		r.setValue('nombre', self.nombre.text().strip())
		r.setValue('unidades', self.unidades.text().strip())
		r.setValue('descripcion', self.descripcion.toPlainText().strip())
		return True
