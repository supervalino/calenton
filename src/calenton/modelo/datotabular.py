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
# $Id: datotabular.py 182 2010-04-08 10:41:10Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/datotabular.py $
#
##############################################################################

from ts import SeqTableModel
from PyQt6 import QtSql
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt6.QtSql import *
from PyQt6.QtWidgets import QApplication, QMessageBox

class InsertError (Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return str(self.value)

class DatoTabular (QAbstractTableModel):
	class Error (Exception):
		def __init__(self, value):
			self.value = value

		def __str__(self):
			return repr(self.value)

	def __init__(self, parent, idFuente, db = QtSql.QSqlDatabase()):
		QAbstractTableModel.__init__(self, parent)
		self.db = db
		self.idFuente = idFuente
		self.dirty = False
		self.idDatos = []
		self.idDatoClas = []
		self.mapDatos = {}
		self.nombreDatos = []
		self.idAforos = []
		self.nombreAforos = []
		self.mapAforos = {}
		self.mapNombreAforos = {}
		self.idAforosLista = []
		self.idAforoCache = {}
		self.cacheDatos = []
		self.cacheDirty = []

	def listaDatos(self):
		cambio = False
		if self.columnCount() > 2:
			self.beginRemoveColumns(QModelIndex(), 2, self.columnCount() - 1)
			cambio = True
		self.idDatos = []
		self.idDatoClas = []
		self.mapDatos = {}
		self.nombreDatos = []
		if cambio:
			self.endRemoveColumns()
		sql = """
				select d.id, d.nombre, c.codigo, c.id
				from dato d, fuenteclasificacion fc, clasificacion c
				where fc.idfuente = %d
					and d.idclasificacion in (
						select * from jerarquia_clasificacion(fc.idclasificacion)
						)
					and c.id = d.idclasificacion
				group by d.id, d.nombre, c.codigo, c.id
				order by c.codigo, d.nombre
			""" % (self.idFuente)
		q = QSqlQuery(sql, self.db)
		mapDatos = {}
		idDatos = []
		idDatoClas = []
		nombreDatos = []
		while q.next():
			id = int(q.value(0) or 0)
			nombre = str(q.value(1) or '')
			nombre2 = str(q.value(2) or '')
			idClas = int(q.value(3) or 0)
			nombre = nombre2 + '\n' + nombre
			mapDatos[id] = len(idDatos)
			idDatos.append(id)
			nombreDatos.append(nombre)
			idDatoClas.append(idClas)
		self.beginInsertColumns(QModelIndex(), 2, 2 + len(nombreDatos) - 1)
		self.mapDatos = mapDatos
		self.idDatos = idDatos
		self.idDatoClas = idDatoClas
		self.nombreDatos = nombreDatos
		self.endInsertColumns()

	def listaAforos(self):
		sql = """
				select a.id, a.nombre
				from aforo a
				where a.idfuente = %d
				order by a.nombre asc
			""" % (self.idFuente)
		q = QSqlQuery(sql, self.db)
		while q.next():
			id = int(q.value(0) or 0)
			nombre = str(q.value(1) or '')
			self.mapAforos[id] = len(self.idAforos)
			self.mapNombreAforos[nombre] = len(self.idAforos)
			self.idAforos.append(id)
			self.nombreAforos.append(nombre)

	def getDatos(self):
		cambio = False
		if self.rowCount() > 0:
			self.beginRemoveRows(QModelIndex(), 0, self.rowCount() - 1)
			cambio = True
		self.idAforoCache = {}
		self.cacheDatos = []
		self.cacheDirty = []
		self.dirty = False
		self.idAforos = []
		self.nombreAforos = []
		self.mapNombreAforos = {}
		self.mapAforos = {}
		if cambio:
			self.endRemoveRows()
		self.listaAforos()
		idAforoCache = {}
		cacheDatos = []
		cacheDirty = []
		idAforosLista = []
		sql = """
			select a.id, v.iddato, v.valor
			from aforo a, valordato v
			where v.idaforo = a.id and
				a.idfuente = %d and
				v.valor <> 0
			order by a.id
			""" % (self.idFuente)
		q = QSqlQuery(sql, self.db)
		lastId = -1
		r = None
		while q.next():
			id = int(q.value(0) or 0)
			idDato = int(q.value(1) or 0)
			v = float(q.value(2) or 0.0)
			if idDato not in self.mapDatos:
				continue
			if id != lastId:
				if r is not None:
					idAforoCache[lastId] = len(cacheDatos)
					idAforosLista.append(lastId)
					cacheDatos.append(r)
					cacheDirty.append(False)
				r = [ None for i in range(len(self.idDatos)) ]
				lastId = id
			r[self.mapDatos[idDato]] = v
		if r is not None:
			idAforoCache[lastId] = len(cacheDatos)
			idAforosLista.append(lastId)
			cacheDatos.append(r)
			cacheDirty.append(False)

		for id in self.idAforos:
			if id not in idAforoCache:
				idAforoCache[id] = None

		self.beginInsertRows(QModelIndex(), 0, len(cacheDatos) - 1)
		self.idAforosLista = idAforosLista
		self.idAforoCache = idAforoCache
		self.cacheDatos = cacheDatos
		self.cacheDirty = cacheDirty
		self.endInsertRows()

	def insertRows(self, position, rows, parent = QModelIndex()):
		if position > self.rowCount() or position < 0:
			return False
		self.beginInsertRows(parent, position, position + rows - 1)
		for i in range(rows):
			self.idAforosLista.insert(position, None)
			r = [ None for j in range(len(self.idDatos)) ]
			self.cacheDatos.insert(position, r)
			self.cacheDirty.insert(position, False)
		for k, v in self.idAforoCache.items():
			if v is not None and v >= position:
				self.idAforoCache[k] = v + rows
		self.endInsertRows()
		return True

	def getDataElement(self, data):
		if data is None:
			return None
		try:
			d = float(data)
		except (ValueError, TypeError):
			return None
		return d

	def borraDatos(self, id):
		sql = "delete from valordato where idaforo = %d" % (id)
		q = QSqlQuery(self.db)
		if not q.exec(sql):
			raise self.Error(q.lastError().text())

	def insertaDato(self, idAforo, idDato, idClas, valor):
		sql = """
			insert into valordato (id, idaforo, iddato, idclasificacion, valor)
			values (nextval('seq_valordato'), %d, %d, %d, %15.10g)
			""" % (idAforo, idDato, idClas, valor)
		q = QSqlQuery(self.db)
		if not q.exec(sql):
			raise self.Error(q.lastError().text())

	def submitAll(self):
		for id, row in self.idAforoCache.items():
			if row is None:
				self.borraDatos(id)
				continue
			if self.cacheDirty[row]:
				self.borraDatos(id)
				r = self.cacheDatos[row]
				for i in range(len(r)):
					if r[i] is not None and r[i] != 0:
						self.insertaDato(id, self.idDatos[i], self.idDatoClas[i], r[i])
				self.cacheDirty[row] = False
		self.headerDataChanged.emit(Qt.Orientation.Vertical, 0, self.rowCount() - 1)

	def submitTrans(self):
		self.db.transaction()
		try:
			self.submitAll()
			self.db.commit()
		except self.Error as e:
			self.db.rollback()
			QMessageBox.warning(None, self.tr('Error en inserción de datos'), str(e))

	def addRows(self, data):
		pos = self.rowCount()
		n = 0
		for i in range(len(data)):
			nombre = str(data[i][1]).strip() if data[i][1] is not None else ''
			if nombre in self.mapNombreAforos:
				n = n + 1
		self.beginInsertRows(QModelIndex(), pos, pos + n - 1)
		for d in data:
			r = [ self.getDataElement(d[j + 2]) for j in range(len(self.idDatos)) ]
			n2 = d[1]
			nombre = str(n2).strip() if n2 is not None else ''
			if nombre not in self.mapNombreAforos:
				raise InsertError('No existe el aforo ' + nombre)
			na = self.mapNombreAforos[nombre]
			id = self.idAforos[na]
			row = len(self.cacheDatos)
			self.cacheDatos.append(r)
			self.cacheDirty.append(True)
			self.idAforosLista.append(id)
			self.idAforoCache[id] = row
			self.dirty = True
		self.endInsertRows()

	def removeRows(self, position, rows, parent = QModelIndex()):
		if position < 0 or (position + rows) > self.rowCount() or rows < 0:
			return False
		if rows == 0:
			return True
		self.beginRemoveRows(parent, position, position + rows - 1)
		for i in range(rows):
			self.cacheDatos.pop(position)
			self.cacheDirty.pop(position)
			if self.idAforosLista[position] is not None:
				self.idAforoCache[self.idAforosLista[position]] = None
				self.dirty = True
			self.idAforosLista.pop(position)
		for k, v in self.idAforoCache.items():
			if v is not None and v >= (position + rows):
				self.idAforoCache[k] = v - rows
		self.endRemoveRows()
		return True

	def actualiza(self):
		QApplication.instance().setOverrideCursor(Qt.CursorShape.WaitCursor)
		self.listaDatos()
		self.getDatos()
		QApplication.instance().restoreOverrideCursor()

	def select(self):
		self.actualiza()

	def setIdFuente(self, idFuente):
		self.idFuente = idFuente
		self.actualiza()

	def rowCount(self, index = QModelIndex()):
		return len(self.cacheDatos)

	def columnCount(self, index = QModelIndex()):
		return len(self.idDatos) + 2

	def data(self, index, role = Qt.ItemDataRole.DisplayRole):
		if not index.isValid():
			return None
		c = index.column()
		r = index.row()
		if role == Qt.ItemDataRole.TextAlignmentRole:
			if c == 1:
				return int(Qt.AlignmentFlag.AlignLeft)
			else:
				return int(Qt.AlignmentFlag.AlignRight)
		if role != Qt.ItemDataRole.DisplayRole and role != Qt.ItemDataRole.EditRole:
			return None
		if r >= self.rowCount():
			return None
		if c >= self.columnCount():
			return None
		if c == 0:
			return self.idAforosLista[r]
		elif c == 1:
			id = self.idAforosLista[r]
			if id is None:
				return None
			else:
				return self.nombreAforos[self.mapAforos[id]]
		else:
			return self.cacheDatos[r][c - 2]

	def headers(self):
		l = []
		l.append('id')
		l.append('nombre')
		for i in self.nombreDatos:
			l.append(str(i))
		return l

	def headerData(self, section, orientation, role = Qt.ItemDataRole.DisplayRole):
		if role != Qt.ItemDataRole.DisplayRole:
			return None
		if orientation == Qt.Orientation.Horizontal:
			if section < 0 or section >= self.columnCount():
				return None
			if section == 0:
				return 'id'
			elif section == 1:
				return 'nombre'
			else:
				return self.nombreDatos[section - 2]
		elif orientation == Qt.Orientation.Vertical:
			if section >= self.rowCount():
				return None
			elif self.cacheDirty[section]:
				return "*"
			else:
				return str(section)
		else:
			return None

	def flags(self, index):
		if not index.isValid():
			return Qt.ItemFlag.ItemIsEnabled
		r = index.row()
		c = index.column()
		res = QAbstractTableModel.flags(self, index)
		if c < 2:
			if self.idAforosLista[r] is None:
				res = res | Qt.ItemFlag.ItemIsEditable
		else:
			res = res | Qt.ItemFlag.ItemIsEditable
		return res

	def setData(self, index, value, role = Qt.ItemDataRole.EditRole):
		if not index.isValid():
			return False
		if role != Qt.ItemDataRole.EditRole:
			return False
		r = index.row()
		c = index.column()
		if c >= self.columnCount():
			return False
		if r >= self.rowCount():
			return False
		if c > 1:
			if value is None or value == '':
				d = None
			else:
				try:
					d = float(value)
				except (ValueError, TypeError):
					return False
				if d == 0.0:
					d = None
			c = c - 2
			if self.cacheDatos[r][c] != d:
				self.cacheDatos[r][c] = d
				self.cacheDirty[r] = True
				self.dirty = True
				self.dataChanged.emit(index, index)
			return True
		if c == 0:
			try:
				id = int(value)
			except (ValueError, TypeError):
				return False
			if id not in self.mapAforos:
				return False
			nombre = self.nombreAforos[self.mapAforos[id]]
		elif c == 1:
			nombre = str(value) if value is not None else ''
			if nombre not in self.mapNombreAforos:
				return False
			id = self.idAforos[self.mapNombreAforos[nombre]]
		if self.idAforosLista[r] is not None:
			if self.idAforosLista[r] == id:
				return True
			else:
				return False
		self.idAforosLista[r] = id
		self.idAforoCache[id] = r
		self.cacheDirty[r] = True
		self.dirty = True
		self.dataChanged.emit(self.index(r, 0), self.index(r, 1))
		return True

	def pendingChanges(self):
		return self.dirty

