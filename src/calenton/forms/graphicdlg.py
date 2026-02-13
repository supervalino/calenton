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
# $Id: graphicdlg.py 198 2010-04-13 15:39:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/graphicdlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from ui import Ui_graphicdlg

class GraphicDlg (QDialog, Ui_graphicdlg.Ui_GraphicDlgClass):
	def __init__(self, parent=None):
		super(GraphicDlg, self).__init__(parent)
		self.setupUi(self)
