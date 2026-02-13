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
# $Id: elegirescenariodlg.py 193 2010-04-09 15:01:43Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/elegirescenariodlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from modelo import *
from ui import Ui_elegirescenariodlg
from ts import DataDialog, ComboDataModel

class ElegirEscenarioDlg (QDialog, Ui_elegirescenariodlg.Ui_ElegirEscenarioDlgClass):
	def __init__(self, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.db = QApplication.instance().workDb()
		self.mEscenario = ComboDataModel(self)
		self.mEscenario.setQuery("select id, nombre from escenario order by id", self.db)
		self.escenario.setModel(self.mEscenario)
	
