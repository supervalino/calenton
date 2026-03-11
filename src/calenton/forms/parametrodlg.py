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

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtSql import *
from ..modelo import *
from .ui import Ui_parametrodlg
from ts import DataDialog
from ..widgets.datalist import DataList
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
		self.nombre.setText(str(r.value('nombre') or ""))
		id_escenario = int(r.value('idescenario') or 0)
		n=self.escenario.findData(id_escenario)
		self.escenario.setCurrentIndex(n)
		self.valor.setText(str(r.value('valor') or ""))
		self.descripcion.setText(str(r.value('descripcion') or ""))
		return True

	def getData(self, r):
		if self.nombre.text().strip() == "":
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		r.setValue('nombre', self.nombre.text().strip())
		i_combo=self.escenario.currentIndex()
		id_escenario=self.escenario.itemData(i_combo)
		r.setValue('idescenario', id_escenario)
		if self.valor.text().strip() == "":
			self.setEditionError(self.tr("El valor no puede estar vacío"))
			return False
		r.setValue('valor', self.valor.text().strip())
		r.setValue('descripcion', self.descripcion.toPlainText().strip())
		return True
