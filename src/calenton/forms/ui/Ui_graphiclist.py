# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphiclist.ui'
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

class Ui_GraphicListClass(object):
    def setupUi(self, GraphicListClass):
        GraphicListClass.setObjectName(_fromUtf8("GraphicListClass"))
        GraphicListClass.resize(614, 457)
        self.verticalLayout = QtGui.QVBoxLayout(GraphicListClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(GraphicListClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.escenario = TComboBox(GraphicListClass)
        self.escenario.setMinimumSize(QtCore.QSize(200, 0))
        self.escenario.setObjectName(_fromUtf8("escenario"))
        self.horizontalLayout_2.addWidget(self.escenario)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabla = QtGui.QTableWidget(GraphicListClass)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.verticalLayout.addWidget(self.tabla)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.crear = QtGui.QPushButton(GraphicListClass)
        self.crear.setObjectName(_fromUtf8("crear"))
        self.horizontalLayout.addWidget(self.crear)
        self.crearTodas = QtGui.QPushButton(GraphicListClass)
        self.crearTodas.setObjectName(_fromUtf8("crearTodas"))
        self.horizontalLayout.addWidget(self.crearTodas)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.elimina = QtGui.QPushButton(GraphicListClass)
        self.elimina.setObjectName(_fromUtf8("elimina"))
        self.horizontalLayout.addWidget(self.elimina)
        self.edita = QtGui.QPushButton(GraphicListClass)
        self.edita.setObjectName(_fromUtf8("edita"))
        self.horizontalLayout.addWidget(self.edita)
        self.anade = QtGui.QPushButton(GraphicListClass)
        self.anade.setObjectName(_fromUtf8("anade"))
        self.horizontalLayout.addWidget(self.anade)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.insertFromClipboard = QtGui.QAction(GraphicListClass)
        self.insertFromClipboard.setObjectName(_fromUtf8("insertFromClipboard"))

        self.retranslateUi(GraphicListClass)
        QtCore.QObject.connect(self.insertFromClipboard, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), GraphicListClass.dataFromClipboard)
        QtCore.QMetaObject.connectSlotsByName(GraphicListClass)
        GraphicListClass.setTabOrder(self.escenario, self.tabla)
        GraphicListClass.setTabOrder(self.tabla, self.crear)
        GraphicListClass.setTabOrder(self.crear, self.crearTodas)
        GraphicListClass.setTabOrder(self.crearTodas, self.elimina)
        GraphicListClass.setTabOrder(self.elimina, self.edita)
        GraphicListClass.setTabOrder(self.edita, self.anade)

    def retranslateUi(self, GraphicListClass):
        GraphicListClass.setWindowTitle(_translate("GraphicListClass", "Lista de gráficos", None))
        self.label.setText(_translate("GraphicListClass", "Escenario:", None))
        self.crear.setText(_translate("GraphicListClass", "Crear Imagen", None))
        self.crearTodas.setText(_translate("GraphicListClass", "Crear Todas", None))
        self.elimina.setText(_translate("GraphicListClass", "Eliminar", None))
        self.edita.setText(_translate("GraphicListClass", "Editar", None))
        self.anade.setText(_translate("GraphicListClass", "Añadir", None))
        self.insertFromClipboard.setText(_translate("GraphicListClass", "Insertar desde portapapeles", None))

from ts import TComboBox
from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    GraphicListClass = QtGui.DataList()
    ui = Ui_GraphicListClass()
    ui.setupUi(GraphicListClass)
    GraphicListClass.show()
    sys.exit(app.exec_())

