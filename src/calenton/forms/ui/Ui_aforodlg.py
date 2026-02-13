# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aforodlg.ui'
#
# Created: Fri Feb 21 12:06:28 2014
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

class Ui_AforoDlgClass(object):
    def setupUi(self, AforoDlgClass):
        AforoDlgClass.setObjectName(_fromUtf8("AforoDlgClass"))
        AforoDlgClass.resize(437, 335)
        self.verticalLayout = QtGui.QVBoxLayout(AforoDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(AforoDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.nombre = QtGui.QLineEdit(AforoDlgClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(AforoDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.fuente = TComboBox(AforoDlgClass)
        self.fuente.setObjectName(_fromUtf8("fuente"))
        self.gridLayout.addWidget(self.fuente, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(AforoDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.escala = QtGui.QLineEdit(AforoDlgClass)
        self.escala.setObjectName(_fromUtf8("escala"))
        self.gridLayout.addWidget(self.escala, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(AforoDlgClass)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.nivelZona = TComboBox(AforoDlgClass)
        self.nivelZona.setObjectName(_fromUtf8("nivelZona"))
        self.gridLayout.addWidget(self.nivelZona, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(AforoDlgClass)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.zona = TComboBox(AforoDlgClass)
        self.zona.setObjectName(_fromUtf8("zona"))
        self.gridLayout.addWidget(self.zona, 4, 1, 1, 1)
        self.label_7 = QtGui.QLabel(AforoDlgClass)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.tipoDatoZona = TComboBox(AforoDlgClass)
        self.tipoDatoZona.setObjectName(_fromUtf8("tipoDatoZona"))
        self.gridLayout.addWidget(self.tipoDatoZona, 5, 1, 1, 1)
        self.label = QtGui.QLabel(AforoDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.descripcion = QtGui.QTextEdit(AforoDlgClass)
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.gridLayout.addWidget(self.descripcion, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(AforoDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.fuente)
        self.label_4.setBuddy(self.escala)
        self.label_5.setBuddy(self.nivelZona)
        self.label_6.setBuddy(self.zona)
        self.label_7.setBuddy(self.tipoDatoZona)
        self.label.setBuddy(self.descripcion)

        self.retranslateUi(AforoDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AforoDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AforoDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(AforoDlgClass)
        AforoDlgClass.setTabOrder(self.nombre, self.fuente)
        AforoDlgClass.setTabOrder(self.fuente, self.escala)
        AforoDlgClass.setTabOrder(self.escala, self.nivelZona)
        AforoDlgClass.setTabOrder(self.nivelZona, self.zona)
        AforoDlgClass.setTabOrder(self.zona, self.tipoDatoZona)
        AforoDlgClass.setTabOrder(self.tipoDatoZona, self.descripcion)
        AforoDlgClass.setTabOrder(self.descripcion, self.buttonBox)

    def retranslateUi(self, AforoDlgClass):
        AforoDlgClass.setWindowTitle(_translate("AforoDlgClass", "Datos de aforo", None))
        self.label_3.setText(_translate("AforoDlgClass", "Nombre", None))
        self.label_2.setText(_translate("AforoDlgClass", "Fuente", None))
        self.label_4.setText(_translate("AforoDlgClass", "Escala", None))
        self.label_5.setText(_translate("AforoDlgClass", "Nivel de zona", None))
        self.label_6.setText(_translate("AforoDlgClass", "Zona", None))
        self.label_7.setText(_translate("AforoDlgClass", "Criterio de distribución", None))
        self.label.setText(_translate("AforoDlgClass", "Descripción", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AforoDlgClass = QtGui.DataDialog()
    ui = Ui_AforoDlgClass()
    ui.setupUi(AforoDlgClass)
    AforoDlgClass.show()
    sys.exit(app.exec_())

