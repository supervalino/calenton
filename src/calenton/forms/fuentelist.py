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
# $Id: fuentelist.py 347 2010-11-02 12:10:58Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/fuentelist.py $
#
##############################################################################

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from .ui.Ui_fuentelist import *
from .fuentedlg import FuenteDlg
from .aforodlg import AforoDlg
from .buscardlg import BuscarDlg
from .valordatodlg import ValorDatoDlg
from .informedlg import InformeDlg
from ..widgets.datalist import DataList
from ..widgets.clasitemdelegate import ClasItemDelegate
from ..widgets.progresocalculo import ProgresoCalculo
from ..modelo.datotabular import DatoTabular
from ts import FKItemDelegate, ComboDataModel, TSqlTableNavigator
from ..calculo import calcula
class ValDelegate (TSqlTableNavigator.Delegate):
	def __init__(self, parent, lista):
		TSqlTableNavigator.Delegate.__init__(self, parent)
		self.lista = lista

	def couldAdd(self, nav):
		if self.lista.idAforo > 0:
			return True
		else:
			return False

	def newRecord(self, nav):
		r = self.lista.mContaminanteValAforo.record()
		r.setValue('idaforo', self.lista.idAforo)
		return r

class EditorFactory (QItemEditorFactory):
	def __init__(self):
		QItemEditorFactory.__init__(self)
		self.fact = QItemEditorFactory.defaultFactory()

	def createEditor(self, type, parent):
		type2 = type
		if type2 == QMetaType.Double:
			type2 = QMetaType.QString
		return self.fact.createEditor(type2, parent)

class FuenteList (DataList, Ui_FuenteListClass):
	editorFactory = None

	def __del__(self):
		if FuenteList.editorFactory is not None:
			del FuenteList.editorFactory
			FuenteList.editorFactory = None
		DataList.__del__(self)

	def __init__(self, parent = None):
		DataList.__init__(self, parent)
		self.setupUi(self)

		app = QApplication.instance()
		if not app.databaseInit:
			return

		self.app = app
		self.db = app.workDb()
		self.puedeCalcular = False


		self.mFuente = app.mFuente
		self.idFuente = -1
		self.tablaFuente.setModel(self.mFuente)
		self.tablaFuente.hideColumn(self.mFuente.fieldIndex("id"))
		self.cambiaEncabezado(self.mFuente, [
				'Escenario', 'Fuente', 'Descripción', 'Origen',
				'Motor de Cálculo', 'Nivel Zona', 'Dato Distribución' ])
		self.tablaFuente.selectionModel().selectionChanged.connect(self.tablaFuente_selectionChanged)
		self.tablaFuente.resizeColumnsToContents()
		self.tablaFuente.resizeRowsToContents()

		# para pestaña aforo
		self.mAforo = app.mAforo
		self.idAforo = -1
		self.tablaAforo.setModel(self.mAforo)
		self.tablaAforo.hideColumn(self.mAforo.fieldIndex("id"))
		self.cambiaEncabezado(self.mAforo, [
				'Fuente', 'Aforo', 'Descripción', 'Escala', 'Zona',
				'Dato Distribución' ])
		self.tablaAforo.selectionModel().selectionChanged.connect(self.tablaAforo_selectionChanged)
		self.tablaAforo.resizeColumnsToContents()
		self.tablaAforo.resizeRowsToContents()

		self.mParametroAforo = app.mParametroAforo
		self.tablaParametros.setModel(self.mParametroAforo)
		self.tablaParametros.hideColumn(self.mParametroAforo.fieldIndex('id'))
		self.cambiaEncabezado(self.mParametroAforo, ['Aforo', 'Parametro', 'valor'])
