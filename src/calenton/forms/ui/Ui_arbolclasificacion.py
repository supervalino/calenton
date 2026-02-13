# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arbolclasificacion.ui'
#
# Created: Fri Feb 21 12:06:28 2014
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

class Ui_ArbolClasificacionClass(object):
    def setupUi(self, ArbolClasificacionClass):
        ArbolClasificacionClass.setObjectName(_fromUtf8("ArbolClasificacionClass"))
        ArbolClasificacionClass.resize(572, 465)
        self.verticalLayout = QtGui.QVBoxLayout(ArbolClasificacionClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(ArbolClasificacionClass)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tablaTipos = QtGui.QTableView(self.tab_3)
        self.tablaTipos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaTipos.setObjectName(_fromUtf8("tablaTipos"))
        self.verticalLayout_3.addWidget(self.tablaTipos)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.guardaTipos = QtGui.QPushButton(self.tab_3)
        self.guardaTipos.setObjectName(_fromUtf8("guardaTipos"))
        self.horizontalLayout.addWidget(self.guardaTipos)
        self.descartaTipos = QtGui.QPushButton(self.tab_3)
        self.descartaTipos.setObjectName(_fromUtf8("descartaTipos"))
        self.horizontalLayout.addWidget(self.descartaTipos)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.eliminaTipos = QtGui.QPushButton(self.tab_3)
        self.eliminaTipos.setObjectName(_fromUtf8("eliminaTipos"))
        self.horizontalLayout.addWidget(self.eliminaTipos)
        self.editaTipos = QtGui.QPushButton(self.tab_3)
        self.editaTipos.setObjectName(_fromUtf8("editaTipos"))
        self.horizontalLayout.addWidget(self.editaTipos)
        self.anadeTipos = QtGui.QPushButton(self.tab_3)
        self.anadeTipos.setObjectName(_fromUtf8("anadeTipos"))
        self.horizontalLayout.addWidget(self.anadeTipos)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.arbolClasificacion = QtGui.QTreeView(self.tab)
        self.arbolClasificacion.setAlternatingRowColors(True)
        self.arbolClasificacion.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.arbolClasificacion.setObjectName(_fromUtf8("arbolClasificacion"))
        self.verticalLayout_2.addWidget(self.arbolClasificacion)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tablaDato = QtGui.QTableView(self.tab_2)
        self.tablaDato.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tablaDato.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaDato.setObjectName(_fromUtf8("tablaDato"))
        self.verticalLayout_4.addWidget(self.tablaDato)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.guardaDato = QtGui.QPushButton(self.tab_2)
        self.guardaDato.setObjectName(_fromUtf8("guardaDato"))
        self.horizontalLayout_2.addWidget(self.guardaDato)
        self.descartaDato = QtGui.QPushButton(self.tab_2)
        self.descartaDato.setObjectName(_fromUtf8("descartaDato"))
        self.horizontalLayout_2.addWidget(self.descartaDato)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.eliminaDato = QtGui.QPushButton(self.tab_2)
        self.eliminaDato.setObjectName(_fromUtf8("eliminaDato"))
        self.horizontalLayout_2.addWidget(self.eliminaDato)
        self.editaDato = QtGui.QPushButton(self.tab_2)
        self.editaDato.setObjectName(_fromUtf8("editaDato"))
        self.horizontalLayout_2.addWidget(self.editaDato)
        self.anadeDato = QtGui.QPushButton(self.tab_2)
        self.anadeDato.setObjectName(_fromUtf8("anadeDato"))
        self.horizontalLayout_2.addWidget(self.anadeDato)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.clipboardDato = QtGui.QAction(ArbolClasificacionClass)
        self.clipboardDato.setObjectName(_fromUtf8("clipboardDato"))

        self.retranslateUi(ArbolClasificacionClass)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.tablaDato, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), ArbolClasificacionClass.showContextMenu)
        QtCore.QMetaObject.connectSlotsByName(ArbolClasificacionClass)

    def retranslateUi(self, ArbolClasificacionClass):
        ArbolClasificacionClass.setWindowTitle(_translate("ArbolClasificacionClass", "Jerarquía de clasificación", None))
        self.guardaTipos.setText(_translate("ArbolClasificacionClass", "Guardar", None))
        self.descartaTipos.setText(_translate("ArbolClasificacionClass", "Descartar", None))
        self.eliminaTipos.setText(_translate("ArbolClasificacionClass", "Eliminar", None))
        self.editaTipos.setText(_translate("ArbolClasificacionClass", "Editar", None))
        self.anadeTipos.setText(_translate("ArbolClasificacionClass", "Añadir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("ArbolClasificacionClass", "Tipos de clasificación", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ArbolClasificacionClass", "Clasificaciones", None))
        self.guardaDato.setText(_translate("ArbolClasificacionClass", "Guardar", None))
        self.descartaDato.setText(_translate("ArbolClasificacionClass", "Descartar", None))
        self.eliminaDato.setText(_translate("ArbolClasificacionClass", "Eliminar", None))
        self.editaDato.setText(_translate("ArbolClasificacionClass", "Editar", None))
        self.anadeDato.setText(_translate("ArbolClasificacionClass", "Añadir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ArbolClasificacionClass", "Datos", None))
        self.clipboardDato.setText(_translate("ArbolClasificacionClass", "Insertar dato desde portapapeles", None))
        self.clipboardDato.setToolTip(_translate("ArbolClasificacionClass", "Insertar dato desde portapapeles", None))

from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ArbolClasificacionClass = QtGui.DataList()
    ui = Ui_ArbolClasificacionClass()
    ui.setupUi(ArbolClasificacionClass)
    ArbolClasificacionClass.show()
    sys.exit(app.exec_())

