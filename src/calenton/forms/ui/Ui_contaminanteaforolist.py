# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contaminanteaforolist.ui'
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

class Ui_ContaminanteAforoListClass(object):
    def setupUi(self, ContaminanteAforoListClass):
        ContaminanteAforoListClass.setObjectName(_fromUtf8("ContaminanteAforoListClass"))
        ContaminanteAforoListClass.resize(677, 558)
        self.gridLayout = QtGui.QGridLayout(ContaminanteAforoListClass)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabla = QtGui.QTableView(ContaminanteAforoListClass)
        self.tabla.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.gridLayout.addWidget(self.tabla, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.guardar = QtGui.QPushButton(ContaminanteAforoListClass)
        self.guardar.setObjectName(_fromUtf8("guardar"))
        self.horizontalLayout.addWidget(self.guardar)
        self.descartar = QtGui.QPushButton(ContaminanteAforoListClass)
        self.descartar.setObjectName(_fromUtf8("descartar"))
        self.horizontalLayout.addWidget(self.descartar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.elimina = QtGui.QPushButton(ContaminanteAforoListClass)
        self.elimina.setObjectName(_fromUtf8("elimina"))
        self.horizontalLayout.addWidget(self.elimina)
        self.edita = QtGui.QPushButton(ContaminanteAforoListClass)
        self.edita.setObjectName(_fromUtf8("edita"))
        self.horizontalLayout.addWidget(self.edita)
        self.anade = QtGui.QPushButton(ContaminanteAforoListClass)
        self.anade.setObjectName(_fromUtf8("anade"))
        self.horizontalLayout.addWidget(self.anade)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.clipboardContaminanteAforo = QtGui.QAction(ContaminanteAforoListClass)
        self.clipboardContaminanteAforo.setObjectName(_fromUtf8("clipboardContaminanteAforo"))

        self.retranslateUi(ContaminanteAforoListClass)
        QtCore.QObject.connect(self.tabla, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), ContaminanteAforoListClass.showContextMenu)
        QtCore.QMetaObject.connectSlotsByName(ContaminanteAforoListClass)
        ContaminanteAforoListClass.setTabOrder(self.tabla, self.elimina)
        ContaminanteAforoListClass.setTabOrder(self.elimina, self.edita)
        ContaminanteAforoListClass.setTabOrder(self.edita, self.anade)

    def retranslateUi(self, ContaminanteAforoListClass):
        ContaminanteAforoListClass.setWindowTitle(_translate("ContaminanteAforoListClass", "Contribución de contaminantes en cada aforo", None))
        self.guardar.setText(_translate("ContaminanteAforoListClass", "Guardar", None))
        self.descartar.setText(_translate("ContaminanteAforoListClass", "Descartar", None))
        self.elimina.setText(_translate("ContaminanteAforoListClass", "Eliminar", None))
        self.edita.setText(_translate("ContaminanteAforoListClass", "Editar", None))
        self.anade.setText(_translate("ContaminanteAforoListClass", "Añadir", None))
        self.clipboardContaminanteAforo.setText(_translate("ContaminanteAforoListClass", "Inserta desde portapapeles", None))
        self.clipboardContaminanteAforo.setToolTip(_translate("ContaminanteAforoListClass", "Inserta desde portapapeles", None))

from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ContaminanteAforoListClass = QtGui.DataList()
    ui = Ui_ContaminanteAforoListClass()
    ui.setupUi(ContaminanteAforoListClass)
    ContaminanteAforoListClass.show()
    sys.exit(app.exec_())

