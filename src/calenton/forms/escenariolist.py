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
# $Id: escenariolist.py 255 2010-05-19 09:24:46Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/escenariolist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from .ui.Ui_escenariolist import *
from ..calculo.escenarios import duplicaEscenario, borraEscenario
from ..calculo import escenarios
from .escenariodlg import EscenarioDlg
from .origendlg import OrigenDlg
from .parametrodlg import ParametroDlg
from ..widgets.datalist import DataList
from .tipodatozonadlg import TipoDatoZonaDlg
class EscenarioList (DataList, Ui_EscenarioListClass):
	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)
		app = QApplication.instance()
		if app.databaseInit:
			self.db = app.workDb()
			self.mEscenario = app.mEscenario
			self.idEscenario = -1
			self.tablaEscenario.setModel(self.mEscenario)
			self.tablaEscenario.hideColumn(self.mEscenario.fieldIndex("id"))
			self.tablaEscenario.selectionModel().selectionChanged.connect(self.tablaEscenario_selectionChanged)
			self.cambiaEncabezado(self.mEscenario, ['Escenario'])
			self.tablaEscenario.resizeColumnsToContents()
			self.tablaEscenario.resizeRowsToContents()
			self.mOrigen = app.mOrigen
			self.idOrigen = -1
			self.mOrigen.setParentId(self.idEscenario)
			self.tablaOrigen.setModel(self.mOrigen)
			self.tablaOrigen.hideColumn(self.mOrigen.fieldIndex("id"))
			self.cambiaEncabezado(self.mOrigen, ['Escenario', 'Origen'])
			self.tablaOrigen.selectionModel().selectionChanged.connect(self.tablaOrigen_selectionChanged)
			self.tablaOrigen.resizeColumnsToContents()
			self.mParametro = app.mParametro
			self.idParametro = -1
			self.mParametro.setParentId(self.idEscenario)
			self.tablaParametro.setModel(self.mParametro)
			self.tablaParametro.hideColumn(self.mParametro.fieldIndex("id"))
			self.cambiaEncabezado(self.mParametro, ['Escenario', 'Parametro', 'Valor', 'Descripción'])
			self.tablaParametro.selectionModel().selectionChanged.connect(self.tablaParametro_selectionChanged)
			self.tablaParametro.resizeColumnsToContents()

			self.mTipoDatoZona = app.mTipoDatoZona
			self.tablaTipoDato.setModel(self.mTipoDatoZona)
			self.tablaTipoDato.hideColumn(self.mTipoDatoZona.fieldIndex("id"))
			self.tablaTipoDato.selectionModel().selectionChanged.connect(self.tablaTipoDato_selectionChanged)

			self.tablaEscenario_selectionChanged(QItemSelection(), QItemSelection())

	######################################################################
	# Escenario
	#

	@pyqtSlot(bool)
	def on_anadeEscenario_clicked(self, checked):
		d = EscenarioDlg(self, self.mEscenario)
		if d.add():
			self.mEscenario.submitTrans()

	@pyqtSlot(bool)
	def on_eliminaEscenario_clicked(self, checked):
		r = QMessageBox.question(self, self.tr("Borrar un escenario"),
			self.tr("¿Está seguro que quiere borrar el escenario?" +
				"\nesto borrará el escenario y todos sus datos asociados," +
				"\nincluyendo entre otros: fuentes, aforos, parametros, datos de emisión..."),
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
		if r != QMessageBox.StandardButton.Yes:
			return
		try:
			borraEscenario(self.idEscenario, self.db)
		except Exception as e:
			mb = QMessageBox(self)
			mb.setText(self.tr("Error al borrar"))
			mb.setInformativeText(str(e))
			mb.setStandardButtons(QMessageBox.StandardButton.Ok)
			mb.setDetailedText(escenarios.informe)
			mb.setIcon(QMessageBox.Critical)
			mb.exec()
		self.mEscenario.select()

	@pyqtSlot("const QModelIndex &")
	def on_tablaEscenario_doubleClicked(self, index):
		dm = EscenarioDlg(self, self.mEscenario)
		if dm.edit(index.row()):
			self.mEscenario.submitTrans()

	@pyqtSlot(bool)
	def on_editaEscenario_clicked(self, checked):
		l = self.tablaEscenario.selectedIndexes()
		l2 = self.mEscenario.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaEscenario_doubleClicked(l[0])

	@pyqtSlot(bool)
	def on_duplicaEscenario_clicked(self, checked):
		(nombre, ok) = QInputDialog.getText(self, self.tr("Duplicar escenario"),
				self.tr("Elija el nombre del nuevo escenario"))
		if not ok or not nombre:
			return
		try:
			duplicaEscenario(self.idEscenario, nombre, self.db)
		except Exception as e:
			QMessageBox.warning(self, self.tr("Error al borrar"), str(e))
		self.mEscenario.select()

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaEscenario_selectionChanged(self, before, after):
		l = self.tablaEscenario.selectionModel().selectedIndexes()
		self.idEscenario = self.mEscenario.getId(l)
		self.eliminaEscenario.setEnabled(self.idEscenario > 0)
		self.editaEscenario.setEnabled(self.idEscenario > 0)
		self.duplicaEscenario.setEnabled(self.idEscenario > 0)
		self.mOrigen.setParentId(self.idEscenario)
		self.tablaOrigen_selectionChanged(QItemSelection(), QItemSelection())
		self.tablaOrigen.resizeColumnsToContents()
		self.tablaOrigen.resizeRowsToContents()
		self.mParametro.setParentId(self.idEscenario)
		self.tablaParametro_selectionChanged(QItemSelection(), QItemSelection())
		self.tablaParametro.resizeColumnsToContents()
		self.tablaParametro.resizeRowsToContents()
		self.mTipoDatoZona.setParentId(self.idEscenario)
		self.tablaTipoDato_selectionChanged(QItemSelection(), QItemSelection())
		self.tablaTipoDato.resizeColumnsToContents()
		self.tablaTipoDato.resizeRowsToContents()

	######################################################################
	# Origen
	#

	@pyqtSlot(bool)
	def on_anadeOrigen_clicked(self, checked):
		d = OrigenDlg(self, self.mOrigen)
		if d.add():
			self.mOrigen.submitTrans()
			self.tablaOrigen.resizeColumnsToContents()

	@pyqtSlot(bool)
	def on_eliminaOrigen_clicked(self, checked):
		self.askAndRemoveRows(self.tablaOrigen, self.mOrigen)

	@pyqtSlot("const QModelIndex &")
	def on_tablaOrigen_doubleClicked(self, index):
		dm = OrigenDlg(self, self.mOrigen)
		if dm.edit(index.row()):
			self.mOrigen.submitTrans()
			self.tablaOrigen.resizeColumnsToContents()

	@pyqtSlot(bool)
	def on_editaOrigen_clicked(self, checked):
		l = self.tablaOrigen.selectedIndexes()
		l2 = self.mOrigen.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaOrigen_doubleClicked(l[0])

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaOrigen_selectionChanged(self, before, after):
		l = self.tablaOrigen.selectionModel().selectedIndexes()
		self.eliminaOrigen.setEnabled(self.mOrigen.eraseActive(l))
		self.idOrigen = self.mOrigen.getId(l)
		self.editaOrigen.setEnabled(self.idOrigen > 0)

	######################################################################
	# Parametro
	#

	@pyqtSlot(bool)
	def on_anadeParametro_clicked(self, checked):
		d = ParametroDlg(self, self.mParametro)
		if d.add():
			self.mParametro.submitTrans()
			self.tablaParametro.resizeColumnsToContents()

	@pyqtSlot(bool)
	def on_eliminaParametro_clicked(self, checked):
		self.askAndRemoveRows(self.tablaParametro, self.mParametro)

	@pyqtSlot("const QModelIndex &")
	def on_tablaParametro_doubleClicked(self, index):
		dm = ParametroDlg(self, self.mParametro)
		if dm.edit(index.row()):
			self.mParametro.submitTrans()
			self.tablaParametro.resizeColumnsToContents()

	@pyqtSlot(bool)
	def on_editaParametro_clicked(self, checked):
		l = self.tablaParametro.selectedIndexes()
		l2 = self.mParametro.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaParametro_doubleClicked(l[0])

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaParametro_selectionChanged(self, before, after):
		l = self.tablaParametro.selectionModel().selectedIndexes()
		self.eliminaParametro.setEnabled(self.mParametro.eraseActive(l))
		self.idParametro = self.mOrigen.getId(l)
		self.editaParametro.setEnabled(self.idParametro > 0)

	######################################################################
	# TipoDato
	#

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaTipoDato_selectionChanged(self, before, after):
		pass

	@pyqtSlot(bool)
	def on_anadeTipoDato_clicked(self, checked):
		d = TipoDatoZonaDlg(self, self.mTipoDatoZona)
		if d.add():
			self.mTipoDatoZona.submitTrans()

	@pyqtSlot(bool)
	def on_eliminaTipoDato_clicked(self, checked):
		self.askAndRemoveRows(self.tablaTipoDato, self.mTipoDatoZona)

	@pyqtSlot("const QModelIndex &")
	def on_tablaTipoDato_doubleClicked(self, index):
		dm = TipoDatoZonaDlg(self, self.mTipoDatoZona)
		if dm.edit(index.row()):
			self.mTipoDatoZona.submitTrans()

	@pyqtSlot(bool)
	def on_editaTipoDato_clicked(self, checked):
		l = self.tablaTipoDato.selectedIndexes()
		l2 = self.mTipoDatoZona.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaTipoDato_doubleClicked(l[0])


