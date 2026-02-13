# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tipoclaslist.ui'
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

class Ui_TipoclasListClass(object):
    def setupUi(self, TipoclasListClass):
        TipoclasListClass.setObjectName(_fromUtf8("TipoclasListClass"))
        TipoclasListClass.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(TipoclasListClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabla = QtGui.QTableView(TipoclasListClass)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.verticalLayout.addWidget(self.tabla)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.anade = QtGui.QPushButton(TipoclasListClass)
        self.anade.setObjectName(_fromUtf8("anade"))
        self.horizontalLayout.addWidget(self.anade)
        self.edita = QtGui.QPushButton(TipoclasListClass)
        self.edita.setEnabled(False)
        self.edita.setObjectName(_fromUtf8("edita"))
        self.horizontalLayout.addWidget(self.edita)
        self.elimina = QtGui.QPushButton(TipoclasListClass)
        self.elimina.setEnabled(False)
        self.elimina.setObjectName(_fromUtf8("elimina"))
        self.horizontalLayout.addWidget(self.elimina)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(TipoclasListClass)
        QtCore.QMetaObject.connectSlotsByName(TipoclasListClass)
        TipoclasListClass.setTabOrder(self.tabla, self.anade)
        TipoclasListClass.setTabOrder(self.anade, self.edita)
        TipoclasListClass.setTabOrder(self.edita, self.elimina)

    def retranslateUi(self, TipoclasListClass):
        TipoclasListClass.setWindowTitle(_translate("TipoclasListClass", "Tipo de clasificación ...", None))
        self.anade.setText(_translate("TipoclasListClass", "Añadir...", None))
        self.edita.setText(_translate("TipoclasListClass", "Editar...", None))
        self.elimina.setText(_translate("TipoclasListClass", "Eliminar", None))

from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TipoclasListClass = QtGui.DataList()
    ui = Ui_TipoclasListClass()
    ui.setupUi(TipoclasListClass)
    TipoclasListClass.show()
    sys.exit(app.exec_())