#		self.mParametroAforo.primeInsert.connect(self.tablaParametros_primeInsert)
		self.tablaParametros.setItemDelegateForColumn(
					self.mParametroAforo.fieldIndex('idaforo'),
					FKItemDelegate({'idfuente': -1 }, self))
		self.tablaParametros.setItemDelegateForColumn(
					self.mParametroAforo.fieldIndex('idparametro'),
					FKItemDelegate({'idescenario': -1 }, self))
		self.tablaParametros.selectionModel().selectionChanged.connect(
					self.tablaParametros_selectionChanged)
		if FuenteList.editorFactory is None:
			FuenteList.editorFactory = EditorFactory()
		self.delValParam = QStyledItemDelegate(self)
		self.delValParam.setItemEditorFactory(FuenteList.editorFactory)
		self.tablaParametros.setItemDelegateForColumn(
					self.mParametroAforo.fieldIndex('valor'),
					self.delValParam)

		# para pestaña dato tabular
		self.mValorDatoTabular = DatoTabular(self, self.idFuente, app.workDb())
		self.tablaDatoTabular.setModel(self.mValorDatoTabular)
		self.tablaDatoTabular.selectionModel().selectionChanged.connect(
				self.tablaDatoTabular_selectionChanged)

		self.mContaminanteValAforo = app.mContaminanteValAforo
