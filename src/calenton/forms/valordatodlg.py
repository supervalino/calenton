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
# $Id: valordatodlg.py 292 2010-06-04 10:51:00Z picazo $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/valordatodlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from modelo import *
from ui import Ui_valordatodlg
from ts import DataDialog

class ValorDatoDlg (DataDialog, Ui_valordatodlg.Ui_ValorDatoDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.model=dataModel
		self.app = QApplication.instance()
		self.clasificacion.currentIndexChanged.connect(self.clasificacion_currentIndexChanged)
		# combobox de aforos
		self.modelCbAfo = aforo.Aforo(parent, self.app.work)
		self.modelCbAfo.select()
		parent.putCombobox(self.aforo, self.modelCbAfo, 'nombre')
		# combobox de clasificacion
		self.modelCbCls = clasificacion.Clasificacion(parent, self.app.work)
		self.modelCbCls.select()
		parent.putCombobox(self.clasificacion, self.modelCbCls, 'codigo')
		# combobox de dato
		self.modelCbDat = dato.Dato(parent, self.app.work)
		self.modelCbDat.select()
		parent.putCombobox(self.dato, self.modelCbDat, 'nombre')
		
	def putData(self, r):
		self.valor.setText(r.value('valor').toString())
		(id, good)=r.value('idaforo').toInt()
		n=self.aforo.findData(id)
		self.aforo.setCurrentIndex(n)
		(id, good)=r.value('iddato').toInt()
		n=self.dato.findData(id)
		self.dato.setCurrentIndex(n)
		(id, good)=r.value('idclasificacion').toInt()
		n=self.clasificacion.findData(id)
		self.clasificacion.setCurrentIndex(n)
		return True
		
	def getData(self, r):
		if self.valor.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El valor no puede estar vacío"))
			return False
		r.setValue('valor', self.valor.text().trimmed())
		i_combo=self.aforo.currentIndex()
		id=self.aforo.itemData(i_combo)
		r.setValue('idaforo', id)
		i_combo=self.clasificacion.currentIndex()
		id=self.clasificacion.itemData(i_combo)
		r.setValue('idclasificacion', id)
		i_combo=self.dato.currentIndex()
		id=self.dato.itemData(i_combo)
		r.setValue('iddato', id)
		return True
		
	@pyqtSlot("int")
	def clasificacion_currentIndexChanged(self, i_combo):
		if i_combo==0:
			return
		id=self.clasificacion.itemData(i_combo).toInt()[0]
		filtro="id = %d" % (id)
		self.modelCbDat.setFilter(filtro)
		
