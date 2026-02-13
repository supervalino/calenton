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
# $Id: parametrodlg.py 198 2010-04-13 15:39:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/parametrodlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from modelo import *
from ui import Ui_parametrodlg
from ts import DataDialog
from widgets.datalist import DataList

class ParametroDlg (DataDialog, Ui_parametrodlg.Ui_ParametroDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.model=dataModel
		self.app = QApplication.instance()
		# combobox de escenarios
		self.modelCb = escenario.Escenario(parent, self.app.work)
		self.modelCb.select()
		parent.putCombobox(self.escenario, self.modelCb, 'nombre')
	
	def putData(self, r):
		self.nombre.setText(r.value('nombre').toString())
		(id_escenario, good)=r.value('idescenario').toInt()
		n=self.escenario.findData(id_escenario)
		self.escenario.setCurrentIndex(n)
		self.valor.setText(r.value('valor').toString())
		self.descripcion.setText(r.value('descripcion').toString())
		return True
		
	def getData(self, r):
		if self.nombre.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		r.setValue('nombre', self.nombre.text().trimmed())
		i_combo=self.escenario.currentIndex()
		id_escenario=self.escenario.itemData(i_combo)
		r.setValue('idescenario', id_escenario)
		if self.valor.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El valor no puede estar vacío"))
			return False
		r.setValue('valor', self.valor.text().trimmed())
		r.setValue('descripcion', self.descripcion.toPlainText().trimmed())
		return True
