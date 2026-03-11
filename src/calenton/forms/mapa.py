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
# $Id: mapa.py 363 2010-12-01 18:30:27Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/mapa.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtSql import *
from qgis.gui import *
from qgis.core import *
from .ui.Ui_mapa import *
from ..widgets.subwindow import SubWindow
from ..calculo import mapas
class Mapa (SubWindow, Ui_MapaClass):
	def __init__(self, sql, idNivelZona, color = None, parent = None):
		QWidget.__init__(self, parent)
		self.setupUi(self)
		self.mapa.setCanvasColor(Qt.white)
		self.mapa.enableAntiAliasing(True)
		self.app = QApplication.instance()
		self.layer = self.app.mapas.layerConfigurada(sql, "base", idNivelZona, color)
		self.legend = mapas.Legend(self.layer)
		self.mapa.renderComplete.connect(self.renderLegend)
		self.mapa.setExtent(self.layer.layer.extent())
		self.mapa.setLayerSet([ QgsMapCanvasLayer(self.layer.layer) ])

	def canPrint(self):
		return True

	def closeEvent(self, evt):
		self.mapa.setLayerSet([])
		self.legend = None
		self.app.mapas.eliminaLayer(self.layer)
		self.layer = None
		evt.accept()

	@pyqtSlot("QPainter *")
	def renderLegend(self, painter):
		if self.legend is not None:
			self.legend.paint(painter)
