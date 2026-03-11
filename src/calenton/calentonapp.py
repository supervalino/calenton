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
##############################################################################

from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QSettings
from PyQt6.QtSql import QSqlDatabase
from .modelo import *
from .js import motor as js_motor
from ts import Magnitude
from ts import UnitSystem
from ts import ForeignKey
from qgis.core import QgsApplication
from .calculo import cache as calculo_cache
from .calculo import temporal as calculo_temporal
from .calculo import mapas as calculo_mapas

class CalentonApp(QgsApplication):
	def __init__(self, argv):
		super().__init__([a.encode() if isinstance(a, str) else a for a in argv], True)
		self.setOrganizationName("LITEC")
		self.setOrganizationDomain("litec.csic.es")
		self.setApplicationName("calenton")
		self.setPrefixPath('/usr', True)
		self.initQgis()
		self.initUnits()
		s = QSettings()
		if self.openDatabase():
			self.databaseInit = True
			self.createModels()
			self.motorJS = js_motor.Motor(self.workDb(), bool(s.value("script/stackable", False)))
			self.cache = calculo_cache.CacheParametros(self.workDb())
			self.tablaTemporal = calculo_temporal.TablaTemporal(self.workDb())
			self.mapas = calculo_mapas.Mapas(self.workDb(), self.tablaTemporal)
		else:
			self.databaseInit = False
			self.cache = None
			self.tablaTemporal = None
			self.mapas = None

	def refreshMotorJS(self):
		del self.motorJS
		s = QSettings()
		self.motorJS = js_motor.Motor(self.workDb(), bool(s.value("script/stackable", False)))

	def openDatabase(self):
		s = QSettings()
		if not s.value("db/basedatos"):
			QMessageBox.warning(None, self.tr("Falta configuración"),
					self.tr("No se ha definido la conexión a la base de datos, hazlo en preferencias"))
			return False
		db = QSqlDatabase.addDatabase('QPSQL', 'work')
		db.setDatabaseName(str(s.value("db/basedatos", "")))
		db.setHostName(str(s.value("db/servidor", "")))
		db.setUserName(str(s.value("db/usuario", "")))
		db.setPassword(str(s.value("db/password", "")))
		puerto = s.value("db/puerto", 5432)
		db.setPort(int(puerto))
		if not db.open():
			QMessageBox.critical(None, self.tr('Error al abrir base de datos'),
						db.lastError().text())
			db.close()
			QSqlDatabase.removeDatabase('work')
			return False
		else:
			return True

	def workDb(self):
		return self.work

	def informeActivo(self):
		s = QSettings()
		return str(s.value("inf/activo", ""))

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

		self.mRelZonas = relzona.RelZona(self, self.work)

		self.mMapperRelZonas = relzona.RelZona(self, self.work)

		self.mNivelZonas = nivelzona.NivelZona(self, self.work)
		self.mNivelZonas.select()

		self.mTipoclas = tipoclas.Tipoclas(self, self.work)
		self.mTipoclas.select()

		self.mEquivContaminante = equivcontaminante.EquivContaminante(self, self.work)

		self.mFuenteClasificacion = fuenteclasificacion.FuenteClasificacion(self, self.work)

		self.mClasificacion = clasificacion.Clasificacion(self, self.work)
		self.mClasificacion.setForeignKey('idtipoclas', ForeignKey('tipoclas', 'nombre'))
		self.mClasificacion.setParentId(-1)

		self.mDato = dato.Dato(self, self.work)
		self.mDato.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.mDato.setParentId(-1)

		self.mFuenteClasificacion = fuenteclasificacion.FuenteClasificacion(self, self.work)
		self.mFuenteClasificacion.setForeignKey('idfuente', ForeignKey('fuente', 'nombre'))
		self.mFuenteClasificacion.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.mFuenteClasificacion.setParentId(-1)

		self.mMapDatoContaminante = mapdatocontaminante.MapDatoContaminante(self, self.work)
		self.mMapDatoContaminanteClas = mapdatocontaminante.MapDatoContaminante(self, self.work, True)

		self.mContaminanteAforo = contaminanteaforo.ContaminanteAforo(self, self.work)

		self.mContaminanteZona = contaminantezona.ContaminanteZona(self, self.work)
		self.mContaminanteZona.setForeignKey('idcontaminante', ForeignKey('contaminante', 'nombre'))
		self.mContaminanteZona.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.mContaminanteZona.setForeignKey('idfuente', ForeignKey('fuente', 'nombre'))
		self.mContaminanteZona.setParentId(-1)

		self.mValorDato = valordato.ValorDato(self, self.work)
		self.mValorDato.setForeignKey('idaforo', ForeignKey('aforo', 'nombre'))
		self.mValorDato.setForeignKey('idclasificacion', ForeignKey('clasificacion', 'codigo'))
		self.mValorDato.setForeignKey('iddato', ForeignKey('dato', 'nombre'))
		self.mValorDato.setParentId(-1)

		self.mMapAforoZona = mapaforozona.MapAforoZona(self, self.work)
		self.mMapAforoZona.setForeignKey('idaforo', ForeignKey('aforo', 'nombre'))
		self.mMapAforoZona.setForeignKey('idzona', ForeignKey('zona', 'nombre'))
		self.mMapAforoZona.setParentId(-1)

		self.mMapDatoContaminanteAforo = mapdatocontaminanteaforo.MapDatoContaminanteAforo(self, self.work)
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
		for i in range(0, model.rowCount()):
			record = model.record(i)
			mLista.append(str(record.value(field) or ""))
		return mLista
