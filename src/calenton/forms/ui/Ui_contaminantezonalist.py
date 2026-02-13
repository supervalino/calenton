# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contaminantezonalist.ui'
#
# Created: Fri Feb 21 12:06:29 2014
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

class Ui_ContaminanteZonaListClass(object):
    def setupUi(self, ContaminanteZonaListClass):
        ContaminanteZonaListClass.setObjectName(_fromUtf8("ContaminanteZonaListClass"))
        ContaminanteZonaListClass.resize(614, 457)
        self.gridLayout = QtGui.QGridLayout(ContaminanteZonaListClass)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabla = QtGui.QTableView(ContaminanteZonaListClass)
        self.tabla.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.gridLayout.addWidget(self.tabla, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.guardar = QtGui.QPushButton(ContaminanteZonaListClass)
        self.guardar.setObjectName(_fromUtf8("guardar"))
        self.horizontalLayout.addWidget(self.guardar)
        self.descartar = QtGui.QPushButton(ContaminanteZonaListClass)
        self.descartar.setObjectName(_fromUtf8("descartar"))
        self.horizontalLayout.addWidget(self.descartar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.elimina = QtGui.QPushButton(ContaminanteZonaListClass)
        self.elimina.setObjectName(_fromUtf8("elimina"))
        self.horizontalLayout.addWidget(self.elimina)
        self.edita = QtGui.QPushButton(ContaminanteZonaListClass)
        self.edita.setObjectName(_fromUtf8("edita"))
        self.horizontalLayout.addWidget(self.edita)
        self.anade = QtGui.QPushButton(ContaminanteZonaListClass)
        self.anade.setObjectName(_fromUtf8("anade"))
        self.horizontalLayout.addWidget(self.anade)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.insertFromClipboard = QtGui.QAction(ContaminanteZonaListClass)
        self.insertFromClipboard.setObjectName(_fromUtf8("insertFromClipboard"))

        self.retranslateUi(ContaminanteZonaListClass)
        QtCore.QObject.connect(self.insertFromClipboard, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), ContaminanteZonaListClass.dataFromClipboard)
        QtCore.QObject.connect(self.tabla, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), ContaminanteZonaListClass.showContextMenu)
        QtCore.QMetaObject.connectSlotsByName(ContaminanteZonaListClass)
        ContaminanteZonaListClass.setTabOrder(self.tabla, self.elimina)
        ContaminanteZonaListClass.setTabOrder(self.elimina, self.edita)
        ContaminanteZonaListClass.setTabOrder(self.edita, self.anade)

    def retranslateUi(self, ContaminanteZonaListClass):
        ContaminanteZonaListClass.setWindowTitle(_translate("ContaminanteZonaListClass", "Emisiones de contaminante por fuente", None))
        self.guardar.setText(_translate("ContaminanteZonaListClass", "Guardar", None))
        self.descartar.setText(_translate("ContaminanteZonaListClass", "Descartar", None))
        self.elimina.setText(_translate("ContaminanteZonaListClass", "Eliminar", None))
        self.edita.setText(_translate("ContaminanteZonaListClass", "Editar", None))
        self.anade.setText(_translate("ContaminanteZonaListClass", "Añadir", None))
        self.insertFromClipboard.setText(_translate("ContaminanteZonaListClass", "Insertar desde portapapeles", None))

from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ContaminanteZonaListClass = QtGui.DataList()
    ui = Ui_ContaminanteZonaListClass()
    ui.setupUi(ContaminanteZonaListClass)
    ContaminanteZonaListClass.show()
    sys.exit(app.exec_())

