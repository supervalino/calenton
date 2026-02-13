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
# $Id: main.py 360 2010-11-18 22:17:21Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/main.py $
#
##############################################################################

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui.Ui_main import *
from escenariodlg import EscenarioDlg
from preferenciasdlg import PreferenciasDlg
from escenariolist import EscenarioList
from motorcalculolist import MotorCalculoList
from fuentelist import FuenteList
from zonalist import ZonaList
from tipoclaslist import TipoclasList
from contaminantelist import ContaminanteList
from equivcontaminantelist import EquivContaminanteList
from mapdatocontaminantelist import MapDatoContaminanteList
from mapdatocontaminanteaforolist import MapDatoContaminanteAforoList
from fuenteclasificacionlist import FuenteClasificacionList
#from valordatolist import ValorDatoList
from mapaforozonalist import MapAforoZonaList
from contaminanteaforolist import ContaminanteAforoList
from contaminantezonalist import ContaminanteZonaList
from plantillalist import PlantillaList
from reportlist import ReportList
from graphiclist import GraphicList
from tablelist import TableList
from arbolclasificacion import ArbolClasificacion
from elegirescenariodlg import ElegirEscenarioDlg
from widgets.progresocalculo import ProgresoCalculo
from listadoresultadosdlg import ListadoResultadosDlg
from combustiblelist import CombustibleList
from maparesultadosdlg import MapaResultadosDlg
from mapa import Mapa
from modelo import escenario
from modelo import motorcalculo
from modelo import origen
from modelo import parametro
from modelo import aforo
from modelo import fuente
from modelo import zona
from modelo import relzona
from modelo import tipoclas
from modelo import contaminante
from modelo import equivcontaminante
from modelo import mapdatocontaminante
from modelo import mapdatocontaminanteaforo
from modelo import fuenteclasificacion
from modelo import clasificacion
#from modelo import valordato
from modelo import dato
from modelo import mapaforozona
from modelo import contaminanteaforo
from modelo import contaminantezona
from widgets import permanentsubwindow

from widgets.datalist import DataListBase
from widgets.subwindow import SubWindowBase

from calculo import calcula
import gc
import pdb

class MainWindow (QMainWindow, Ui_MainWindowClass):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.mdiArea = QMdiArea(self)
		self.mdiArea.setObjectName("mdiArea")
		self.setupUi(self)
		self.setCentralWidget(self.mdiArea)
		
		self.escenarioList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.escenarioList.setWidget(EscenarioList(self.escenarioList))
		self.centralWidget().addSubWindow(self.escenarioList)
		self.escenarioList.visibilityChanged.connect(self.actionEscenario.setChecked)
		self.escenarioList.hide()

		self.fuenteList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.fuenteList.setWidget(FuenteList(self.fuenteList))
		self.centralWidget().addSubWindow(self.fuenteList)
		self.fuenteList.visibilityChanged.connect(self.actionFuente.setChecked)
		self.fuenteList.hide()

		self.motorCalculoList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.motorCalculoList.setWidget(MotorCalculoList(self.motorCalculoList))
		self.centralWidget().addSubWindow(self.motorCalculoList)
		self.motorCalculoList.visibilityChanged.connect(self.actionMotoresCalculo.setChecked)
		self.motorCalculoList.hide()

		self.zonaList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.zonaList.setWidget(ZonaList(self.zonaList))
		self.centralWidget().addSubWindow(self.zonaList)
		self.zonaList.visibilityChanged.connect(self.actionZonas.setChecked)
		self.zonaList.hide()

		self.tipoclasList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.tipoclasList.setWidget(TipoclasList(self.tipoclasList))
		self.centralWidget().addSubWindow(self.tipoclasList)
		self.tipoclasList.visibilityChanged.connect(self.actionTipo_Clasificaci_n.setChecked)
		self.tipoclasList.hide()

		self.equivcontaminanteList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.equivcontaminanteList.setWidget(EquivContaminanteList(self.equivcontaminanteList))
		self.centralWidget().addSubWindow(self.equivcontaminanteList)
		self.equivcontaminanteList.visibilityChanged.connect(self.actionEquivalentes.setChecked)
		self.equivcontaminanteList.hide()

		self.contaminanteList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.contaminanteList.setWidget(ContaminanteList(self.contaminanteList))
		self.centralWidget().addSubWindow(self.contaminanteList)
		self.contaminanteList.visibilityChanged.connect(self.actionContaminante.setChecked)
		self.contaminanteList.hide()

		self.mapdatocontaminanteList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.mapdatocontaminanteList.setWidget(MapDatoContaminanteList(self.mapdatocontaminanteList))
		self.centralWidget().addSubWindow(self.mapdatocontaminanteList)
		self.mapdatocontaminanteList.visibilityChanged.connect(self.actionFactor_Conversi_n.setChecked)
		self.mapdatocontaminanteList.hide()

		self.mapdatocontaminanteaforoList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
