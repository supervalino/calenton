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

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ProgresoCalculo (QProgressDialog):
	def __init__(self, parent = None, flags = Qt.WindowFlags()):
		QProgressDialog.__init__(self, parent, flags)
		self.setMinimumDuration(0)
		self.setWindowTitle(QString("Calculando escenario"))
		
	def daMensaje(self, msg, calculados):
		QApplication.processEvents()
		self.setLabelText(QString(msg))
		self.setValue(calculados)
		QApplication.processEvents()
		QApplication.flush()
		return not self.wasCanceled()
		
	def setNumAforos(self, nAforos):
		self.setMinimum(0)
		self.setMaximum(nAforos)
	
