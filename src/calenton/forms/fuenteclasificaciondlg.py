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
# $Id: fuenteclasificaciondlg.py 59 2010-01-18 17:28:55Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/fuenteclasificaciondlg.py $
#
##############################################################################

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import *
from ..modelo import *
from .ui import Ui_fuenteclasificaciondlg
from ts import DataDialog

class FuenteClasificacionDlg (DataDialog, Ui_fuenteclasificaciondlg.Ui_FuenteClasificacionDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.model=dataModel
		self.app = QApplication.instance()
		# combobox
#		self.escenario.addItems(self.model.lEscenarios())
#		self.origen.addItems(self.model.lOrigenes())
#		self.motorcalculo.addItems(self.model.lMotorCalculos())
		# combobox de fuente
		self.modelCbFnt = fuente.Fuente(parent, self.app.work)
		self.modelCbFnt.select()
		parent.putCombobox(self.fuente, self.modelCbFnt, 'nombre')
		# combobox de clasificacion
		self.modelCbCls = clasificacion.Clasificacion(parent, self.app.work)
		self.modelCbCls.select()
		parent.putCombobox(self.clasificacion, self.modelCbCls, 'codigo', 'descripcion')

	def putData(self, r):
		self.nombre.setText(str(r.value('nombre') or ""))
		id = int(r.value('idfuente') or 0)
		n=self.fuente.findData(id)
		self.fuente.setCurrentIndex(n)
		id = int(r.value('idclasificacion') or 0)
		n=self.clasificacion.findData(id)
		self.clasificacion.setCurrentIndex(n)

		return True

	def getData(self, r):
#		if self.nombre.text().strip() == "":
#			self.setEditionError(self.tr("El nombre no puede estar vacío"))
#			return False
#		r.setValue('nombre', self.nombre.text().strip())
		i_combo=self.fuente.currentIndex()
		id=self.fuente.itemData(i_combo)
		r.setValue('idfuente', id)
		i_combo=self.clasificacion.currentIndex()
		id=self.clasificacion.itemData(i_combo)
		r.setValue('idclasificacion', id)
		return True
