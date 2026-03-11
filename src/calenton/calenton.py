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
##############################################################################

import sys
import os
import gc
# Add src/ to sys.path so calenton package is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from PyQt6 import QtWidgets, QtCore
from calenton.calentonapp import CalentonApp
from calenton.forms.main import MainWindow

app = CalentonApp(sys.argv)
window = MainWindow()
window.show()
window.actionQuit.triggered.connect(app.quit)
res = app.exec()
window = None
app = None
gc.collect()
sys.exit(res)
