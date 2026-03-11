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
# $Id: datodlg.py 198 2010-04-13 15:39:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/datodlg.py $
#
##############################################################################

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import *
from ..modelo import *
from .ui import Ui_datodlg
from ts import DataDialog

class DatoDlg (DataDialog, Ui_datodlg.Ui_DatoDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.model=dataModel
		self.app = QApplication.instance()
		# combobox de clasificacion
		self.modelCbCls = clasificacion.Clasificacion(parent, self.app.work)
		self.modelCbCls.select()
		parent.putCombobox(self.clasificacion, self.modelCbCls, 'codigo')

	def putData(self, r):
		self.nombre.setText(str(r.value('nombre') or ""))
		self.descripcion.setText(str(r.value('descripcion') or ""))
		self.unidades.setText(str(r.value('unidades') or ""))
		id = int(r.value('idclasificacion') or 0)
		n=self.clasificacion.findData(id)
		self.clasificacion.setCurrentIndex(n)
		return True

	def getData(self, r):
		if self.nombre.text().strip() == "":
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		r.setValue('nombre', self.nombre.text().strip())
		r.setValue('descripcion', self.descripcion.toPlainText().strip())
		if self.unidades.text().strip() == "":
			self.setEditionError(self.tr("Las unidades no puede estar vacío"))
			return False
		r.setValue('unidades', self.unidades.text().strip())
		i_combo=self.clasificacion.currentIndex()
		id=self.clasificacion.itemData(i_combo)
		r.setValue('idclasificacion', id)
		return True
