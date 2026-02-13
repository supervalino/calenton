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
# $Id: datalistplugin.py 59 2010-01-18 17:28:55Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/designer/datalistplugin.py $
#
##############################################################################

from PyQt4 import QtCore, QtGui, QtDesigner

import sys
import os

_DataListPluginFile_ = __file__
if _DataListPluginFile_[-4:] == '.pyc':
	_DataListPluginFile_ = _DataListPluginFile_[:-1]
_DataListPluginPath_ = os.path.dirname(os.path.realpath(_DataListPluginFile_))
sys.path.append(os.path.abspath(os.path.join(_DataListPluginPath_, '..')))

from widgets.datalist import DataList

class DataListPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):
	def __init__(self, parent=None):
		QtDesigner.QPyDesignerCustomWidgetPlugin.__init__(self, parent)
		self._initialized = False
		
	def initialize(self, formEditor):
		if self._initialized:
			return
		self._initialized = True

	def isInitialized(self):
		return self._initialized

	def createWidget(self, parent):
		return DataList(parent)

	def name(self):
		return "DataList"

	def group(self):
		return "Trustserver Widgets"

	def icon(self):
		return QtGui.QIcon()

	def toolTip(self):
		return "Diálogo de lista de datos"

	def whatsThis(self):
		return "Diálogo de lista de datos" 

	def isContainer(self):
		return True

	def domXml(self):
		return QtCore.QString()

	def includeFile(self):
		return "<widgets/datalist.h>"


