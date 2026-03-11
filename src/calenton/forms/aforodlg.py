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
# $Id: aforodlg.py 198 2010-04-13 15:39:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/aforodlg.py $
#
##############################################################################

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from ..modelo import *
from .ui import Ui_aforodlg
from ts import DataDialog, ComboDataModel

class AforoDlg (DataDialog, Ui_aforodlg.Ui_AforoDlgClass):
	def __init__(self, parent, dataModel, idEscenario, idFuenteDfl):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.model=dataModel
		self.app = QApplication.instance()
		self.db = self.app.workDb()
		self.idEscenario = idEscenario
		self.idFuenteDfl = idFuenteDfl
		# combobox de fuentes
		self.modelCbFte = ComboDataModel(self)
		self.modelCbFte.setQuery("select id, nombre from fuente where idescenario = %d" % (idEscenario), self.db)
		self.fuente.setModel(self.modelCbFte)
		self.fuente.setCurrentItemData(self.idFuenteDfl)

		self.modelNivelZona = ComboDataModel(self, True, self.tr('No asociado'))
		self.modelNivelZona.setQuery("select id, nombre from nivelzona order by nombre", self.db)
		self.nivelZona.setModel(self.modelNivelZona)

		self.modelZona = ComboDataModel(self, True, self.tr('No asociado'))
		self.modelZona = self.model.foreignKey('idzona').model(
						{ 'idnivelzona': -1 },
						True,
						self.tr('No asociado'))
		self.zona.setModel(self.modelZona)

		self.modelTipoDato = ComboDataModel(self, True, self.tr('Sin distribución automática'))
		self.modelTipoDato = self.model.foreignKey('idtipodatozona').model(
						{'idescenario': -1},
						True,
						self.tr('Sin distribución automática'))
		self.tipoDatoZona.setModel(self.modelTipoDato)

	def putData(self, r):
		self.nombre.setText(str(r.value('nombre') or ""))
		self.escala.setText(str(r.value('escala') or ""))
		self.descripcion.setText(str(r.value('descripcion') or ""))
		if r.value('idfuente') is not None:
			self.fuente.setCurrentItemData(r.value('idfuente'))
		else:
			self.fuente.setCurrentItemData(self.idFuenteDfl)

		self.idNivelZona = self.model.getIdNivelZona(int(r.value('idzona') or 0))
		self.idEscenario = self.model.getIdEscenario(int(r.value('idfuente') or 0))
		self.modelTipoDato.setFilters({ 'idescenario': self.idEscenario })
		self.modelZona.setFilters({ 'idnivelzona': self.idNivelZona })

		self.nivelZona.setCurrentItemData(self.idNivelZona)
		self.zona.setCurrentItemData(r.value('idzona'))
		self.tipoDatoZona.setCurrentItemData(r.value('idtipodatozona'))

		return True

	def getData(self, r):
		if self.nombre.text().strip() == "":
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		r.setValue('nombre', self.nombre.text().strip())
		r.setValue('descripcion', self.descripcion.toPlainText().strip())
		if self.escala.text().strip() == "":
			self.setEditionError(self.tr("La escala no puede estar vacía"))
			return False
		r.setValue('escala', self.escala.text().strip())
		r.setValue('idfuente', self.fuente.currentItemData())

		r.setValue('idzona', self.zona.currentItemData())
		r.setValue('idtipodatozona', self.tipoDatoZona.currentItemData())
		return True

	@pyqtSlot(int)
	def on_fuente_activated(self, index):
		idfuente = int(self.fuente.currentItemData() or 0)
		if not idfuente:
			return
		idescenario = self.aforo.getIdEscenario(idfuente)
		itdz = self.tipoDatoZona.currentItemData()
		self.modelTipoDato.setFilters({ 'idescenario': idescenario })
		self.tipoDatoZona.setCurrentItemData(itdz)

	@pyqtSlot(int)
	def on_nivelZona_activated(self, index):
		inz = self.nivelZona.currentItemData()
		if inz is None:
			idnivelzona = -1
		else:
			idnivelzona = int(inz or 0)
			if not idnivelzona:
				idnivelzona = -1
		self.zona.setEnabled(idnivelzona != -1)
		iz = self.zona.currentItemData()
		self.modelZona.setFilters({ 'idnivelzona': idnivelzona })
		self.zona.setCurrentItemData(iz)


