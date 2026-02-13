# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motorcalculodlg.ui'
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

class Ui_MotorcalculoDialogClass(object):
    def setupUi(self, MotorcalculoDialogClass):
        MotorcalculoDialogClass.setObjectName(_fromUtf8("MotorcalculoDialogClass"))
        MotorcalculoDialogClass.resize(475, 355)
        self.verticalLayout = QtGui.QVBoxLayout(MotorcalculoDialogClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_7 = QtGui.QLabel(MotorcalculoDialogClass)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.codigo = QtGui.QLineEdit(MotorcalculoDialogClass)
        self.codigo.setObjectName(_fromUtf8("codigo"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.codigo)
        self.label_8 = QtGui.QLabel(MotorcalculoDialogClass)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.nombre = QtGui.QLineEdit(MotorcalculoDialogClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.nombre)
        self.label_10 = QtGui.QLabel(MotorcalculoDialogClass)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_10)
        self.clase = QtGui.QLineEdit(MotorcalculoDialogClass)
        self.clase.setObjectName(_fromUtf8("clase"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.clase)
        self.label_9 = QtGui.QLabel(MotorcalculoDialogClass)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.descripcion = QtGui.QTextEdit(MotorcalculoDialogClass)
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.descripcion)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(MotorcalculoDialogClass)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_7.setBuddy(self.codigo)
        self.label_8.setBuddy(self.nombre)
        self.label_10.setBuddy(self.clase)
        self.label_9.setBuddy(self.descripcion)

        self.retranslateUi(MotorcalculoDialogClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MotorcalculoDialogClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MotorcalculoDialogClass.reject)
        QtCore.QMetaObject.connectSlotsByName(MotorcalculoDialogClass)
        MotorcalculoDialogClass.setTabOrder(self.codigo, self.nombre)
        MotorcalculoDialogClass.setTabOrder(self.nombre, self.clase)
        MotorcalculoDialogClass.setTabOrder(self.clase, self.descripcion)
        MotorcalculoDialogClass.setTabOrder(self.descripcion, self.buttonBox)

    def retranslateUi(self, MotorcalculoDialogClass):
        MotorcalculoDialogClass.setWindowTitle(_translate("MotorcalculoDialogClass", "Datos de motor de cálculo", None))
        self.label_7.setText(_translate("MotorcalculoDialogClass", "Codigo", None))
        self.label_8.setText(_translate("MotorcalculoDialogClass", "Nombre", None))
        self.label_10.setText(_translate("MotorcalculoDialogClass", "Clase", None))
        self.label_9.setText(_translate("MotorcalculoDialogClass", "Descripción", None))

from ts import DataDialog

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MotorcalculoDialogClass = QtGui.DataDialog()
    ui = Ui_MotorcalculoDialogClass()
    ui.setupUi(MotorcalculoDialogClass)
    MotorcalculoDialogClass.show()
    sys.exit(app.exec_())

