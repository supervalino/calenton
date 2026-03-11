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
# $Id: reportlist.py 352 2010-11-15 22:59:33Z picazo $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/reportlist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_reportlist import *
from .reportdlg import ReportDlg
from ..widgets.datalist import DataList
#import cairo
#import pycha.bar
#import pycha.stackedbar
#import pycha.pie
#import pycha.line

from configobj import ConfigObj

#
from ts import FKItemDelegate

class ReportList (DataList, Ui_ReportListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		app = QApplication.instance()
		self.tabla.selectionModel().selectionChanged.connect(self.tabla_selectionChanged)
		self.work = QSqlDatabase.database('work')
#		self.cambiosSinGuardar = 0
		self.dirRep = QDir("reports")
		self.s = QSettings()
		self.informeAc.setText(app.informeActivo())
		self.cargaTabla()

	def cargaTabla(self):
		self.dirRep.setNameFilters(["*.dat"])
		self.listaRepF = self.dirRep.entryList()
#		listaGrapD = []
#		listaGrapS = []
		self.nRep = len(self.listaRepF)
		self.tabla.setRowCount(self.nRep)
		self.tabla.setColumnCount(2)
		encabezado = [self.tr("Nombre"), self.tr("Descripción")]
		#[self.tr("Descripción"), self.tr("SQL")]
		self.tabla.setHorizontalHeaderLabels(encabezado)
		if self.nRep==0 :
			return
		for i in range(0,self.nRep):
			nombre=self.listaRepF[i].split(".")[0]
			nombreDat=self.dirRep.filePath(self.listaRepF[i])
			config = ConfigObj(str(nombreDat), encoding='UTF8')
			self.tabla.setItem(i, 0, QTableWidgetItem(nombre))
			self.tabla.setItem(i, 1, QTableWidgetItem(config['descripcion']))
		self.tabla.resizeColumnsToContents()
		self.elimina.setEnabled(False)
		self.activar.setEnabled(False)
		self.edita.setEnabled(False)
		self.crear.setEnabled(False)


	def filasSeleccionadas(self):
		filas = []
		i = -1
		for g in self.tabla.selectedIndexes():
			filas.append(g.row())
		ln = list(dict.fromkeys(filas))
		ln.sort()
		return ln

	@pyqtSlot(bool)
	def on_anade_clicked(self, checked):
		d = ReportDlg(self)
		if d.exec():
			nombre = d.nombre.text().strip()
			if not self.dirRep.exists(nombre):
				if self.dirRep.mkdir(nombre):
					self.escribeDat(d)
				else:
					QMessageBox.warning(None, self.tr("No se puede crear el directorio"),
						self.tr("¿?"),
						QMessageBox.StandardButton.Ok)
			else:
				QMessageBox.warning(None, self.tr("El informe ya existe"),
					self.tr("Tiene que cambiar el nombre"),
					QMessageBox.StandardButton.Ok)
				self.on_anade_clicked(True)


	def escribeDat(self, d):
		nombre = d.nombre.text().strip()
		nombreDat=self.dirRep.filePath(nombre) + ".dat"
		config = ConfigObj(str(nombreDat), encoding='UTF8')
		config['descripcion'] = str(d.descripcion.toPlainText().strip())
		config.write()
		self.cargaTabla()

	@pyqtSlot(bool)
	def on_elimina_clicked(self, checked):
		res = QMessageBox.question(self, self.tr("¿Está seguro?"),
				self.tr("¿Desea eliminar los informes seleccionados?\n" +
					"Esta operación es permanente e irreversible"),
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Escape,
				QMessageBox.StandardButton.No)
		if res != QMessageBox.StandardButton.Yes:
			return
		for i in self.filasSeleccionadas():
			nombre=self.tabla.item(i, 0).text()
			nombreDat=self.dirRep.filePath(nombre) + ".dat"
			F = QFile(nombreDat)
			F.remove(nombreDat)
			self.dirRep.rmdir(nombre)
		self.cargaTabla()


	@pyqtSlot(bool)
	def on_crear_clicked(self, checked):
		l = self.filasSeleccionadas()
		if len(l) == 1:
			pass

	@pyqtSlot(bool)
	def on_activar_clicked(self, checked):
		l = self.filasSeleccionadas()
		if len(l) == 1:
			self.informeAc.setText(self.tabla.item(l[0], 0).text())
			self.s.setValue("inf/activo", self.tabla.item(l[0], 0).text())

	@pyqtSlot(QModelIndex)
	def on_tabla_doubleClicked(self, index):
		i = index.row()
		nombreBase0 = self.tabla.item(i, 0).text().split(".")[0]
		nombreDat=self.dirRep.filePath(nombreBase0) + ".dat"
		config = ConfigObj(str(nombreDat), encoding='UTF8')
		d = ReportDlg(self)
		d.nombre.setText(nombreBase0)
		d.descripcion.setText(config['descripcion'])
		if d.exec():
			nombreBase = d.nombre.text().strip()
			nombreDat=self.dirRep.filePath(nombreBase0) + ".dat"
			self.escribeDat(d)
			self.cargaTabla()

	@pyqtSlot(bool)
	def on_edita_clicked(self, checked):
		l = self.tabla.selectedIndexes()
		if len(self.filasSeleccionadas()) == 1:
			self.on_tabla_doubleClicked(l[0])

	@pyqtSlot(QItemSelection, QItemSelection)
	def tabla_selectionChanged(self, after, before):
		l = self.filasSeleccionadas()
		self.elimina.setEnabled(len(l) > 0)
		self.edita.setEnabled(len(l) == 1)
		self.activar.setEnabled(len(l) == 1)
		self.crear.setEnabled(len(l) > 0)
