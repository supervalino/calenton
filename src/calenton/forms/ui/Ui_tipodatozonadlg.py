# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tipodatozonadlg.ui'
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

class Ui_TipoDatoZonaDlgClass(object):
    def setupUi(self, TipoDatoZonaDlgClass):
        TipoDatoZonaDlgClass.setObjectName(_fromUtf8("TipoDatoZonaDlgClass"))
        TipoDatoZonaDlgClass.resize(370, 203)
        self.verticalLayout = QtGui.QVBoxLayout(TipoDatoZonaDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(TipoDatoZonaDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(TipoDatoZonaDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.nombre = QtGui.QLineEdit(TipoDatoZonaDlgClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.nombre)
        self.label_3 = QtGui.QLabel(TipoDatoZonaDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.unidades = QtGui.QLineEdit(TipoDatoZonaDlgClass)
        self.unidades.setObjectName(_fromUtf8("unidades"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.unidades)
        self.escenario = TComboBox(TipoDatoZonaDlgClass)
        self.escenario.setObjectName(_fromUtf8("escenario"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.escenario)
        self.variable = QtGui.QLineEdit(TipoDatoZonaDlgClass)
        self.variable.setObjectName(_fromUtf8("variable"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.variable)
        self.label_4 = QtGui.QLabel(TipoDatoZonaDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.defecto = QtGui.QLineEdit(TipoDatoZonaDlgClass)
        self.defecto.setObjectName(_fromUtf8("defecto"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.defecto)
        self.label_5 = QtGui.QLabel(TipoDatoZonaDlgClass)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(TipoDatoZonaDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.escenario)
        self.label_2.setBuddy(self.nombre)
        self.label_3.setBuddy(self.unidades)
        self.label_4.setBuddy(self.variable)
        self.label_5.setBuddy(self.defecto)

        self.retranslateUi(TipoDatoZonaDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TipoDatoZonaDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TipoDatoZonaDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(TipoDatoZonaDlgClass)
        TipoDatoZonaDlgClass.setTabOrder(self.escenario, self.nombre)
        TipoDatoZonaDlgClass.setTabOrder(self.nombre, self.variable)
        TipoDatoZonaDlgClass.setTabOrder(self.variable, self.defecto)
        TipoDatoZonaDlgClass.setTabOrder(self.defecto, self.unidades)
        TipoDatoZonaDlgClass.setTabOrder(self.unidades, self.buttonBox)

    def retranslateUi(self, TipoDatoZonaDlgClass):
        TipoDatoZonaDlgClass.setWindowTitle(_translate("TipoDatoZonaDlgClass", "Tipos de datos por zona", None))
        self.label.setText(_translate("TipoDatoZonaDlgClass", "Escenario", None))
        self.label_2.setText(_translate("TipoDatoZonaDlgClass", "Nombre", None))
        self.label_3.setText(_translate("TipoDatoZonaDlgClass", "Unidades", None))
        self.label_4.setText(_translate("TipoDatoZonaDlgClass", "Variable JavaScript", None))
        self.label_5.setText(_translate("TipoDatoZonaDlgClass", "Valor por defecto", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TipoDatoZonaDlgClass = QtGui.DataDialog()
    ui = Ui_TipoDatoZonaDlgClass()
    ui.setupUi(TipoDatoZonaDlgClass)
    TipoDatoZonaDlgClass.show()
    sys.exit(app.exec_())

