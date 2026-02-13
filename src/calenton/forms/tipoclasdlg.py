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
# $Id: tipoclasdlg.py 74 2010-01-21 18:06:05Z picazo $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/tipoclasdlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from modelo import *
from ui import Ui_tipoclasdlg
from ui.Ui_tipoclasdlg import *
from ts import DataDialog

class TipoClasDlg (DataDialog, Ui_TipoclasDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		
	def putData(self, r):
		self.nombre.setText(r.value('nombre').toString())
		self.descripcion.setText(r.value('descripcion').toString())
		return True
		
	def getData(self, r):
		if self.nombre.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		r.setValue('nombre', self.nombre.text().trimmed())
		r.setValue('descripcion', self.descripcion.toPlainText().trimmed())
		return True
