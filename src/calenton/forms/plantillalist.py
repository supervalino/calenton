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
# $Id: plantillalist.py 128 2010-03-10 18:37:20Z picazo $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/plantillalist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from .ui.Ui_plantillalist import *
from ..widgets.datalist import DataList
from configobj import ConfigObj

class PlantillaList (DataList, Ui_PlantillaListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		app = QApplication.instance()

	@pyqtSlot(bool)
	def on_nueva_clicked(self, checked):
		fileName = QFileDialog.getOpenFileName(self,self.tr("Abrir Plantilla"), "reports", self.tr("Config Files .dat (*.dat)"))
		lista = fileName.split("/")
		nombrePlantilla = lista[len(lista)-1]
		self.plantilla.setText(nombrePlantilla)
		nombreDat=self.dirGrap.filePath(fileName)
		config = ConfigObj(str(nombreDat), encoding='UTF8')
		self.descripcion.setText(config['descripcion'])
