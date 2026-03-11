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
# $Id: arbolclasificacion.py 73 2010-01-21 14:53:41Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/modelo/arbolclasificacion.py $
#
##############################################################################

from ts import SeqTableModel
from PyQt6.QtSql import *
from PyQt6.QtCore import *

class Item (object):
	def __init__(self, id, data, parent):
		self.parentItem = parent
		self.id = id
		self.itemData = data
		self.children = []

	def child(self, row):
		if row < len(self.children):
			return self.children[row]
		else:
			return None

	def childCount(self):
		return len(self.children)

	def childNumber(self):
		if self.parentItem is not None:
			return self.parentItem.children.index(self)
		else:
			return 0

	def columnCount(self):
		return len(self.itemData)

	def data(self, column):
		if column >= 0 and column < len(self.itemData):
			return self.itemData[column]
		else:
			return None

	def insertChildren(self, position, count):
		if position == -1:
			position = len(self.children)
		if position < 0 or position > len(self.children):
			return False
		for row in range(count):
			data = [ None for i in range(len(self.itemData)) ]
			item = Item(None, data, self)
			self.children.insert(position, item)
		return True

	def insertChild(self, position, child):
		if position == -1:
			position = len(self.children)
		if position < 0 or position > len(self.children):
			return False
		self.children.insert(position, child)
		return True

	def removeChildren(self, position, count):
		if position < 0 or (position + count) > len(self.children):
			return False
		for row in range(count):
			self.children.pop(position)
		return True

	def removeAllChildren(self):
		self.children = []

	def setData(self, column, value):
		if column < 0 or column >= len(self.itemData):
			return False
		self.itemData[column] = value
		return True

	def parent(self):
		return self.parentItem


class ArbolClasificacion (QAbstractItemModel):
	def __init__(self, idtipo, db = QSqlDatabase(), parent = None):
		QAbstractItemModel.__init__(self, parent)
		self.idtipo = idtipo
		self.db = db
		rootData = [ 'id', 'codigo', 'descripcion' ]
		self.rootItem = Item(None, rootData, None)
		if self.idtipo != -1:
			self.setupDataItem(self.rootItem, self.rootItem)

	def setIdTipo(self, idTipo):
		if idTipo == self.idtipo:
			return
		n = self.rootItem.childCount()
		self.beginRemoveRows(QModelIndex(), 0, n - 1)
		self.rootItem.removeAllChildren()
		self.endRemoveRows()
		self.idtipo = idTipo
		rootData = [ 'id', 'codigo', 'descripcion' ]
		rootItem = Item(None, rootData, None)
		self.setupDataItem(rootItem, rootItem)
		self.beginInsertRows(QModelIndex(), 0, rootItem.childCount() - 1)
		self.rootItem = rootItem
		self.endInsertRows()

	def setupDataItem(self, parent, root):
		if parent == root:
			cond = "idpadre is null"
		else:
			cond = "idpadre = %d" % (parent.id)
		sql = """
				select id, codigo, descripcion
				from clasificacion
				where idtipoclas = %d
					and %s
				order by codigo
				""" % (self.idtipo, cond)
		q = QSqlQuery(sql, self.db)
		while q.next():
			id = int(q.value(0) or 0)
			codigo = str(q.value(1) or '')
			desc = str(q.value(2) or '')
			data = [ id, codigo, desc ]
			item = Item(id, data, parent)
			parent.insertChild(-1, item)
		for i in range(parent.childCount()):
			self.setupDataItem(parent.child(i), root)

	def columnCount(self, parent = QModelIndex()):
		return self.rootItem.columnCount()

	def data(self, index, role):
		if not index.isValid():
			return None
		if role != Qt.ItemDataRole.DisplayRole and role != Qt.ItemDataRole.EditRole:
			return None
		item = self.getItem(index)
		if item == self.rootItem:
			return None
		r = item.data(index.column())
		return r

	def flags(self, index):
		if not index.isValid():
			return Qt.ItemFlag(0)
		r = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
		item = self.getItem(index)
		if index.column() > 1 and item != self.rootItem:
			r = r | Qt.ItemFlag.ItemIsEditable
		return r

	def getItem(self, index):
		if index.isValid():
			item = index.internalPointer()
			if item is not None:
				return item
		return self.rootItem

	def headerData(self, section, orientation, role = Qt.ItemDataRole.DisplayRole):
		if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
			return self.rootItem.data(section)
		return None

	def index(self, row, column, parent = QModelIndex()):
		if parent.isValid() and parent.column() != 0:
			return QModelIndex()
		parentItem = self.getItem(parent)
		if row < 0 or row >= parentItem.childCount():
			return QModelIndex()
		childItem = parentItem.child(row)
		if childItem is None:
			return QModelIndex()
		return self.createIndex(row, column, childItem)

	def insertColumns(self, position, columns, parent = QModelIndex()):
		return False

	def insertRows(self, position, rows, parent = QModelIndex()):
		parentItem = self.getItem(parent)
		self.beginInsertRows(parent, position, position + rows - 1)
		success = parentItem.insertChildren(position, rows)
		self.endInsertRows()
		return success

	def parent(self, index):
		if not index.isValid():
			return QModelIndex()
		childItem = self.getItem(index)
		if childItem == self.rootItem:
			return QModelIndex()
		parentItem = childItem.parent()
		if parentItem == self.rootItem:
			return QModelIndex()
		return self.createIndex(parentItem.childNumber(), 0, parentItem)

	def removeColumns(self, position, columns, parent = QModelIndex()):
		return False

	def removeRows(self, position, rows, parent = QModelIndex()):
		parentItem = self.getItem(parent)
		self.beginRemoveRows(parent, position, position + rows - 1)
		success = parentItem.removeChildren(position, rows)
		self.endRemoveRows()
		return success

	def rowCount(self, parent = QModelIndex()):
		parentItem = self.getItem(parent)
		return parentItem.childCount()

	def setData(self, index, value, role = Qt.ItemDataRole.EditRole):
		if role != Qt.ItemDataRole.EditRole:
			return False
		item = self.getItem(index)
		if item == self.rootItem:
			return False
		c = index.column()
		if c == 0:
			d = int(value) if value is not None else 0
		else:
			d = str(value) if value is not None else ''
		success = item.setData(c, d)
		if success:
			self.dataChanged.emit(index, index)
		return success

	def setHeaderData(self, section, orientation, value, role = Qt.ItemDataRole.EditRole):
		return False

	def getIds(self, l):
		rows = {}
		for i in l:
			if i.row() in rows:
				continue
			e = i
			if e.column() != 0:
				e = e.sibling(e.row(), 0)
			id_val = e.data()
			if id_val is None:
				continue
			try:
				id = int(id_val)
			except (ValueError, TypeError):
				continue
			rows[e.row()] = id
		return rows.values()

	def getId(self, l):
		ids = list(self.getIds(l))
		if len(ids) != 1:
			return -1
		else:
			return ids[0]