#		self.mapdatocontaminanteaforoList.setWidget(MapDatoContaminanteAforoList(self.mapdatocontaminanteaforoList))
#		self.centralWidget().addSubWindow(self.mapdatocontaminanteaforoList)
		self.mapdatocontaminanteaforoList.visibilityChanged.connect(self.actionFactor_Conversi_n_por_Aforo.setChecked)
		self.mapdatocontaminanteaforoList.hide()

		self.fuenteclasificacionList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.fuenteclasificacionList.setWidget(FuenteClasificacionList(self.fuenteclasificacionList))
		self.centralWidget().addSubWindow(self.fuenteclasificacionList)
		self.fuenteclasificacionList.visibilityChanged.connect(self.actionFuenteClasificacion.setChecked)
		self.fuenteclasificacionList.hide()

#		self.valordatoList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
#		self.valordatoList.setWidget(ValorDatoList(self.valordatoList))
#		self.centralWidget().addSubWindow(self.valordatoList)
#		self.valordatoList.visibilityChanged.connect(self.actionValor_Dato.setChecked)
#		self.valordatoList.hide()

		self.mapaforozonaList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.mapaforozonaList.setWidget(MapAforoZonaList(self.mapaforozonaList))
		self.centralWidget().addSubWindow(self.mapaforozonaList)
		self.mapaforozonaList.visibilityChanged.connect(self.actionMapAforoZona.setChecked)
		self.mapaforozonaList.hide()

		self.contaminanteaforoList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.contaminanteaforoList.setWidget(ContaminanteAforoList(self.contaminanteaforoList))
		self.centralWidget().addSubWindow(self.contaminanteaforoList)
		self.contaminanteaforoList.visibilityChanged.connect(self.actionContaminante_Aforo.setChecked)
		self.contaminanteaforoList.hide()

		self.contaminantezonaList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.contaminantezonaList.setWidget(ContaminanteZonaList(self.contaminantezonaList))
		self.centralWidget().addSubWindow(self.contaminantezonaList)
		self.contaminantezonaList.visibilityChanged.connect(self.actionContaminanteZona.setChecked)
		self.contaminantezonaList.hide()

