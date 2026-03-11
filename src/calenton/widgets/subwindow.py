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
# $Id: subwindow.py 350 2010-11-03 13:08:29Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/widgets/subwindow.py $
#
##############################################################################

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class SubWindowBase (object):
	@pyqtSlot()
	def copy(self):
		pass

	@pyqtSlot()
	def print_(self):
		pass

	def canCopy(self):
		return False

	def canPrint(self):
		return False

class SubWindow (SubWindowBase, QWidget):
	def __init__(self, parent = None, flags = Qt.WindowType(0)):
		QWidget.__init__(self, parent, flags)
