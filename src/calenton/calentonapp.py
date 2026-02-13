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
# $Id: calentonapp.py 357 2010-11-18 13:13:14Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/calentonapp.py $
#
##############################################################################

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from modelo import *
import js.motor
from ts import Magnitude
from ts import UnitSystem
from ts import ForeignKey
from qgis.core import QgsApplication
import calculo.cache
import calculo.temporal
import calculo.mapas

class CalentonApp(QgsApplication):
	def __init__(self, argv):
		QgsApplication.__init__(self, argv, True)
		QApplication.setOrganizationName("LITEC")
		QApplication.setOrganizationDomain("litec.csic.es")
		QApplication.setApplicationName("calenton")
		QgsApplication.setPrefixPath('/usr', True)
		QgsApplication.initQgis()
		self.initUnits()
		s = QSettings()
		if self.openDatabase():
			self.databaseInit = True
			self.createModels()
			self.motorJS = js.motor.Motor(self.workDb(), s.value("script/stackable").toBool())
			self.cache = calculo.cache.CacheParametros(self.workDb())
			self.tablaTemporal = calculo.temporal.TablaTemporal(self.workDb())
			self.mapas = calculo.mapas.Mapas(self.workDb(), self.tablaTemporal)
		else:
			self.databaseInit = False
			self.cache = None
			self.tablaTemporal = None
			self.mapas = None
		
	def refreshMotorJS(self):
		del self.motorJS
		s = QSettings()
		self.motorJS = js.motor.Motor(self.workDb(), s.value("script/stackable").toBool())
		
	def openDatabase(self):
		s = QSettings()
		if s.value("db/basedatos").isNull():
			QMessageBox.warning(None, self.tr("Falta configuración"),
					self.tr("No se ha definido la conexión a la base de datos, hazlo en preferencias"),
					QMessageBox.Ok)
			return False
		db = QSqlDatabase.addDatabase('QPSQL', 'work')
		db.setDatabaseName(s.value("db/basedatos").toString())
		db.setHostName(s.value("db/servidor").toString())
		db.setUserName(s.value("db/usuario").toString())
		db.setPassword(s.value("db/password").toString())
