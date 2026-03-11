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

from PyQt6 import QtWidgets, QtCore
from .ui import Ui_tipodatozonadlg
from ts import DataDialog

class TipoDatoZonaDlg (DataDialog, Ui_tipodatozonadlg.Ui_TipoDatoZonaDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		fk = dataModel.foreignKey(dataModel.fieldIndex('idescenario'))
		self.modelCombo = fk.model({})
		self.escenario.setModel(self.modelCombo)

	def putData(self, r):
		self.nombre.setText(str(r.value('nombre') or ""))
		self.unidades.setText(str(r.value('unidades') or ""))
		idescenario = r.value('idescenario')
		if idescenario is not None:
			try:
				self.escenario.setCurrentItemData(int(idescenario))
			except (ValueError, TypeError):
				pass
		self.variable.setText(str(r.value('variable') or ""))
		self.defecto.setText(str(r.value('valor_defecto') or ""))
		return True

	def getData(self, r):
		if self.nombre.text().strip() == "":
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		if self.unidades.text().strip() == "":
			self.setEditionError(self.tr("El campo unidades no puede estar vacío"))
			return False
		if self.variable.text().strip() == "":
			self.setEditionError(self.tr("El campo 'Variable JavaScript' no puede estar vacío"))
			return False
		d = self.defecto.text().strip()
		try:
			d2 = float(d)
		except (ValueError, TypeError):
			self.setEditionError(self.tr("El campo valor por defecto no es correcto"))
			return False
		if d == "":
			self.setEditionError(self.tr("El campo valor por defecto no es correcto"))
			return False
		r.setValue('nombre', self.nombre.text().strip())
		r.setValue('unidades', self.unidades.text().strip())
		idescenario_raw = self.escenario.currentItemData()
		if idescenario_raw is not None:
			try:
				idescenario = int(idescenario_raw)
			except (ValueError, TypeError):
				idescenario = -1
		else:
			idescenario = -1
		r.setValue('idescenario', idescenario)
		r.setValue('valor_defecto', d2)
		r.setValue('variable', self.variable.text().strip())
		return True
