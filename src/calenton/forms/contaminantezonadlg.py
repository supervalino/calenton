#!/usr/bin/python
#-*- coding: utf-8 -*-
##############################################################################
#
# CALENTON
# Programa de procesamiento y generación de informes para datos de emisión
# de contaminantes
#
# (C) LITEC, 2009
# (C) Trustserver SL, 2009
# Todos los derechos reservados
#
# $Id: contaminantezonadlg.py 198 2010-04-13 15:39:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/contaminantezonadlg.py $
#
##############################################################################

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import *
from ..modelo import *
from .ui import Ui_contaminantezonadlg
from ts import DataDialog

class ContaminanteZonaDlg (DataDialog, Ui_contaminantezonadlg.Ui_ContaminanteZonaDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.model=dataModel
		self.app = QApplication.instance()
		# combobox de contaminante
		self.modelCbCnt = contaminante.Contaminante(parent, self.app.work)
		self.modelCbCnt.select()
		parent.putCombobox(self.contaminante, self.modelCbCnt, 'nombre')
		# combobox de fuentes
		self.modelCbFte = fuente.Fuente(parent, self.app.work)
		self.modelCbFte.select()
		parent.putCombobox(self.fuente, self.modelCbFte, 'nombre')
		# combobox de clasificacion
		self.modelCbCls = clasificacion.Clasificacion(parent, self.app.work)
		self.modelCbCls.select()
		parent.putCombobox(self.clasificacion, self.modelCbCls, 'codigo')

	def putData(self, r):
		self.valor.setText(str(r.value('valor') or ""))
		id = int(r.value('idcontaminante') or 0)
		n=self.contaminante.findData(id)
		self.contaminante.setCurrentIndex(n)
		id = int(r.value('idfuente') or 0)
		n=self.fuente.findData(id)
		self.fuente.setCurrentIndex(n)
		id = int(r.value('idclasificacion') or 0)
		n=self.clasificacion.findData(id)
		self.clasificacion.setCurrentIndex(n)
		return True

	def getData(self, r):
		if self.valor.text().strip() == "":
			self.setEditionError(self.tr("El valor no puede estar vacío"))
			return False
		r.setValue('valor', self.valor.text().strip())
		i_combo=self.contaminante.currentIndex()
		id=self.contaminante.itemData(i_combo)
		r.setValue('idcontaminante', id)
		i_combo=self.fuente.currentIndex()
		id=self.fuente.itemData(i_combo)
		r.setValue('idfuente', id)
		i_combo=self.clasificacion.currentIndex()
		id=self.clasificacion.itemData(i_combo)
		r.setValue('idclasificacion', id)
		return True