#		QSqlQuery("client_encoding = 'UTF8'", db)
		(puerto, good) = s.value("db/puerto").toInt()
		db.setPort(puerto)
		if not db.open():
			QMessageBox.critical(None, self.tr('Error al abrir base de datos'), 
						db.lastError().text(), QMessageBox.Ok)
			db.close()
			db = None
			QSqlDatabase.removeDatabase('work')
			return False
		else:
			return True
		
	def workDb(self):
		return self.work
		
	def informeActivo(self):
		s = QSettings()
		return s.value("inf/activo").toString()
		
	def createModels(self):
		self.work = QSqlDatabase.database('work')
		if self.work is None:
			return
		self.mEscenario = escenario.Escenario(self, self.work)
		self.mEscenario.select()

		self.mFuente = fuente.Fuente(self, self.work)

		self.mOrigen = origen.Origen(self, self.work)
		self.mOrigen.setForeignKey('idescenario', ForeignKey('escenario', 'nombre'))
		self.mOrigen.select()

		self.mParametro = parametro.Parametro(self, self.work)
		self.mParametro.setForeignKey('idescenario', ForeignKey('escenario', 'nombre'))
		self.mParametro.setParentId(-1)

		self.mAforo = aforo.Aforo(self, self.work)
		self.mAforo.setForeignKey('idfuente', ForeignKey('fuente', 'nombre'))
		self.mAforo.setForeignKey('idzona', ForeignKey('zona', 'nombre'))
		self.mAforo.setForeignKey('idtipodatozona', ForeignKey('tipodatozona', 'nombre'))
		self.mAforo.setParentId(-1)

		self.mMotoresCalculo = motorcalculo.MotorCalculo(self, self.work)
		self.mMotoresCalculo.select()

		self.mZonas = zona.Zona(self, self.work)
		self.mZonas.setForeignKey('idnivelzona', ForeignKey('nivelzona', 'nombre'))

		self.mRelZonas = relzona.RelZona(self,self.work)

		self.mMapperRelZonas = relzona.RelZona(self,self.work)

		self.mNivelZonas = nivelzona.NivelZona(self,self.work)
		self.mNivelZonas.select()

		self.mTipoclas = tipoclas.Tipoclas(self,self.work)
		self.mTipoclas.select()

		self.mEquivContaminante = equivcontaminante.EquivContaminante(self,self.work)

		self.mFuenteClasificacion = fuenteclasificacion.FuenteClasificacion(self,self.work)

		self.mClasificacion = clasificacion.Clasificacion(self, self.work)
		self.mClasificacion.setForeignKey('idtipoclas', ForeignKey('tipoclas', 'nombre'))
		self.mClasificacion.setParentId(-1)
		
		self.mDato = dato.Dato(self, self.work)
		self.mDato.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.mDato.setParentId(-1)

		self.mFuenteClasificacion = fuenteclasificacion.FuenteClasificacion(self,self.work)
		self.mFuenteClasificacion.setForeignKey('idfuente', ForeignKey('fuente', 'nombre'))
		self.mFuenteClasificacion.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.mFuenteClasificacion.setParentId(-1)

		self.mMapDatoContaminante = mapdatocontaminante.MapDatoContaminante(self, self.work)
		self.mMapDatoContaminanteClas = mapdatocontaminante.MapDatoContaminante(self, self.work, True)

		self.mContaminanteAforo = contaminanteaforo.ContaminanteAforo(self,self.work)

		self.mContaminanteZona = contaminantezona.ContaminanteZona(self,self.work)
		self.mContaminanteZona.setForeignKey('idcontaminante', ForeignKey('contaminante', 'nombre'))
		self.mContaminanteZona.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.mContaminanteZona.setForeignKey('idfuente', ForeignKey('fuente', 'nombre'))
		self.mContaminanteZona.setParentId(-1)

		self.mValorDato = valordato.ValorDato(self,self.work)
		self.mValorDato.setForeignKey('idaforo', ForeignKey('aforo', 'nombre'))
		self.mValorDato.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.mValorDato.setForeignKey('iddato', ForeignKey('dato', 'nombre'))
		self.mValorDato.setParentId(-1)

		self.mMapAforoZona = mapaforozona.MapAforoZona(self,self.work)
		self.mMapAforoZona.setForeignKey('idaforo', ForeignKey('aforo', 'nombre'))
		self.mMapAforoZona.setForeignKey('idzona', ForeignKey('zona', 'nombre'))
		self.mMapAforoZona.setParentId(-1)

		self.mMapDatoContaminanteAforo = mapdatocontaminanteaforo.MapDatoContaminanteAforo(self,self.work)
		self.mMapDatoContaminanteAforo.setForeignKey('idaforo', ForeignKey('aforo', 'nombre'))
		self.mMapDatoContaminanteAforo.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.mMapDatoContaminanteAforo.setForeignKey('iddato', ForeignKey('dato', 'nombre'))
		self.mMapDatoContaminanteAforo.setForeignKey('idcontaminante', ForeignKey('contaminante', 'nombre'))
		self.mMapDatoContaminanteAforo.setParentId(-1)

		self.mContaminante = contaminante.Contaminante(self, self.work)
		
		self.mTipoDatoZona = tipodatozona.TipoDatoZona(self, self.work)
		self.mTipoDatoZona.setForeignKey('idescenario', ForeignKey('escenario', 'nombre'))
		self.mTipoDatoZona.setParentId(-1)
		
		self.mDatoZona = datozona.DatoZona(self, self.work)
		self.mDatoZona.setForeignKey('idtipodatozona', ForeignKey('tipodatozona', 'nombre'))
		self.mDatoZona.setForeignKey('idzona', ForeignKey('zona', 'nombre'))
		
		self.mParametroZona = parametrozona.ParametroZona(self, self.work)
		self.mParametroAforo = parametroaforo.ParametroAforo(self, self.work)
		
		self.mContaminanteValAforo = contaminantevalidadoaforo.ContaminanteValidadoAforo(self, self.work)
		self.mCombustible = combustible.Combustible(self, self.work)
		self.mClasCombustible = clascombustible.ClasCombustible(self, self.work)
		
	def initUnits(self):
		Magnitude.registerMetaType()
		self.unitSystem = UnitSystem("config/unidades.xml")
		UnitSystem.setDefaultUnitSystem(self.unitSystem)

	def modelo2lista(self, model, field):
		mLista = []
#		model = self.app.mEscenario
		for i in range(0,model.rowCount()):
			record = model.record(i)
			mLista.append(record.value(field).toString())
		return mLista