#		self.mContaminanteValAforo.primeInsert.connect(self.navValidado_primeInsert)
#		self.connect(self.mContaminanteValAforo, SIGNAL("primeInsert(int, QSqlRecord &)"),
#				self, SLOT("navValidado_primeInsert(int, QSqlRecord &)"))
		self.navValidado.setModel(self.mContaminanteValAforo)
		self.navValidado.tableView().hideColumn(
				self.mContaminanteValAforo.fieldIndex('id'))
		self.cambiaEncabezado(self.mContaminanteValAforo, [ 'Clasificación', 'Aforo', 'Contaminante', 'Valor'])
		self.navValidado.setDelegate(ValDelegate(self.navValidado, self))
		self.navValidado.tableView().setItemDelegateForColumn(
				self.mContaminanteValAforo.fieldIndex("idaforo"),
				FKItemDelegate({'idfuente': None }, self))
		self.navValidado.tableView().setItemDelegateForColumn(
				self.mContaminanteValAforo.fieldIndex("idcontaminante"),
				FKItemDelegate({}, self))
		self.navValidado.tableView().setItemDelegateForColumn(
				self.mContaminanteValAforo.fieldIndex("idclasificacion"),
				ClasItemDelegate(self))

		# Para pestaña de resultados
		self.mContaminanteAforo = app.mContaminanteAforo
		self.navResultados.setModel(self.mContaminanteAforo)

		# para pestaña dato
		self.mValorDato = app.mValorDato
		self.idDato = -1
		self.tablaDato.setModel(self.mValorDato)
		self.tablaDato.hideColumn(self.mValorDato.fieldIndex("id"))
		self.cambiaEncabezado(self.mValorDato, ['Aforo', 'Dato', 'Clasificación', 'Valor'])
		self.tablaDato.selectionModel().selectionChanged.connect(self.tablaDato_selectionChanged)
		self.tablaDato.setItemDelegateForColumn(
				self.mValorDato.fieldIndex("idaforo"),
				FKItemDelegate({'idfuente': -1 }, self))
		self.tablaDato.setItemDelegateForColumn(
				self.mValorDato.fieldIndex("iddato"),
				FKItemDelegate({'idclasificacion': None }, self))
		self.tablaDato.setItemDelegateForColumn(
				self.mValorDato.fieldIndex("idclasificacion"), ClasItemDelegate(self))

		self.tablaDato.resizeColumnsToContents()
		self.tablaDato.resizeRowsToContents()

		# Para comprobaciones de datos
		self.mFuenteClasificacion=app.mFuenteClasificacion

		self.i_busca = -1

		self.idEscenario = -1
		self.mEscenario = ComboDataModel(self)
		self.mEscenario.setQuery("select id, nombre from escenario order by id", self.db)
		self.escenario.setModel(self.mEscenario)

		self.cambiaFuentes()

	##########################################################################
	# Fuentes
	#

	@pyqtSlot(int)
	def on_escenario_activated(self, index):
		self.cambiaFuentes()

	def cambiaFuentes(self):
		self.idEscenario = -1
		ide = self.escenario.currentItemData()
		if ide is not None:
			i = int(ide or 0)
			if i:
				self.idEscenario = i
		self.mFuente.setParentId(self.idEscenario)
		self.tablaParametros.itemDelegateForColumn(
				self.mParametroAforo.fieldIndex('idparametro')
				).setFilterValue('idescenario', self.idEscenario)
		self.tablaFuente.resizeColumnsToContents()
		self.tablaFuente.resizeRowsToContents()
		self.tablaFuente_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(bool)
	def on_deseleccionaFuente_clicked(self, checked):
		self.mAforo.setParentId(-1)
		self.tablaFuente.clearSelection()

	@pyqtSlot(bool)
	def on_anadeFuente_clicked(self, checked):
		d = FuenteDlg(self, self.mFuente)
		if d.add():
			self.mFuente.submitTrans()

	@pyqtSlot(bool)
	def on_eliminaFuente_clicked(self, checked):
		self.askAndRemoveRows(self.tablaFuente, self.mFuente)

	@pyqtSlot(bool)
	def on_editaFuente_clicked(self, checked):
		l = self.tablaFuente.selectedIndexes()
		l2 = self.mFuente.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaFuente_doubleClicked(l[0])

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaFuente_selectionChanged(self, before, after):
		l = self.tablaFuente.selectionModel().selectedIndexes()
		self.eliminaFuente.setEnabled(self.mFuente.eraseActive(l))
		self.idFuente = self.mFuente.getId(l)
		self.editaFuente.setEnabled(self.idFuente > 0)
		self.mAforo.setParentId(self.idFuente)
		self.tablaAforo.resizeColumnsToContents()
		self.tablaAforo.resizeRowsToContents()
		self.mValorDatoTabular.setIdFuente(self.idFuente)
		self.tablaDatoTabular.resizeColumnsToContents()
		self.tablaDatoTabular.resizeRowsToContents()
		self.tablaAforo_selectionChanged(QItemSelection(), QItemSelection())
		self.tablaDatoTabular_selectionChanged(QItemSelection(), QItemSelection())
		self.tablaDato.itemDelegateForColumn(
				self.mValorDato.fieldIndex("idaforo")).setFilterValue(
								"idfuente", self.idFuente)
		self.tablaDato.itemDelegateForColumn(
				self.mValorDato.fieldIndex("idclasificacion")).setIdFuente(self.idFuente)
		self.tablaParametros.itemDelegateForColumn(self.mParametroAforo.fieldIndex('idaforo')
				).setFilterValue('idfuente', self.idFuente)
		self.navValidado.tableView().itemDelegateForColumn(
				self.mContaminanteValAforo.fieldIndex('idaforo')
				).setFilterValue('idfuente', self.idFuente)
		self.navValidado.tableView().itemDelegateForColumn(
				self.mContaminanteValAforo.fieldIndex('idclasificacion')
				).setIdFuente(self.idFuente)

	@pyqtSlot("const QModelIndex &")
	def on_tablaFuente_doubleClicked(self, index):
		dm = FuenteDlg(self, self.mFuente)
		if dm.edit(index.row()):
			self.mFuente.submitTrans()

	@pyqtSlot(bool)
	def on_calcularFuente_triggered(self, checked):
		p = ProgresoCalculo(self)
		p.setWindowModality(Qt.WindowModal)
		calc = calcula.CalculaEscenario(self.idEscenario, self.app.workDb(),
					self.app.cache, self.app.motorJS, p)
		try:
			calc.calculaFuente(self.idFuente)
		except Exception as e:
			QMessageBox.warning(self, self.tr("Error en cálculo"), str(e))
			p.reset()
		self.app.cache.clean()
		self.app.refreshMotorJS()

	def tablaFuente_contextualMenuActions(self):
		if self.idFuente > 0:
			r = [ self.calcularFuente ]
		else:
			r = None
		return r

	##########################################################################
	# Aforos
	#

	@pyqtSlot(bool)
	def on_anadeAforo_clicked(self, checked):
		d = AforoDlg(self, self.mAforo, self.idEscenario, self.idFuente)
		if d.add():
			self.mAforo.submitTrans()

	@pyqtSlot(bool)
	def on_eliminaAforo_clicked(self, checked):
		self.askAndRemoveRows(self.tablaAforo, self.mAforo)

	@pyqtSlot(bool)
	def on_editaAforo_clicked(self, checked):
		l = self.tablaAforo.selectedIndexes()
		l2 = self.mAforo.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaAforo_doubleClicked(l[0])

	@pyqtSlot("const QModelIndex &")
	def on_tablaAforo_doubleClicked(self, index):
		dm = AforoDlg(self, self.mAforo, self.idEscenario, self.idFuente)
		if dm.edit(index.row()):
			self.mAforo.submitTrans()

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaAforo_selectionChanged(self, after, before):
		l = self.tablaAforo.selectionModel().selectedIndexes()
		self.eliminaAforo.setEnabled(self.mAforo.eraseActive(l) and not self.mAforo.pendingChanges())
		self.idAforo = self.mAforo.getId(l)
		self.mValorDato.setParentId(self.idAforo)
		self.tablaDato.resizeColumnsToContents()
		self.tablaDato.resizeRowsToContents()
		self.tablaDato_selectionChanged(QItemSelection(), QItemSelection())
		self.editaAforo.setEnabled(self.idAforo > 0 and not self.mAforo.pendingChanges())
		self.anadeAforo.setEnabled(not self.mAforo.pendingChanges())
		self.cambiaParametros()
		self.navValidado.setParentId(self.idAforo)
		self.navResultados.setParentId(self.idAforo)
		self.puedeCalcular = (self.idAforo > 0)

	@pyqtSlot(bool)
	def on_guardaAforo_clicked(self, checked):
		self.mAforo.submitTrans()
		self.anadeAforo.setEnabled(True)

	@pyqtSlot(bool)
	def on_descartaAforo_clicked(self, checked):
		self.mAforo.revertAll()
		self.anadeAforo.setEnabled(True)

	@pyqtSlot(bool)
	def on_buscaAforo_clicked(self, checked):
		campos = [self.tr('Aforo y descripción'), 'Aforo', self.tr('Descripción')]
		d = BuscarDlg(self)
		d.campos.addItems(campos)
		d.campos.setCurrentIndex(self.i_busca)
		d.exec()
		self.i_busca = d.campos.currentIndex()
		t = d.texto.text().strip()
		if t == "":
			self.mAforo.setParentId(-1)
			return
		if self.i_busca == 0:
			filtro = "nombre ~* '%s' or descripcion ~* '%s'" % (t, t)
			self.mAforo.setFilter(filtro)
		if self.i_busca == 1:
			filtro = "nombre ~* '%s'" % (t)
			self.mAforo.setFilter(filtro)
		if self.i_busca == 2:
			filtro = "descripcion ~* '%s'" % (t)
			self.mAforo.setFilter(filtro)

	@pyqtSlot(bool)
	def on_deseleccionaAforo_clicked(self, checked):
		self.mValorDato.setParentId(-1)
		self.tablaAforo.clearSelection()

	def insertDataAforo(self, data):
		fields = [ 'idfuente', 'nombre', 'descripcion', 'escala', 'idzona', 'idtipodatozona' ]
		self.mAforo.addRows(fields, data)

	def tablaAforo_contextualMenuActions(self):
		r = [ self.clipboardAforo ]
		if self.puedeCalcular:
			r.insert(0, self.calcularAforo)
		return r

	@pyqtSlot(bool)
	def on_clipboardAforo_triggered(self, checked):
		self.getDataFromClipboard(checked, self.insertDataAforo)

	@pyqtSlot(bool)
	def on_calcularAforo_triggered(self, checked):
		calc = calcula.CalculaEscenario(self.idEscenario, self.app.workDb(),
					self.app.cache, self.app.motorJS, None)
		try:
			calc.calculaAforo(self.idAforo)
		except Exception as e:
			QMessageBox.warning(self, self.tr("Error en cálculo"), str(e))
		id = InformeDlg(self)
		id.setCalc(calc)
		id.exec()
		calc.descartaInforme()

	##########################################################################
	# Parametros
	#

	def cambiaParametros(self):
		self.mParametroAforo.revertAll()
		self.mParametroAforo.setFilter("""
			idaforo = %d and
			idparametro in (
				select id from parametro where idescenario = %d
				)
			""" % (self.idAforo, self.idEscenario))
		self.tablaParametros_selectionChanged(QItemSelection(), QItemSelection())
		self.tablaParametros.resizeColumnsToContents()
		self.tablaParametros.resizeRowsToContents()

	def tablaParametros_contextualMenuActions(self):
		if self.idAforo > 0 and self.idEscenario > 0:
			return [ self.clipboardParametros ]
		else:
			return None

	@pyqtSlot(bool)
	def on_anadeParametros_clicked(self, checked):
		row = self.mParametroAforo.rowCount()
		r = self.mParametroAforo.record()
		if self.idAforo:
			r.setValue('idaforo', self.idAforo)
		self.mParametroAforo.insertRecord(row, r)
		idx = self.mParametroAforo.index(row, 1)
		if row == 0:
			self.tablaParametros.resizeColumnsToContents()
			self.tablaParametros.resizeRowsToContents()
		self.tablaParametros.setCurrentIndex(idx)
		self.tablaParametros.edit(idx)

	@pyqtSlot(bool)
	def on_guardaParametros_clicked(self, checked):
		self.mParametroAforo.submitTrans()
		self.tablaParametros_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(bool)
	def on_descartaParametros_clicked(self, checked):
		self.cambiaParametros()

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaParametros_selectionChanged(self, before, after):
		l = self.tablaParametros.selectionModel().selectedIndexes()
		self.guardaParametros.setEnabled(self.mParametroAforo.pendingChanges())
		self.descartaParametros.setEnabled(self.mParametroAforo.pendingChanges())
		self.escenario.setEnabled(not self.mParametroAforo.pendingChanges())
		self.anadeParametros.setEnabled(self.idAforo > 0 and self.idEscenario > 0)
		self.eliminaParametros.setEnabled(len(l) > 0)
		self.tab.setLocked(self.mParametroAforo.pendingChanges())

	def insertDataParametros(self, data):
		fields = [ 'idzona', 'idparametro', 'valor' ]
		filters = [ { 'idnivelzona': self.idNivelZona },
					{ 'idescenario': self.idEscenario },
					{} ]
		order = [ 'idzona', 'idparametro', 'valor' ]
		try:
			self.mParametroAforo.addRows(fields, data, filters, order)
		finally:
			self.tablaParametros.resizeColumnsToContents()
			self.tablaParametros.resizeRowsToContents()
			self.tablaParametros_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(bool)
	def on_clipboardParametros_triggered(self, checked):
		self.getDataFromClipboard(checked, self.insertDataParametros)


	##########################################################################
	# Dato
	#

	@pyqtSlot(bool)
	def on_anadeDato_clicked(self, checked):
		d = ValorDatoDlg(self, self.mValorDato)
		if d.add():
			self.mValorDato.submitTrans()

	@pyqtSlot(bool)
	def on_eliminaDato_clicked(self, checked):
		self.askAndRemoveRows(self.tablaDato, self.mValorDato)

	@pyqtSlot(bool)
	def on_editaDato_clicked(self, checked):
		l = self.tablaDato.selectedIndexes()
		l2 = self.mValorDato.selectedRows(l)
		if len(l2) == 1:
			self.on_tablaDato_doubleClicked(l[0])

	@pyqtSlot("const QModelIndex &")
	def on_tablaDato_doubleClicked(self, index):
		dm = ValorDatoDlg(self, self.mValorDato)
		if dm.edit(index.row()):
			self.mValorDato.submitTrans()

	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaDato_selectionChanged(self, after, before):
		l = self.tablaDato.selectionModel().selectedIndexes()
		self.eliminaDato.setEnabled(self.mValorDato.eraseActive(l) and not self.mValorDato.pendingChanges())
		self.idDato = self.mValorDato.getId(l)
		self.editaDato.setEnabled(self.idDato > 0  and not self.mValorDato.pendingChanges())
		self.anadeDato.setEnabled(not self.mValorDato.pendingChanges())

	@pyqtSlot(bool)
	def on_guardaDato_clicked(self, checked):
		valido=self.mValorDato.isValidPaste(self.mFuenteClasificacion,self.idFuente)
		msj=valido[1].join("\n")
		if valido[0]:
			self.mValorDato.submitTrans()
			self.anadeDato.setEnabled(True)
		else:
			QMessageBox.warning(self, self.tr("Datos no correctos"),
				msj,
				QMessageBox.StandardButton.Ok)

	@pyqtSlot(bool)
	def on_descartaDato_clicked(self, checked):
		self.mValorDato.revertAll()
		self.anadeDato.setEnabled(True)

	def insertDataDato(self, data):
		fields = [ 'idaforo', 'iddato', 'idclasificacion', 'valor' ]
		filters = [ { 'idfuente': self.idFuente },
					{ 'idclasificacion': None },
					{},
					{} ]
		order = [ 'idaforo', 'idclasificacion', 'iddato', 'valor' ]
		self.mValorDato.addRows(fields, data, filters, order)

	@pyqtSlot(bool)
	def on_clipboardDato_triggered(self, checked):
		self.getDataFromClipboard(checked, self.insertDataDato)

	def tablaDato_contextualMenuActions(self):
		return [ self.clipboardDato ]

	##########################################################################
	# DatoTabular
	#

	@pyqtSlot(bool)
	def on_eliminaDatoTabular_clicked(self, checked):
		l = self.tablaDatoTabular.selectionModel().selection()
		while len(l) > 0:
			r = l[0]
			if r.left() == 0 and r.right() == (self.tablaDatoTabular.horizontalHeader().count() - 1):
				self.mValorDatoTabular.removeRows(r.top(), r.height(), r.parent())
				self.tablaDatoTabular_selectionChanged(QItemSelection(), QItemSelection())
			else:
				idxs = r.indexes()
				for idx in idxs:
					if idx.column() > 1:
						self.mValorDatoTabular.setData(idx, None, Qt.EditRole)
				s = QItemSelection(r.topLeft(), r.bottomRight())
				self.tablaDatoTabular.selectionModel().select(s, QItemSelectionModel.Deselect)
			l = self.tablaDatoTabular.selectionModel().selection()


	@pyqtSlot("const QItemSelection &", "const QItemSelection &")
	def tablaDatoTabular_selectionChanged(self, after, before):
		l = self.tablaDatoTabular.selectionModel().selectedIndexes()
		self.eliminaDatoTabular.setEnabled(len(l) > 0)
		self.guardaDatoTabular.setEnabled(self.mValorDatoTabular.pendingChanges())
		self.descartaDatoTabular.setEnabled(self.mValorDatoTabular.pendingChanges())

	@pyqtSlot(bool)
	def on_guardaDatoTabular_clicked(self, checked):
		self.mValorDatoTabular.submitTrans()
		self.tablaDatoTabular.resizeColumnsToContents()
		self.tablaDatoTabular.resizeRowsToContents()
		self.tablaDatoTabular_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(bool)
	def on_descartaDatoTabular_clicked(self, checked):
		self.mValorDatoTabular.select()
		self.tablaDatoTabular.resizeColumnsToContents()
		self.tablaDatoTabular.resizeRowsToContents()
		self.tablaDatoTabular_selectionChanged(QItemSelection(), QItemSelection())

	def insertDataDatoTabular(self, data):
		self.mValorDatoTabular.addRows(data)
		self.tablaDatoTabular.resizeColumnsToContents()
		self.tablaDatoTabular.resizeRowsToContents()
		self.tablaDatoTabular_selectionChanged(QItemSelection(), QItemSelection())

	@pyqtSlot(bool)
	def on_clipboardDatoTabular_triggered(self, checked):
		self.getDataFromClipboard(checked, self.insertDataDatoTabular)

	@pyqtSlot(bool)
	def on_copyHeaderDatoTabular_triggered(self, checked):
		self.copyDataToClipboard( [ self.mValorDatoTabular.headers() ] )

	def tablaDatoTabular_contextualMenuActions(self):
		return [ self.clipboardDatoTabular, self.copyHeaderDatoTabular ]

	######################################################################
	# Contaminantes validados
	#

	@pyqtSlot(int, "QSqlRecord &")
	def navValidado_primeInsert(self, row, record):
		record.setValue('idaforo', self.idAforo)



