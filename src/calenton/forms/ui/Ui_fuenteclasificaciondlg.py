# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuenteclasificaciondlg.ui'
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

class Ui_FuenteClasificacionDlgClass(object):
    def setupUi(self, FuenteClasificacionDlgClass):
        FuenteClasificacionDlgClass.setObjectName(_fromUtf8("FuenteClasificacionDlgClass"))
        FuenteClasificacionDlgClass.resize(448, 329)
        self.verticalLayout = QtGui.QVBoxLayout(FuenteClasificacionDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(FuenteClasificacionDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.nombre = QtGui.QLineEdit(FuenteClasificacionDlgClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(FuenteClasificacionDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.fuente = TComboBox(FuenteClasificacionDlgClass)
        self.fuente.setObjectName(_fromUtf8("fuente"))
        self.gridLayout.addWidget(self.fuente, 1, 2, 1, 1)
        self.label = QtGui.QLabel(FuenteClasificacionDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.clasificacion = TComboBox(FuenteClasificacionDlgClass)
        self.clasificacion.setObjectName(_fromUtf8("clasificacion"))
        self.gridLayout.addWidget(self.clasificacion, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(FuenteClasificacionDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.fuente)

        self.retranslateUi(FuenteClasificacionDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FuenteClasificacionDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FuenteClasificacionDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(FuenteClasificacionDlgClass)
        FuenteClasificacionDlgClass.setTabOrder(self.nombre, self.fuente)

    def retranslateUi(self, FuenteClasificacionDlgClass):
        FuenteClasificacionDlgClass.setWindowTitle(_translate("FuenteClasificacionDlgClass", "Datos de tipo de clasificación por fuente", None))
        self.label_3.setText(_translate("FuenteClasificacionDlgClass", "Nombre", None))
        self.label_2.setText(_translate("FuenteClasificacionDlgClass", "Fuente", None))
        self.label.setText(_translate("FuenteClasificacionDlgClass", "Clasificación", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FuenteClasificacionDlgClass = QtGui.DataDialog()
    ui = Ui_FuenteClasificacionDlgClass()
    ui.setupUi(FuenteClasificacionDlgClass)
    FuenteClasificacionDlgClass.show()
    sys.exit(app.exec_())

