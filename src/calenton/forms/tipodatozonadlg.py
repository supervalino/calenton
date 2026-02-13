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
# $Id: tipodatozonadlg.py 150 2010-03-26 01:20:19Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/tipodatozonadlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QVariant
from ui import Ui_tipodatozonadlg
from ts import DataDialog

class TipoDatoZonaDlg (DataDialog, Ui_tipodatozonadlg.Ui_TipoDatoZonaDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		fk = dataModel.foreignKey(dataModel.fieldIndex('idescenario'))
		self.modelCombo = fk.model({})
		self.escenario.setModel(self.modelCombo)
		
	def putData(self, r):
		self.nombre.setText(r.value('nombre').toString())
		self.unidades.setText(r.value('unidades').toString())
		(idescenario, good) = r.value('idescenario').toInt()
		if good:
			self.escenario.setCurrentItemData(idescenario)
		self.variable.setText(r.value('variable').toString())
		self.defecto.setText(r.value('valor_defecto').toString())
		return True
		
	def getData(self, r):
		if self.nombre.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		if self.unidades.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El campo unidades no puede estar vacío"))
			return False
		if self.variable.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El campo 'Variable JavaScript' no puede estar vacío"))
			return False
		d = self.defecto.text().trimmed()
		(d2, good) = d.toDouble()
		if d.isEmpty() or not good:
			self.setEditionError(self.tr("El campo valor por defecto no es correcto"))
			return False
		r.setValue('nombre', self.nombre.text().trimmed())
		r.setValue('unidades', self.unidades.text().trimmed())
		(idescenario, good) = self.escenario.currentItemData().toInt()
		r.setValue('idescenario', idescenario)
		r.setValue('valor_defecto', QVariant(d2))
		r.setValue('variable', self.variable.text().trimmed())
		return True

