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
# $Id: hazcalculodlg.py 330 2010-07-20 21:08:06Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/hazcalculodlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from modelo import *
from ui import Ui_hazcalculodlg
from ts import DataDialog, ComboDataModel

class HazCalculoDlg (QDialog, Ui_hazcalculodlg.Ui_HazCalculoDlgClass):
	def __init__(self, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		
	def daMensaje(self, msg):
		aforo.setText(QString(msg))
		QApplication.processEvents()
		
