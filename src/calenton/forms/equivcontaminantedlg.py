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
# $Id: equivcontaminantedlg.py 113 2010-02-17 12:28:57Z picazo $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/equivcontaminantedlg.py $
#
##############################################################################

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import *
from ..modelo import *
from .ui import Ui_equivcontaminantedlg
from ts import DataDialog

class EquivContaminanteDlg (DataDialog, Ui_equivcontaminantedlg.Ui_EquivContaminanteDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.model=dataModel
		self.app = QApplication.instance()
		# combobox de escenarios
		self.modelCbEsc = escenario.Escenario(parent, self.app.work)
		self.modelCbEsc.select()
		parent.putCombobox(self.escenario, self.modelCbEsc, 'nombre')
		# combobox de contaminante
		self.modelCbCnt = contaminante.Contaminante(parent, self.app.work)
		self.modelCbCnt.select()
		parent.putCombobox(self.contaminante, self.modelCbCnt, 'nombre')

	def putData(self, r):
		self.p.setText(str(r.value('p') or ""))
		id = int(r.value('idescenario') or 0)
		n=self.escenario.findData(id)
		self.escenario.setCurrentIndex(n)
		id = int(r.value('idcontaminante') or 0)
		n=self.contaminante.findData(id)
		self.contaminante.setCurrentIndex(n)

		return True

	def getData(self, r):
		if self.p.text().strip() == "":
			self.setEditionError(self.tr("El valor no puede estar vacío"))
			return False
		r.setValue('p', self.p.text().strip())
		i_combo=self.escenario.currentIndex()
		id=self.escenario.itemData(i_combo)
		r.setValue('idescenario', id)
		i_combo=self.contaminante.currentIndex()
		id=self.contaminante.itemData(i_combo)
		r.setValue('idcontaminante', id)
		return True
