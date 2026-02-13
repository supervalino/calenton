# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'equivcontaminantelist.ui'
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

class Ui_EquivContaminanteListClass(object):
    def setupUi(self, EquivContaminanteListClass):
        EquivContaminanteListClass.setObjectName(_fromUtf8("EquivContaminanteListClass"))
        EquivContaminanteListClass.resize(412, 308)
        self.verticalLayout = QtGui.QVBoxLayout(EquivContaminanteListClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabla = QtGui.QTableView(EquivContaminanteListClass)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.verticalLayout.addWidget(self.tabla)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.elimina = QtGui.QPushButton(EquivContaminanteListClass)
        self.elimina.setObjectName(_fromUtf8("elimina"))
        self.horizontalLayout.addWidget(self.elimina)
        self.edita = QtGui.QPushButton(EquivContaminanteListClass)
        self.edita.setObjectName(_fromUtf8("edita"))
        self.horizontalLayout.addWidget(self.edita)
        self.anade = QtGui.QPushButton(EquivContaminanteListClass)
        self.anade.setObjectName(_fromUtf8("anade"))
        self.horizontalLayout.addWidget(self.anade)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(EquivContaminanteListClass)
        QtCore.QMetaObject.connectSlotsByName(EquivContaminanteListClass)

    def retranslateUi(self, EquivContaminanteListClass):
        EquivContaminanteListClass.setWindowTitle(_translate("EquivContaminanteListClass", "Lista de equivalentes de CO2", None))
        self.elimina.setText(_translate("EquivContaminanteListClass", "Eliminar", None))
        self.edita.setText(_translate("EquivContaminanteListClass", "Editar", None))
        self.anade.setText(_translate("EquivContaminanteListClass", "Añadir", None))

from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EquivContaminanteListClass = QtGui.DataList()
    ui = Ui_EquivContaminanteListClass()
    ui.setupUi(EquivContaminanteListClass)
    EquivContaminanteListClass.show()
    sys.exit(app.exec_())

