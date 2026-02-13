# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapaforozonalist.ui'
#
# Created: Fri Feb 21 12:06:30 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MapAforoZonaListClass(object):
    def setupUi(self, MapAforoZonaListClass):
        MapAforoZonaListClass.setObjectName(_fromUtf8("MapAforoZonaListClass"))
        MapAforoZonaListClass.resize(492, 370)
        self.verticalLayout_2 = QtGui.QVBoxLayout(MapAforoZonaListClass)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tablaDatos = QtGui.QTabWidget(MapAforoZonaListClass)
        self.tablaDatos.setObjectName(_fromUtf8("tablaDatos"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.comboEscenario = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboEscenario.sizePolicy().hasHeightForWidth())
        self.comboEscenario.setSizePolicy(sizePolicy)
        self.comboEscenario.setObjectName(_fromUtf8("comboEscenario"))
        self.horizontalLayout_2.addWidget(self.comboEscenario)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tablaFuentes = QtGui.QTableView(self.tab)
        self.tablaFuentes.setObjectName(_fromUtf8("tablaFuentes"))
        self.verticalLayout_3.addWidget(self.tablaFuentes)
        self.tablaDatos.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboTipoClasificacion = QtGui.QComboBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboTipoClasificacion.sizePolicy().hasHeightForWidth())
        self.comboTipoClasificacion.setSizePolicy(sizePolicy)
        self.comboTipoClasificacion.setObjectName(_fromUtf8("comboTipoClasificacion"))
        self.horizontalLayout_3.addWidget(self.comboTipoClasificacion)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.treeView = QtGui.QTreeView(self.tab_2)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout_4.addWidget(self.treeView)
        self.tablaDatos.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.tableView_2 = QtGui.QTableView(self.tab_4)
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.verticalLayout_5.addWidget(self.tableView_2)
        self.tablaDatos.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tablaMap = QtGui.QTableView(self.tab_3)
        self.tablaMap.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tablaMap.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.tablaMap.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaMap.setObjectName(_fromUtf8("tablaMap"))
        self.verticalLayout.addWidget(self.tablaMap)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.guardar = QtGui.QPushButton(self.tab_3)
        self.guardar.setObjectName(_fromUtf8("guardar"))
        self.horizontalLayout.addWidget(self.guardar)
        self.descartar = QtGui.QPushButton(self.tab_3)
        self.descartar.setObjectName(_fromUtf8("descartar"))
        self.horizontalLayout.addWidget(self.descartar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.elimina = QtGui.QPushButton(self.tab_3)
        self.elimina.setObjectName(_fromUtf8("elimina"))
        self.horizontalLayout.addWidget(self.elimina)
        self.edita = QtGui.QPushButton(self.tab_3)
        self.edita.setObjectName(_fromUtf8("edita"))
        self.horizontalLayout.addWidget(self.edita)
        self.anade = QtGui.QPushButton(self.tab_3)
        self.anade.setObjectName(_fromUtf8("anade"))
        self.horizontalLayout.addWidget(self.anade)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tablaDatos.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tablaDatos)
        self.insertFromClipboard = QtGui.QAction(MapAforoZonaListClass)
        self.insertFromClipboard.setObjectName(_fromUtf8("insertFromClipboard"))
        self.deleteAll = QtGui.QAction(MapAforoZonaListClass)
        self.deleteAll.setObjectName(_fromUtf8("deleteAll"))
        self.surfaceGeneration = QtGui.QAction(MapAforoZonaListClass)
        self.surfaceGeneration.setObjectName(_fromUtf8("surfaceGeneration"))
        self.one2OneGeneration = QtGui.QAction(MapAforoZonaListClass)
        self.one2OneGeneration.setObjectName(_fromUtf8("one2OneGeneration"))

        self.retranslateUi(MapAforoZonaListClass)
        self.tablaDatos.setCurrentIndex(0)
        QtCore.QObject.connect(self.tablaMap, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), MapAforoZonaListClass.showContextMenu)
        QtCore.QMetaObject.connectSlotsByName(MapAforoZonaListClass)
        MapAforoZonaListClass.setTabOrder(self.tablaMap, self.elimina)
        MapAforoZonaListClass.setTabOrder(self.elimina, self.edita)
        MapAforoZonaListClass.setTabOrder(self.edita, self.anade)

    def retranslateUi(self, MapAforoZonaListClass):
        MapAforoZonaListClass.setWindowTitle(_translate("MapAforoZonaListClass", "Contribución de contaminantes por aforo y zona", None))
        self.label.setText(_translate("MapAforoZonaListClass", "Escenario", None))
        self.tablaDatos.setTabText(self.tablaDatos.indexOf(self.tab), _translate("MapAforoZonaListClass", "Fuentes", None))
        self.label_2.setText(_translate("MapAforoZonaListClass", "Tipo  de clasificación", None))
        self.tablaDatos.setTabText(self.tablaDatos.indexOf(self.tab_2), _translate("MapAforoZonaListClass", "Clasificación", None))
        self.tablaDatos.setTabText(self.tablaDatos.indexOf(self.tab_4), _translate("MapAforoZonaListClass", "Datos", None))
        self.guardar.setText(_translate("MapAforoZonaListClass", "Guardar", None))
        self.descartar.setText(_translate("MapAforoZonaListClass", "Descartar", None))
        self.elimina.setText(_translate("MapAforoZonaListClass", "Eliminar", None))
        self.edita.setText(_translate("MapAforoZonaListClass", "Editar", None))
        self.anade.setText(_translate("MapAforoZonaListClass", "Añadir", None))
        self.tablaDatos.setTabText(self.tablaDatos.indexOf(self.tab_3), _translate("MapAforoZonaListClass", "Distribución por zona", None))
        self.insertFromClipboard.setText(_translate("MapAforoZonaListClass", "Insertar desde portapapeles", None))
        self.deleteAll.setText(_translate("MapAforoZonaListClass", "Borrar todos", None))
        self.surfaceGeneration.setText(_translate("MapAforoZonaListClass", "Generar por superficie", None))
        self.one2OneGeneration.setText(_translate("MapAforoZonaListClass", "Generar uno a uno", None))

from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MapAforoZonaListClass = QtGui.DataList()
    ui = Ui_MapAforoZonaListClass()
    ui.setupUi(MapAforoZonaListClass)
    MapAforoZonaListClass.show()
    sys.exit(app.exec_())

