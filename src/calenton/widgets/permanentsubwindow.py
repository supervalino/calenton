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
# $Id: permanentsubwindow.py 59 2010-01-18 17:28:55Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/widgets/permanentsubwindow.py $
#
##############################################################################

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PermanentSubWindow (QMdiSubWindow):
	visibilityChanged = pyqtSignal("bool")
	
	def __init__(self, parent = None, flags = Qt.WindowFlags()):
		QMdiSubWindow.__init__(self, parent, flags)
		self.setAttribute(Qt.WA_DeleteOnClose, False)
		
	def hideEvent(self, evt):
		if (self.windowState() & Qt.WindowActive) == Qt.WindowActive:
			self.mdiArea().activateNextSubWindow()
		QMdiSubWindow.hideEvent(self, evt)
		if not self.isVisible():
			self.visibilityChanged.emit(False)
			
	def showEvent(self, evt):
		QMdiSubWindow.showEvent(self, evt)
		if self.isVisible():
			self.visibilityChanged.emit(True)
			
	def closeEvent(self, evt):
		self.hide()
		evt.ignore()
