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
# $Id: escenariodlg.py 59 2010-01-18 17:28:55Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/escenariodlg.py $
#
##############################################################################

from PyQt6 import QtWidgets, QtCore, QtGui
from .ui import Ui_escenariodlg
from ts import DataDialog

class EscenarioDlg (DataDialog, Ui_escenariodlg.Ui_EscenarioDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)

	def putData(self, r):
		self.nombre.setText(str(r.value('nombre') or ""))
		return True

	def getData(self, r):
		if self.nombre.text().strip() == "":
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		r.setValue('nombre', self.nombre.text().strip())
		return True
