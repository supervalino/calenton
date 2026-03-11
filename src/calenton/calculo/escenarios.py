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
# $Id: escenarios.py 258 2010-05-19 12:32:58Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/calculo/escenarios.py $
#
##############################################################################

from ts import SeqTableModel
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

class ErrorEscenario (Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return str(self.value)

class Escenarios:
	def __init__(self, db, idEscenario = None):
		self.db = db
		self.idEscenario = idEscenario
		self.informe = ""

	def initDebug(self):
		self.informe = ""

	def debug(self, mensaje):
		self.informe = self.informe + mensaje + "\n"

	def ejecutaSql(self, sql):
		self.debug(sql + ";")
		q = self.db.exec(sql)
		if self.db.lastError().isValid():
			raise ErrorEscenario(str(self.db.lastError().text()))
		return q

	def creaEscenario(self, nombre):
		idNuevo = SeqTableModel.nextVal('seq_escenario', self.db)
		sql = "insert into escenario (id, nombre) values (%d, '%s')" % (idNuevo, nombre)
		self.ejecutaSql(sql)
		self.idEscenario = idNuevo
		self.nombre = nombre

	def borraEscenario(self):
		sql = "delete from escenario where id = %d" % (self.idEscenario)
		self.ejecutaSql(sql)
		self.idEscenario = None

	def duplicaParametros(self, idEscenarioViejo):
		sql = """
			insert into parametro (id, idescenario, nombre, valor, descripcion)
			select nextval('seq_parametro'), %d, nombre, valor, descripcion
			from parametro
			where idescenario = %d
			""" % (self.idEscenario, idEscenarioViejo)
		self.ejecutaSql(sql)
		sql = """
			insert into parametrozona (id, idzona, idparametro, valor)
			select nextval('seq_parametrozona'), pz.idzona, pn.id, pz.valor
			from parametrozona pz, parametro pv, parametro pn
			where pv.idescenario = %d and
				pz.idparametro = pv.id and
				pn.idescenario = %d and
				pn.nombre = pv.nombre
			""" % (idEscenarioViejo, self.idEscenario)
		self.ejecutaSql(sql)

	def borraParametros(self):
		sql = """delete
			from parametrozona
			where idparametro in (
				select id from parametro where idescenario = %d)
			""" % (self.idEscenario)
		self.ejecutaSql(sql)
		sql = "delete from parametro where idescenario = %d" % (self.idEscenario)
		self.ejecutaSql(sql)

	def duplicaOrigen(self, idEscenarioViejo):
		sql = """
			insert into origen (id, idescenario, nombre)
			select nextval('seq_origen'), %d, nombre
			from origen
			where idescenario = %d
			""" % (self.idEscenario, idEscenarioViejo)
		self.ejecutaSql(sql)

	def borraOrigen(self):
		sql = "delete from origen where idescenario = %d" % (self.idEscenario)
		self.ejecutaSql(sql)

	def duplicaTipoDatoZona(self, idEscenarioViejo):
		sql = """
			insert into tipodatozona (id, idescenario, nombre, unidades, valor_defecto, variable)
			select nextval('seq_tipodatozona'), %d, nombre, unidades, valor_defecto, variable
			from tipodatozona
			where idescenario = %d
			""" % (self.idEscenario, idEscenarioViejo)
		self.ejecutaSql(sql)
		sql = """
			insert into datozona (id, idzona, idtipodatozona, dato)
			select nextval('seq_datozona'), dz.idzona, tdn.id, dz.dato
			from datozona dz, tipodatozona tdn, tipodatozona tdv
			where tdv.idescenario = %d and
				dz.idtipodatozona = tdv.id and
				tdn.idescenario = %d and
				tdn.nombre = tdv.nombre
			""" % (idEscenarioViejo, self.idEscenario)
		self.ejecutaSql(sql)

	def borraTipoDatoZona(self):
		sql = """delete
			from datozona
			where idtipodatozona in (
				select id from tipodatozona where idescenario = %d)
			""" % (self.idEscenario)
		self.ejecutaSql(sql)
		sql = "delete from tipodatozona where idescenario = %d" % (self.idEscenario)
		self.ejecutaSql(sql)

	def duplicaEquivContaminante(self, idEscenarioViejo):
		sql = """
			insert into equivcontaminante (id, idescenario, idcontaminante, p)
			select nextval('seq_equivcontaminante'), %d, idcontaminante, p
			from equivcontaminante
			where idescenario = %d
			""" % (self.idEscenario, idEscenarioViejo)
		self.ejecutaSql(sql)

	def borraEquivContaminante(self):
		sql = "delete from equivcontaminante where idescenario = %d" % (self.idEscenario)
		self.ejecutaSql(sql)

	def duplicaUnMapDatoContaminante(self, idMapDatoContaminante, idFormulaViejo):
		if idFormulaViejo > 0:
			idFormula = SeqTableModel.nextVal('seq_formula', self.db)
			if idFormula < 0:
				raise ErrorEscenario(str(self.db.lastError().text()))
			sql = """
				insert into formula (id, idescenario, expresion, valor)
				select %d, %d, expresion, valor
				from formula
				where id = %d
				""" % (idFormula, self.idEscenario, idFormulaViejo)
			idFormula = "%d" % (idFormula)
		else:
			idFormula = "null"
		self.ejecutaSql(sql)
		sql = """
			insert into mapdatocontaminante (id, idescenario, iddato, idclasificacion,
					idcontaminante, idformula)
			select nextval('seq_mapdatocontaminante'), %d, iddato, idclasificacion,
					idcontaminante, %s
			from mapdatocontaminante
			where id = %d
			""" % (self.idEscenario, idFormula, idMapDatoContaminante)
		self.ejecutaSql(sql)

	def borraMapDatoContaminante(self):
		sql = "delete from mapdatocontaminante where idescenario = %d" % (self.idEscenario)
		self.ejecutaSql(sql)
		sql = "delete from formula where idescenario = %d" % (self.idEscenario)
		self.ejecutaSql(sql)

	def duplicaMapDatoContaminante(self, idEscenarioViejo):
		sql = "select id, idformula from mapdatocontaminante where idescenario = %d" % (idEscenarioViejo)
		q = self.ejecutaSql(sql)
		while q.next():
			id = int(q.value(0) or 0)
			if q.value(1) is None:
				idFormula = -1
			else:
				idFormula = int(q.value(1) or 0)
			self.duplicaUnMapDatoContaminante(id, idFormula)

	def duplicaAforos(self, idFuente, idFuenteVieja, idEscenarioViejo):
		id = SeqTableModel.nextVal('seq_aforo', self.db)
		if id < 0:
			raise ErrorEscenario(self.db.lastError().text())
		sql = """
			insert into aforo (id, idfuente, nombre, descripcion, escala, idzona, idtipodatozona)
			select nextval('seq_aforo'), %d, a.nombre, a.descripcion, a.escala, a.idzona, tdn.id
			from aforo a
				left outer join tipodatozona tdv
					on tdv.id = a.idtipodatozona
				left outer join tipodatozona tdn
					on tdn.idescenario = %d and tdn.nombre = tdv.nombre
			where a.idfuente = %d
			""" % (idFuente, self.idEscenario, idFuenteVieja)
		self.ejecutaSql(sql)
		sql = """
			insert into parametroaforo (id, idaforo, idparametro, valor)
			select nextval('seq_parametroaforo'), an.id, pn.id, pa.valor
			from parametroaforo pa, parametro pn, parametro pv, aforo av, aforo an
			where pv.idescenario = %d and
				pn.idescenario = %d and
				pv.id = pa.idparametro and
				pn.nombre = pv.nombre and
				pa.idaforo = av.id and
				av.idfuente = %d and
				an.idfuente = %d and
				an.nombre = av.nombre
			""" % (idEscenarioViejo, self.idEscenario, idFuenteVieja, idFuente)
		self.ejecutaSql(sql)
		sql = """
			insert into valordato (id, idaforo, iddato, idclasificacion, valor)
			select nextval('seq_valordato'), an.id, v.iddato, v.idclasificacion, v.valor
			from valordato v, aforo av, aforo an
			where v.idaforo = av.id and
				av.idfuente = %d and
				an.idfuente = %d and
				an.nombre = av.nombre
			""" % (idFuenteVieja, idFuente)
		self.ejecutaSql(sql)
		sql = """
			insert into contaminantevalidadoaforo (id, idclasificacion, idaforo, idcontaminante, valor)
			select nextval('seq_contaminantevalidadoaforo'), cva.idclasificacion,
						an.id, cva.idcontaminante, cva.valor
			from contaminantevalidadoaforo cva, aforo av, aforo an
			where cva.idaforo = av.id and
				av.idfuente = %d and
				an.idfuente = %d and
				av.nombre = an.nombre
			""" % (idFuenteVieja, idFuente)
		self.ejecutaSql(sql)

	def borraAforo(self):
		subsql = "select a.id from aforo a, fuente f where a.idfuente = f.id and f.idescenario = %d" % (self.idEscenario)

		sql = "delete from contaminantevalidadoaforo where idaforo in (%s)" % (subsql)
		self.ejecutaSql(sql)
		sql = "delete from valordato where idaforo in (%s)" % (subsql)
		self.ejecutaSql(sql)
		sql = "delete from parametroaforo where idaforo in (%s)" % (subsql)
		self.ejecutaSql(sql)
		sql = "delete from aforo where idfuente in (select id from fuente where idescenario = %d)" % (self.idEscenario)
		self.ejecutaSql(sql)

	def duplicaFuente(self, idFuente, idEscenarioViejo):
		idFuenteNueva = SeqTableModel.nextVal('seq_fuente', self.db)
		if idFuenteNueva < 0:
			raise ErrorEscenario(self.db.lastError().text())
		sql = """
			insert into fuente (id, idescenario, nombre, descripcion, idorigen, idmotorcalculo,
						idnivelzona, idtipodatozona)
			select %d, %d, f.nombre, f.descripcion, orn.id, f.idmotorcalculo,
						f.idnivelzona, tdn.id
			from fuente f
					left outer join tipodatozona tdv
						on tdv.id = f.idtipodatozona
					left outer join tipodatozona tdn
						on tdn.idescenario = %d and tdn.nombre = tdv.nombre,
				origen ov, origen orn
			where f.id = %d and
				ov.id = f.idorigen and
				orn.idescenario = %d and
				orn.nombre = ov.nombre
			""" % (idFuenteNueva, self.idEscenario, idEscenarioViejo, idFuente, idEscenarioViejo)
		self.ejecutaSql(sql)
		sql = """
			insert into fuenteclasificacion (id, idfuente, idclasificacion)
			select nextval('seq_fuenteclasificacion'), %d, fc.idclasificacion
			from fuenteclasificacion fc
			where fc.idfuente = %d
			""" % (idFuenteNueva, idFuente)
		self.ejecutaSql(sql)
		self.duplicaAforos(idFuenteNueva, idFuente, idEscenarioViejo)

	def borraFuente(self):
		sql = "delete from fuenteclasificacion where idfuente in (select id from fuente where idescenario = %d)" % (self.idEscenario)
		self.ejecutaSql(sql)
		sql = "delete from fuente where idescenario = %d" % (self.idEscenario)
		self.ejecutaSql(sql)

	def duplicaFuentes(self, idEscenarioViejo):
		sql = "select id from fuente where idescenario = %d" % (idEscenarioViejo)
		q = self.ejecutaSql(sql)
		while q.next():
			idFuente = int(q.value(0) or 0)
			self.duplicaFuente(idFuente, idEscenarioViejo)

	def duplica(self, idEscenarioViejo, nombre):
		self.db.transaction()
		try:
			self.creaEscenario(nombre)
			self.duplicaParametros(idEscenarioViejo)
			self.duplicaOrigen(idEscenarioViejo)
			self.duplicaTipoDatoZona(idEscenarioViejo)
			self.duplicaEquivContaminante(idEscenarioViejo)
			self.duplicaFuentes(idEscenarioViejo)
			self.duplicaMapDatoContaminante(idEscenarioViejo)
			self.db.commit()
		except:
			self.db.rollback()
			raise

	def borraCalculos(self):
		sql = "delete from contaminantezona where idfuente in (select id from fuente where idescenario = %d)" % (self.idEscenario)
		self.ejecutaSql(sql)
		sql = """delete
			from contaminanteaforo
			where idaforo in (
				select a.id
				from aforo a, fuente f
				where a.idfuente = f.id and
					f.idescenario = %d)
			""" % (self.idEscenario)
		self.ejecutaSql(sql)

	def borra(self):
		self.db.transaction()
		self.initDebug()
		try:
			self.borraCalculos()
			self.borraAforo()
			self.borraFuente()
			self.borraMapDatoContaminante()
			self.borraEquivContaminante()
			self.borraTipoDatoZona()
			self.borraParametros()
			self.borraOrigen()
			self.borraEscenario()
			self.db.commit()
		except:
			self.db.rollback()
			raise

informe = None

def duplicaEscenario(idEscenario, nombre, db):
	try:
		QApplication.instance().setOverrideCursor(Qt.CursorShape.WaitCursor)
		es = Escenarios(db)
		es.duplica(idEscenario, nombre)
		return es.idEscenario
	finally:
		QApplication.instance().restoreOverrideCursor()

def borraEscenario(idEscenario, db):
	global informe

	es = Escenarios(db, idEscenario)
	try:
		QApplication.instance().setOverrideCursor(Qt.CursorShape.WaitCursor)
		es.borra()
	finally:
		informe = es.informe
		QApplication.instance().restoreOverrideCursor()

