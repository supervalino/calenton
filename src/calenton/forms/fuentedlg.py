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
# $Id: fuentedlg.py 255 2010-05-19 09:24:46Z bruno $
# $URL: https://www.litec.csic.es/svn/emisiones/trunk/src/calenton/forms/fuentedlg.py $
#
##############################################################################

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from modelo import *
from ui import Ui_fuentedlg
from ui.Ui_fuentedlg import *
from ts import DataDialog
from ts import ForeignKey
from ts import ComboDataModel

class FuenteDlg (DataDialog, Ui_fuentedlg.Ui_FuenteDlgClass):
	def __init__(self, parent, dataModel):
		DataDialog.__init__(self, parent, dataModel)
		self.setupUi(self)
		self.dialogoPadre=parent
		self.model=dataModel
		self.db = self.model.database()
		self.app = QApplication.instance()
		# combobox de escenarios
		self.modelCbEsc = escenario.Escenario(parent, self.app.work)
		self.modelCbEsc.select()
		parent.putCombobox(self.escenario, self.modelCbEsc, 'nombre')
		# combobox de origen
		self.modelCbOri = self.model.foreignKey('idorigen').model(
						{ 'idescenario' : QVariant(-1) },
						False)
		self.origen.setModel(self.modelCbOri)
		# combobox de motorcalculo
		self.modelCbMtc = motorcalculo.MotorCalculo(parent, self.app.work)
		self.modelCbMtc.select()
		parent.putCombobox(self.motorcalculo, self.modelCbMtc, 'nombre')
		# combobox de clasificacion
		self.modelCbCls = clasificacion.Clasificacion(parent, self.app.work)
		self.modelCbCls.select()
		parent.putCombobox(self.clasificacion, self.modelCbCls, 'codigo', 'descripcion')
		# lista de clasificaciones
		self.modelLtCls = clasificacion.Clasificacion(parent, self.app.work)
		self.modelLtCls.select()
		
		self.modelNivelZona = ComboDataModel(self, True, self.tr('No asociado'))
		self.modelNivelZona.setQuery("select id, nombre from nivelzona order by nombre", self.db)
		self.nivelZona.setModel(self.modelNivelZona)
		
		self.modelTipoDato = ComboDataModel(self, True, self.tr('Sin distribución automática'))
		self.modelTipoDato = self.model.foreignKey('idtipodatozona').model(
							{'idescenario': QVariant(-1)}, 
							True, 
							self.tr('Sin distribución automática'))
		self.tipoDatoZona.setModel(self.modelTipoDato)
		
	def putData(self, r):
		self.modelFteCls = self.app.mFuenteClasificacion
		self.nombre.setText(r.value('nombre').toString())
		(self.id,good) = r.value('id').toInt()
		self.escenario.setCurrentItemData(r.value('idescenario'))
		self.modelCbOri.setFilters({ 'idescenario': r.value('idescenario') })
		self.origen.setCurrentItemData(r.value('idorigen'))
		self.motorcalculo.setCurrentItemData(r.value('idmotorcalculo'))
		self.nivelZona.setCurrentItemData(r.value('idnivelzona'))
		self.modelTipoDato.setFilters({ 'idescenario': r.value('idescenario') })
		self.tipoDatoZona.setCurrentItemData(r.value('idtipodatozona'))
		# lista de clasificacioines
		self.filtraClasificacion()
		self.listaclasificacion.setModel(self.modelLtCls)
		self.dialogoPadre.cambiaEncabezado(self.modelLtCls, ['Código', 'Descripción'])
		self.listaclasificacion.hideColumn(self.modelLtCls.fieldIndex("id"))
		self.listaclasificacion.resizeColumnsToContents()

		return True
		
	def getData(self, r):
		if self.nombre.text().trimmed().isEmpty():
			self.setEditionError(self.tr("El nombre no puede estar vacío"))
			return False
		r.setValue('nombre', self.nombre.text().trimmed())
		r.setValue('idescenario', self.escenario.currentItemData())
		r.setValue('idorigen', self.origen.currentItemData())
		r.setValue('idmotorcalculo', self.motorcalculo.currentItemData())
		r.setValue('idnivelzona', self.nivelZona.currentItemData())
		r.setValue('idtipodatozona', self.tipoDatoZona.currentItemData())
		return True

	def filtraClasificacion(self):
		query = QSqlQuery(self.model.database())
		query.exec_("select fuenteclasificacion.id, clasificacion.codigo,clasificacion.descripcion\
									from fuenteclasificacion,clasificacion \
									where clasificacion.id=fuenteclasificacion.idclasificacion\
									and fuenteclasificacion.idfuente= %d" % self.id)
		self.modelLtCls.setQuery(query)
		
	@pyqtSlot("int")
	def on_escenario_activated(self, index):
		idescenario = self.escenario.currentItemData()
		itdz = self.tipoDatoZona.currentItemData()
		self.modelTipoDato.setFilters({ 'idescenario': idescenario })
		self.tipoDatoZona.setCurrentItemData(itdz)
		io = self.origen.currentItemData()
		self.modelCbOri.setFilters({ 'idescenario': idescenario })
		self.origen.setCurrentItemData(io)

	@pyqtSlot("bool")
	def on_asignaclasificacion_clicked(self, checked):
		i_sel=self.clasificacion.currentIndex()
		r=self.modelFteCls.record(0) # registro para plantilla
		(id_clas, good) = self.modelCbCls.record(i_sel).value('id').toInt()
		r.setNull('id')
		self.modelFteCls.calcSeq(r)
		r.setValue('idfuente', self.id)
		r.setValue('idclasificacion', id_clas)
		self.dialogoPadre.askAndAddRow(r, self.modelFteCls)		
		self.filtraClasificacion()
		return True

	@pyqtSlot("bool")
	def on_borraclasificacion_clicked(self, checked):
#		self.dialogoPadre.askAndRemoveRows(self.listaclasificacion, self.modelFteCls)
#		self.modelFteCls.askAndRemoveRows(self.listaclasificacion, self.modelFteCls)
			
		res = QMessageBox.question(self, self.tr("¿Está seguro?"),
				self.tr("¿Desea eliminar los registros seleccionados?\n" +
					"Esta operación es permanente e irreversible"),
				QMessageBox.Yes | QMessageBox.Escape,
				QMessageBox.No | QMessageBox.Default)
		if res != QMessageBox.Yes:
			return
		l = self.listaclasificacion.selectedIndexes()
		if len(l) == 0:
			return
		query = QSqlQuery(self.model.database())
		l1 = []
		for i in l:
			if not i.column() == 1:
				continue
			cod = i.data().toString()
			query.exec_("select id from clasificacion where codigo = '%s'" % cod)
			if not query.first():
				return
			l1.append(query.record().value('id').toInt()[0])
			
		l0 = l1.pop(0)
		sql = QString("delete from fuenteclasificacion \
					where idfuente = %d and idclasificacion = %d" % (self.id, l0))
		for i in l1:
			sql.append(" or (idfuente = %d and idclasificacion = %d)" % (self.id, i) )
		query.exec_(sql)
		self.filtraClasificacion()
