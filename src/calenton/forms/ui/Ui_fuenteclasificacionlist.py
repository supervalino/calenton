# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuenteclasificacionlist.ui'
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

class Ui_FuenteClasificacionListClass(object):
    def setupUi(self, FuenteClasificacionListClass):
        FuenteClasificacionListClass.setObjectName(_fromUtf8("FuenteClasificacionListClass"))
        FuenteClasificacionListClass.resize(599, 308)
        self.verticalLayout = QtGui.QVBoxLayout(FuenteClasificacionListClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabla = QtGui.QTableView(FuenteClasificacionListClass)
        self.tabla.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.verticalLayout.addWidget(self.tabla)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.guarda = QtGui.QPushButton(FuenteClasificacionListClass)
        self.guarda.setObjectName(_fromUtf8("guarda"))
        self.horizontalLayout.addWidget(self.guarda)
        self.descarta = QtGui.QPushButton(FuenteClasificacionListClass)
        self.descarta.setObjectName(_fromUtf8("descarta"))
        self.horizontalLayout.addWidget(self.descarta)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.elimina = QtGui.QPushButton(FuenteClasificacionListClass)
        self.elimina.setObjectName(_fromUtf8("elimina"))
        self.horizontalLayout.addWidget(self.elimina)
        self.edita = QtGui.QPushButton(FuenteClasificacionListClass)
        self.edita.setObjectName(_fromUtf8("edita"))
        self.horizontalLayout.addWidget(self.edita)
        self.anade = QtGui.QPushButton(FuenteClasificacionListClass)
        self.anade.setObjectName(_fromUtf8("anade"))
        self.horizontalLayout.addWidget(self.anade)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.clipboardFuenteClasificacion = QtGui.QAction(FuenteClasificacionListClass)
        self.clipboardFuenteClasificacion.setObjectName(_fromUtf8("clipboardFuenteClasificacion"))

        self.retranslateUi(FuenteClasificacionListClass)
        QtCore.QObject.connect(self.tabla, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), FuenteClasificacionListClass.showContextMenu)
        QtCore.QMetaObject.connectSlotsByName(FuenteClasificacionListClass)

    def retranslateUi(self, FuenteClasificacionListClass):
        FuenteClasificacionListClass.setWindowTitle(_translate("FuenteClasificacionListClass", "Lista de clasificación por fuente...", None))
        self.guarda.setText(_translate("FuenteClasificacionListClass", "Guardar", None))
        self.descarta.setText(_translate("FuenteClasificacionListClass", "Descartar", None))
        self.elimina.setText(_translate("FuenteClasificacionListClass", "Eliminar", None))
        self.edita.setText(_translate("FuenteClasificacionListClass", "Editar", None))
        self.anade.setText(_translate("FuenteClasificacionListClass", "Añadir", None))
        self.clipboardFuenteClasificacion.setText(_translate("FuenteClasificacionListClass", "Insertar desde portapapeles", None))

from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FuenteClasificacionListClass = QtGui.DataList()
    ui = Ui_FuenteClasificacionListClass()
    ui.setupUi(FuenteClasificacionListClass)
    FuenteClasificacionListClass.show()
    sys.exit(app.exec_())