#		self.plantillaList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
#		self.plantillaList.setWidget(PlantillaList(self.plantillaList))
#		self.centralWidget().addSubWindow(self.plantillaList)
#		self.plantillaList.visibilityChanged.connect(self.actionPlantillas.setChecked)
#		self.plantillaList.hide()

		self.reportList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.reportList.setWidget(ReportList(self.reportList))
		self.centralWidget().addSubWindow(self.reportList)
		self.reportList.visibilityChanged.connect(self.actionPlantillas.setChecked)
		self.reportList.hide()
		
		self.arbolClasificacion = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.arbolClasificacion.setWidget(ArbolClasificacion(self.arbolClasificacion))
		self.centralWidget().addSubWindow(self.arbolClasificacion)
		self.arbolClasificacion.visibilityChanged.connect(self.actionArbolClasificacion.setChecked)
		self.arbolClasificacion.hide()
		
		self.graphicList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.graphicList.setWidget(GraphicList(self.graphicList))
		self.centralWidget().addSubWindow(self.graphicList)
		self.graphicList.visibilityChanged.connect(self.actionGraficos.setChecked)
		self.graphicList.hide()
		
		self.tableList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.tableList.setWidget(TableList(self.tableList))
		self.centralWidget().addSubWindow(self.tableList)
		self.tableList.visibilityChanged.connect(self.actionTablas.setChecked)
		self.tableList.hide()
		
		self.combustibleList = permanentsubwindow.PermanentSubWindow(self.mdiArea)
		self.combustibleList.setWidget(CombustibleList(self.combustibleList))
		self.centralWidget().addSubWindow(self.combustibleList)
		self.combustibleList.visibilityChanged.connect(self.actionCombustibles.setChecked)
		self.combustibleList.hide()
		
	@pyqtSlot("bool")
	def on_actionOpenConnection_triggered(self, checked):
		pass

	@pyqtSlot("bool")
	def on_actionPreferencias_triggered(self, checked):
		d = PreferenciasDlg(self)
		d.exec_()
		
	@pyqtSlot("bool")
	def on_actionArbolClasificacion_triggered(self, checked):
		self.arbolClasificacion.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionEscenario_triggered(self, checked):
		self.escenarioList.setVisible(checked)

	@pyqtSlot("bool")
	def on_actionOrigen_triggered(self, checked):
		self.origenList.setVisible(checked)

	@pyqtSlot("bool")
	def on_actionAforo_triggered(self, checked):
		self.aforoList.setVisible(checked)

	@pyqtSlot("bool")
	def on_actionFuente_triggered(self, checked):
		self.fuenteList.setVisible(checked)

	@pyqtSlot("bool")
	def on_actionMotoresCalculo_triggered(self, checked):
		self.motorCalculoList.setVisible(checked)

	@pyqtSlot("bool")
	def on_actionZonas_triggered(self, checked):
		self.zonaList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionTipo_Clasificaci_n_triggered(self, checked):
		self.tipoclasList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionEquivalentes_triggered(self, checked):
		self.equivcontaminanteList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionContaminante_triggered(self, checked):
		self.contaminanteList.setVisible(checked)

	@pyqtSlot("bool")
	def on_actionFactor_Conversi_n_triggered(self, checked):
		self.mapdatocontaminanteList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionFactor_Conversi_n_por_Aforo_triggered(self, checked):
		self.mapdatocontaminanteaforoList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionFuenteClasificacion_triggered(self, checked):
		self.fuenteclasificacionList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionMapAforoZona_triggered(self, checked):
		self.mapaforozonaList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionContaminante_Aforo_triggered(self, checked):
		self.contaminanteaforoList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionContaminanteZona_triggered(self, checked):
		self.contaminantezonaList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionPlantillas_triggered(self, checked):
		self.reportList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionGenerar_PDF_triggered(self, checked):
		self.generar_PDF.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionGraficos_triggered(self, checked):
		self.graphicList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionTablas_triggered(self, checked):
		self.tableList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionCalcularEscenario_triggered(self, checked):
		dlg = ElegirEscenarioDlg(self)
		if not dlg.exec_():
			return
		p = ProgresoCalculo(self)
		p.setWindowModality(Qt.WindowModal)
		(idEscenario, g) = dlg.escenario.currentItemData().toInt()
		if not g:
			return
		app = QApplication.instance()
		calc = calcula.CalculaEscenario(idEscenario, app.workDb(), app.cache, app.motorJS, p)
		try:
			calc.calcula()
		except Exception, e:
			QMessageBox.warning(self, self.tr("Error en cálculo"), QString(unicode(e)))
			p.reset()
		app.cache.clean()
		gc.collect()
		app.refreshMotorJS()
		
	@pyqtSlot("bool")
	def on_actionResultados_triggered(self, checked):
		dlg = ListadoResultadosDlg(self)
		dlg.exec_()
		
	@pyqtSlot("bool")
	def on_actionCombustibles_triggered(self, checked):
		self.combustibleList.setVisible(checked)
		
	@pyqtSlot("bool")
	def on_actionCopiar_triggered(self, checked):
		a = self.centralWidget().activeSubWindow()
		if a is None:
			return
		dl = a.findChild(SubWindowBase)
		if dl is None:
			return
		dl.copy()
		
	@pyqtSlot("bool")
	def on_actionMapas_triggered(self, checked):
		d = MapaResultadosDlg(self)
		if d.exec_() == QDialog.Accepted:
			w = QMdiSubWindow(self.mdiArea)
			w.setWidget(Mapa(d.sql, d.idNivelZona, d.color, w))
			self.centralWidget().addSubWindow(w)
			w.show()
		
	@pyqtSlot("QMdiSubWindow *")
	def on_mdiArea_subWindowActivated(self, subWindow):
		canCopy = False
		canPrint = False
		if subWindow is not None:
			dl = subWindow.findChild(SubWindowBase)
			if dl is not None:
				canCopy = dl.canCopy()
				canPrint = dl.canPrint()
		self.actionCopiar.setEnabled(canCopy)
		self.actionPrint.setEnabled(canPrint)
		
	def closeEvent(self, ce):
		r = QMessageBox.question(self, self.tr("Salir..."), self.tr("¿Estás seguro?"),
			QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if r == QMessageBox.No:
			ce.ignore()
		else:
			app = QApplication.instance()
			app.tablaTemporal.quitaTodas()
			ce.accept()
	
	
	
	
