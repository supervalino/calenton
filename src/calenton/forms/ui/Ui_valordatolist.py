# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'valordatolist.ui'
#
# Created: Fri Feb 21 12:06:31 2014
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

class Ui_ValorDatoListClass(object):
    def setupUi(self, ValorDatoListClass):
        ValorDatoListClass.setObjectName(_fromUtf8("ValorDatoListClass"))
        ValorDatoListClass.resize(614, 549)
        self.gridLayout = QtGui.QGridLayout(ValorDatoListClass)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabla = QtGui.QTableView(ValorDatoListClass)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.gridLayout.addWidget(self.tabla, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.guardar = QtGui.QPushButton(ValorDatoListClass)
        self.guardar.setObjectName(_fromUtf8("guardar"))
        self.horizontalLayout.addWidget(self.guardar)
        self.descartar = QtGui.QPushButton(ValorDatoListClass)
        self.descartar.setObjectName(_fromUtf8("descartar"))
        self.horizontalLayout.addWidget(self.descartar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.elimina = QtGui.QPushButton(ValorDatoListClass)
        self.elimina.setObjectName(_fromUtf8("elimina"))
        self.horizontalLayout.addWidget(self.elimina)
        self.edita = QtGui.QPushButton(ValorDatoListClass)
        self.edita.setObjectName(_fromUtf8("edita"))
        self.horizontalLayout.addWidget(self.edita)
        self.anade = QtGui.QPushButton(ValorDatoListClass)
        self.anade.setObjectName(_fromUtf8("anade"))
        self.horizontalLayout.addWidget(self.anade)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(ValorDatoListClass)
        QtCore.QMetaObject.connectSlotsByName(ValorDatoListClass)
        ValorDatoListClass.setTabOrder(self.tabla, self.elimina)
        ValorDatoListClass.setTabOrder(self.elimina, self.edita)
        ValorDatoListClass.setTabOrder(self.edita, self.anade)

    def retranslateUi(self, ValorDatoListClass):
        ValorDatoListClass.setWindowTitle(_translate("ValorDatoListClass", "Valores tomados  en cada aforo", None))
        self.guardar.setText(_translate("ValorDatoListClass", "Guardar", None))
        self.descartar.setText(_translate("ValorDatoListClass", "Descartar", None))
        self.elimina.setText(_translate("ValorDatoListClass", "Eliminar", None))
        self.edita.setText(_translate("ValorDatoListClass", "Editar", None))
        self.anade.setText(_translate("ValorDatoListClass", "Añadir", None))

from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ValorDatoListClass = QtGui.DataList()
    ui = Ui_ValorDatoListClass()
    ui.setupUi(ValorDatoListClass)
    ValorDatoListClass.show()
    sys.exit(app.exec_())

