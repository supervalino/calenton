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
# $Id: contaminantelist.py 191 2010-04-09 11:55:34Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/contaminantelist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from .ui.Ui_contaminantelist import *
from ts import TSqlTableNavigator

class ContaminanteList (DataList, Ui_ContaminanteListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		app = QApplication.instance()
		if not app.databaseInit:
			return
		self.model = app.mContaminante
		self.nav.setModel(self.model)
		self.nav.tableView().hideColumn(self.model.fieldIndex("id"))
		self.cambiaEncabezado(self.model, ['Contaminante', 'Descripción', 'Unidades'])


