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
# $Id: zonadlg.py 59 2010-01-18 17:28:55Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/zonadlg.py $
#
##############################################################################

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_zonadlg import *
from ts import DataDialog
from ..widgets.datalist import DataList
class ZonaDlg (DataDialog, Ui_ZonaDialogClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.app = QApplication.instance()
		self.dialogoPadre=parent
		self.model=dataModel
		# combobox de zonas
		self.zonapadre.addItems(self.model.lZonas())
		# combobox de niveles
		self.nivel.addItems(self.app.mNivelZonas.lNivelesZona())

	def putData(self, r):
		self.modelRelZonas = self.app.mRelZonas
		self.modelmapperRelZonas = self.app.mMapperRelZonas # Copia del modelo relzonas para filtrarlo con un registro concreto
		self.nombre.setText(str(r.value('nombre') or ""))
		self.id = int(r.value('id') or 0)
		indice = int(r.value('idnivelzona') or 0)
		self.nivel.setCurrentIndex(indice-1)
		# lista de padres
		self.filtraZonasPadre()
		self.mapper = QDataWidgetMapper(self)
		self.mapper.setSubmitPolicy(QDataWidgetMapper.SubmitPolicy.ManualSubmit)
		self.mapper.setModel(self.modelmapperRelZonas)
		self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
		self.listapadres.setModel(self.modelmapperRelZonas)
		self.mapper.addMapping(self.listapadres, 0)
		return True

	def getData(self, r):
		if self.nombre.text().strip() == "":
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		r.setValue('nombre', self.nombre.text().strip())
		return True

	def filtraZonasPadre(self):
		query = QSqlQuery(self.model.database())
		query.exec("select zona.nombre,relzona.id from zona,relzona where zona.id=relzona.idzonapadre and relzona.idzona= %d" % self.id)
		self.modelmapperRelZonas.setQuery(query)


	@pyqtSlot(bool)
	def on_asignapadre_clicked(self, checked):
		i_sel=self.zonapadre.currentIndex()
		r=self.modelRelZonas.record(0) # registro para plantilla
		id_zonapadre = int(self.model.record(i_sel).value('id') or 0)
		r.setNull('id')
		self.modelRelZonas.calcSeq(r)
		r.setValue('idzona', self.id)
		r.setValue('idzonapadre', id_zonapadre)
		self.dialogoPadre.askAndAddRow(r, self.modelRelZonas)
		self.filtraZonasPadre()
		return True

	@pyqtSlot(bool)
	def on_borrapadre_clicked(self, checked):
		self.dialogoPadre.askAndRemoveRows(self.listapadres, self.modelmapperRelZonas)
		self.filtraZonasPadre()
