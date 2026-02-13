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
# $Id: calenton.py 328 2010-07-20 11:56:05Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/calenton.py $
#
##############################################################################

from PyQt4 import QtGui
from PyQt4 import QtCore
from calentonapp import CalentonApp
from forms.main import MainWindow
import sys
import gc
QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("UTF-8"))
app = CalentonApp(sys.argv)
window = MainWindow()
QtCore.pyqtRemoveInputHook()
window.show()
window.actionQuit.triggered.connect(app.quit)
res = app.exec_()
window = None
app = None
gc.collect()
sys.exit(res)
