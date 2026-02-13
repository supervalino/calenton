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
# $Id: contaminantedlg.py 59 2010-01-18 17:28:55Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/contaminantedlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from ui.Ui_contaminantedlg import *
from ts import DataDialog

class ContaminanteDlg (DataDialog, Ui_ContaminanteDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		
	def putData(self, r):
		self.nombre.setText(r.value('nombre').toString())
		self.descripcion.setText(r.value('descripcion').toString())
		self.unidades.setText(r.value('unidades').toString())
		return True
		
	def getData(self, r):
		if self.nombre.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		if self.unidades.text().trimmed().isEmpty():
			self.setEditionError(self.tr("Las unidades no pueden estar vacías"))
			return False
		r.setValue('nombre', self.nombre.text().trimmed())
		r.setValue('unidades', self.unidades.text().trimmed())
		r.setValue('descripcion', self.descripcion.toPlainText().trimmed())
		return True
