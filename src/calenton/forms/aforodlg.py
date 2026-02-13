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

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from modelo import *
from ui import Ui_aforodlg
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
		self.fuente.setCurrentItemData(QVariant(self.idFuenteDfl))
		
		self.modelNivelZona = ComboDataModel(self, True, self.tr('No asociado'))
		self.modelNivelZona.setQuery("select id, nombre from nivelzona order by nombre", self.db)
		self.nivelZona.setModel(self.modelNivelZona)
		
		self.modelZona = ComboDataModel(self, True, self.tr('No asociado'))
		self.modelZona = self.model.foreignKey('idzona').model(
							{ 'idnivelzona': QVariant(-1) },
							True,
							self.tr('No asociado'))
		self.zona.setModel(self.modelZona)
		
		self.modelTipoDato = ComboDataModel(self, True, self.tr('Sin distribución automática'))
		self.modelTipoDato = self.model.foreignKey('idtipodatozona').model(
							{'idescenario': QVariant(-1)}, 
							True, 
							self.tr('Sin distribución automática'))
		self.tipoDatoZona.setModel(self.modelTipoDato)
		
	def putData(self, r):
		self.nombre.setText(r.value('nombre').toString())
		self.escala.setText(r.value('escala').toString())
		self.descripcion.setText(r.value('descripcion').toString())
		if r.value('idfuente').isValid():
			self.fuente.setCurrentItemData(r.value('idfuente'))
		else:
			self.fuente.setCurrentItemData(QVariant(self.idFuenteDfl))
		
		self.idNivelZona = self.model.getIdNivelZona(r.value('idzona').toInt()[0])
		self.idEscenario = self.model.getIdEscenario(r.value('idfuente').toInt()[0])
		self.modelTipoDato.setFilters({ 'idescenario': QVariant(self.idEscenario) })
		self.modelZona.setFilters({ 'idnivelzona': QVariant(self.idNivelZona) })
		
		self.nivelZona.setCurrentItemData(QVariant(self.idNivelZona))
		self.zona.setCurrentItemData(r.value('idzona'))
		self.tipoDatoZona.setCurrentItemData(r.value('idtipodatozona'))
		
		return True
		
	def getData(self, r):
		if self.nombre.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		r.setValue('nombre', self.nombre.text().trimmed())
		r.setValue('descripcion', self.descripcion.toPlainText().trimmed())
		if self.escala.text().trimmed().isEmpty():
			self.setEditionError(self.tr("La escala no puede estar vacía"))
			return False
		r.setValue('escala', self.escala.text().trimmed())
		r.setValue('idfuente', self.fuente.currentItemData())
		
		r.setValue('idzona', self.zona.currentItemData())
		r.setValue('idtipodatozona', self.tipoDatoZona.currentItemData())
		return True
		
	@pyqtSlot("int")
	def on_fuente_activated(self, index):
		(idfuente, good) = self.fuente.currentItemData().toInt()
		if not good:
			return
		idescenario = self.aforo.getIdEscenario(idfuente)
		itdz = self.tipoDatoZona.currentItemData()
		self.modelTipoDato.setFilters({ 'idescenario': idescenario })
		self.tipoDatoZona.setCurrentItemData(itdz)
		
	@pyqtSlot("int")
	def on_nivelZona_activated(self, index):
		inz = self.nivelZona.currentItemData()
		if not inz.isValid() or inz.isNull():
			idnivelzona = -1
		else:
			(idnivelzona, good) = inz.toInt()
			if not good:
				idnivelzona = -1
		self.zona.setEnabled(idnivelzona != -1)
		iz = self.zona.currentItemData()
		self.modelZona.setFilters({ 'idnivelzona': idnivelzona })
		self.zona.setCurrentItemData(iz)


