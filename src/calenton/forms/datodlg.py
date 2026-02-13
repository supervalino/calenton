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

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from modelo import *
from ui import Ui_datodlg
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
		self.nombre.setText(r.value('nombre').toString())
		self.descripcion.setText(r.value('descripcion').toString())
		self.unidades.setText(r.value('unidades').toString())
		(id, good)=r.value('idclasificacion').toInt()
		n=self.clasificacion.findData(id)
		self.clasificacion.setCurrentIndex(n)
		return True
		
	def getData(self, r):
		if self.nombre.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		r.setValue('nombre', self.nombre.text().trimmed())
		r.setValue('descripcion', self.descripcion.toPlainText().trimmed())
		if self.unidades.text().trimmed().isEmpty():
			self.setEditionError(self.tr("Las unidades no puede estar vacío"))
			return False
		r.setValue('unidades', self.unidades.text().trimmed())
		i_combo=self.clasificacion.currentIndex()
		id=self.clasificacion.itemData(i_combo)
		r.setValue('idclasificacion', id)
		return True
