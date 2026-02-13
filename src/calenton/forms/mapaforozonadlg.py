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
# $Id: mapaforozonadlg.py 198 2010-04-13 15:39:47Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/mapaforozonadlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from modelo import *
from ui import Ui_mapaforozonadlg
from ts import DataDialog

class MapAforoZonaDlg (DataDialog, Ui_mapaforozonadlg.Ui_MapAforoZonaDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.model=dataModel
		self.app = QApplication.instance()
		# combobox de aforos
		self.modelCbAfo = aforo.Aforo(parent, self.app.work)
		self.modelCbAfo.select()
		parent.putCombobox(self.aforo, self.modelCbAfo, 'nombre')
		# combobox de zona
		self.modelCbZna = zona.Zona(parent, self.app.work)
		self.modelCbZna.select()
		parent.putCombobox(self.zona, self.modelCbZna, 'nombre')
		
	def putData(self, r):
		self.p.setText(r.value('p').toString())
		(id, good)=r.value('idaforo').toInt()
		n=self.aforo.findData(id)
		self.aforo.setCurrentIndex(n)
		(id, good)=r.value('idzona').toInt()
		n=self.zona.findData(id)
		self.zona.setCurrentIndex(n)
		return True
		
	def getData(self, r):
		if self.p.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El valor no puede estar vacío"))
			return False
		r.setValue('p', self.p.text().trimmed())
		i_combo=self.aforo.currentIndex()
		id=self.aforo.itemData(i_combo)
		r.setValue('idaforo', id)
		i_combo=self.zona.currentIndex()
		id=self.zona.itemData(i_combo)
		r.setValue('idzona', id)
		return True
