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
# $Id: mapdatocontaminanteaforodlg.py 113 2010-02-17 12:28:57Z picazo $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/mapdatocontaminanteaforodlg.py $
#
##############################################################################

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from ..modelo import *
from .ui import Ui_mapdatocontaminanteaforodlg
from ts import DataDialog

class MapDatoContaminanteAforoDlg (DataDialog, Ui_mapdatocontaminanteaforodlg.Ui_MapDatoContaminanteAforoDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.model=dataModel
		self.app = QApplication.instance()
		# combobox de datos
		self.modelCbDat = dato.Dato(parent, self.app.work)
		self.modelCbDat.select()
		parent.putCombobox(self.dato, self.modelCbDat, 'nombre')
		# combobox de clasificacion
		self.modelCbCls = clasificacion.Clasificacion(parent, self.app.work)
		self.modelCbCls.select()
		parent.putCombobox(self.clasificacion, self.modelCbCls, 'codigo')
		# combobox de aforo
		self.modelCbAfo = aforo.Aforo(parent, self.app.work)
		self.modelCbAfo.select()
		parent.putCombobox(self.aforo, self.modelCbAfo, 'nombre')
		# combobox de contaminante
		self.modelCbCnt = contaminante.Contaminante(parent, self.app.work)
		self.modelCbCnt.select()
		parent.putCombobox(self.contaminante, self.modelCbCnt, 'nombre')

	def putData(self, r):
		self.factor.setText(str(r.value('p') or ""))
		id = int(r.value('idaforo') or 0)
		n=self.aforo.findData(id)
		self.aforo.setCurrentIndex(n)
		id = int(r.value('iddato') or 0)
		n=self.dato.findData(id)
		self.dato.setCurrentIndex(n)
		id = int(r.value('idclasificacion') or 0)
		n=self.clasificacion.findData(id)
		self.clasificacion.setCurrentIndex(n)
		id = int(r.value('idcontaminante') or 0)
		n=self.contaminante.findData(id)
		self.contaminante.setCurrentIndex(n)
		return True

	def getData(self, r):
		if self.p.text().strip() == "":
			self.setEditionError(self.tr("El factor no puede estar vacío"))
			return False
		r.setValue('p', self.p.text().strip())
		i_combo=self.aforo.currentIndex()
		id=self.aforo.itemData(i_combo)
		r.setValue('idaforo', id)
		i_combo=self.clasificacion.currentIndex()
		id=self.clasificacion.itemData(i_combo)
		r.setValue('idclasificacion', id)
		i_combo=self.dato.currentIndex()
		id=self.dato.itemData(i_combo)
		r.setValue('iddato', id)
		i_combo=self.contaminante.currentIndex()
		id=self.contaminante.itemData(i_combo)
		r.setValue('idcontaminante', id)
		return True
