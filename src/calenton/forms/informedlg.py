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
# $Id: informedlg.py 348 2010-11-02 12:53:05Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/informedlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui import Ui_informedlg
import shutil

class InformeDlg (QDialog, Ui_informedlg.Ui_InformeDlgClass):
	def __init__(self, parent):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.addAction(self.actionCopiar)
		self.addAction(self.actionSelectAll)
		self.calc = None
		
	@pyqtSlot("bool")
	def on_busca_clicked(self, checked):
		txt = self.texto.text().trimmed()
		print txt.size(), unicode(txt)
		r = self.informe.find(txt)
		if not r:
			return
		c = self.informe.textCursor()
		c.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, txt.size())
		self.informe.setTextCursor(c)
		
	@pyqtSlot("QAbstractButton *")
	def on_buttonBox_clicked(self, button):
		sb = self.buttonBox.standardButton(button)
		if sb == QDialogButtonBox.Save:
			self.guarda()
		elif sb == QDialogButtonBox.Ok:
			self.accept()
			
	def setCalc(self, calc):
		self.calc = calc
		self.informe.setPlainText(calc.getInforme())
	
	def guarda(self):
		if self.calc is None:
			return
		fileName = QFileDialog.getSaveFileName(self, self.tr("Guardar informe..."), QString(), "*.txt")
		if not fileName.isEmpty():
			self.calc.guardaInforme(fileName)
	
