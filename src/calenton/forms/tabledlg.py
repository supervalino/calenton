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
# $Id: tabledlg.py 198 2010-04-13 15:39:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/tabledlg.py $
#
##############################################################################

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from .ui import Ui_tabledlg

class TableDlg (QDialog, Ui_tabledlg.Ui_TableDlgClass):
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setupUi(self)
