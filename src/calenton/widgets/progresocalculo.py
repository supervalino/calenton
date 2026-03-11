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
# $Id: progresocalculo.py 204 2010-04-18 14:37:17Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/widgets/progresocalculo.py $
#
##############################################################################

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class ProgresoCalculo (QProgressDialog):
	def __init__(self, parent = None, flags = Qt.WindowType(0)):
		QProgressDialog.__init__(self, parent, flags)
		self.setMinimumDuration(0)
		self.setWindowTitle("Calculando escenario")

	def daMensaje(self, msg, calculados):
		QApplication.processEvents()
		self.setLabelText(msg)
		self.setValue(calculados)
		QApplication.processEvents()
		QApplication.instance().flush() if hasattr(QApplication.instance(), 'flush') else None
		return not self.wasCanceled()

	def setNumAforos(self, nAforos):
		self.setMinimum(0)
		self.setMaximum(nAforos)
