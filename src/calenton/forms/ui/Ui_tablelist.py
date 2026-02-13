# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tablelist.ui'
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

class Ui_TableListClass(object):
    def setupUi(self, TableListClass):
        TableListClass.setObjectName(_fromUtf8("TableListClass"))
        TableListClass.resize(614, 457)
        self.verticalLayout = QtGui.QVBoxLayout(TableListClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(TableListClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.escenario = TComboBox(TableListClass)
        self.escenario.setMinimumSize(QtCore.QSize(200, 0))
        self.escenario.setObjectName(_fromUtf8("escenario"))
        self.horizontalLayout_2.addWidget(self.escenario)
        spacerItem = QtGui.QSpacerItem(168, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabla = QtGui.QTableWidget(TableListClass)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.verticalLayout.addWidget(self.tabla)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.crear = QtGui.QPushButton(TableListClass)
        self.crear.setObjectName(_fromUtf8("crear"))
        self.horizontalLayout.addWidget(self.crear)
        self.crearTodas = QtGui.QPushButton(TableListClass)
        self.crearTodas.setObjectName(_fromUtf8("crearTodas"))
        self.horizontalLayout.addWidget(self.crearTodas)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.recarga = QtGui.QPushButton(TableListClass)
        self.recarga.setObjectName(_fromUtf8("recarga"))
        self.horizontalLayout.addWidget(self.recarga)
        self.elimina = QtGui.QPushButton(TableListClass)
        self.elimina.setObjectName(_fromUtf8("elimina"))
        self.horizontalLayout.addWidget(self.elimina)
        self.edita = QtGui.QPushButton(TableListClass)
        self.edita.setObjectName(_fromUtf8("edita"))
        self.horizontalLayout.addWidget(self.edita)
        self.anade = QtGui.QPushButton(TableListClass)
        self.anade.setObjectName(_fromUtf8("anade"))
        self.horizontalLayout.addWidget(self.anade)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.insertFromClipboard = QtGui.QAction(TableListClass)
        self.insertFromClipboard.setObjectName(_fromUtf8("insertFromClipboard"))

        self.retranslateUi(TableListClass)
        QtCore.QObject.connect(self.insertFromClipboard, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), TableListClass.dataFromClipboard)
        QtCore.QMetaObject.connectSlotsByName(TableListClass)
        TableListClass.setTabOrder(self.escenario, self.tabla)
        TableListClass.setTabOrder(self.tabla, self.crear)
        TableListClass.setTabOrder(self.crear, self.crearTodas)
        TableListClass.setTabOrder(self.crearTodas, self.recarga)
        TableListClass.setTabOrder(self.recarga, self.elimina)
        TableListClass.setTabOrder(self.elimina, self.edita)
        TableListClass.setTabOrder(self.edita, self.anade)

    def retranslateUi(self, TableListClass):
        TableListClass.setWindowTitle(_translate("TableListClass", "Lista de tablas", None))
        self.label.setText(_translate("TableListClass", "Escenario:", None))
        self.crear.setText(_translate("TableListClass", "Crear Tabla", None))
        self.crearTodas.setText(_translate("TableListClass", "Crear Todas", None))
        self.recarga.setText(_translate("TableListClass", "Recargar", None))
        self.elimina.setText(_translate("TableListClass", "Eliminar", None))
        self.edita.setText(_translate("TableListClass", "Editar", None))
        self.anade.setText(_translate("TableListClass", "Añadir", None))
        self.insertFromClipboard.setText(_translate("TableListClass", "Insertar desde portapapeles", None))

from ts import TComboBox
from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TableListClass = QtGui.DataList()
    ui = Ui_TableListClass()
    ui.setupUi(TableListClass)
    TableListClass.show()
    sys.exit(app.exec_())

