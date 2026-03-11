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
# $Id: subwindowplugin.py 349 2010-11-03 13:01:09Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/designer/subwindowplugin.py $
#
##############################################################################

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtDesigner import QDesignerCustomWidgetInterface

import sys
import os

_DataListPluginFile_ = __file__
if _DataListPluginFile_[-4:] == '.pyc':
	_DataListPluginFile_ = _DataListPluginFile_[:-1]
_DataListPluginPath_ = os.path.dirname(os.path.realpath(_DataListPluginFile_))
sys.path.append(os.path.abspath(os.path.join(_DataListPluginPath_, '..')))

from widgets.subwindow import SubWindow

class SubWindowPlugin(QDesignerCustomWidgetInterface):
	def __init__(self, parent=None):
		QDesignerCustomWidgetInterface.__init__(self, parent)
		self._initialized = False

	def initialize(self, formEditor):
		if self._initialized:
			return
		self._initialized = True

	def isInitialized(self):
		return self._initialized

	def createWidget(self, parent):
		return SubWindow(parent)

	def name(self):
		return "SubWindow"

	def group(self):
		return "Trustserver Widgets"

	def icon(self):
		return QtGui.QIcon()

	def toolTip(self):
		return "Base de ventana de la aplicación"

	def whatsThis(self):
		return "Base de ventana de la aplicación"

	def isContainer(self):
		return True

	def domXml(self):
		return ""

	def includeFile(self):
		return "<widgets/subwindow.h>"


