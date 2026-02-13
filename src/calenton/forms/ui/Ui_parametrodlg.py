# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parametrodlg.ui'
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

class Ui_ParametroDlgClass(object):
    def setupUi(self, ParametroDlgClass):
        ParametroDlgClass.setObjectName(_fromUtf8("ParametroDlgClass"))
        ParametroDlgClass.resize(545, 542)
        self.verticalLayout = QtGui.QVBoxLayout(ParametroDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(ParametroDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.nombre = QtGui.QLineEdit(ParametroDlgClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ParametroDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.escenario = TComboBox(ParametroDlgClass)
        self.escenario.setObjectName(_fromUtf8("escenario"))
        self.gridLayout.addWidget(self.escenario, 1, 1, 1, 1)
        self.label = QtGui.QLabel(ParametroDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.valor = QtGui.QLineEdit(ParametroDlgClass)
        self.valor.setObjectName(_fromUtf8("valor"))
        self.gridLayout.addWidget(self.valor, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(ParametroDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.descripcion = QtGui.QTextEdit(ParametroDlgClass)
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.gridLayout.addWidget(self.descripcion, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(206, 183, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(ParametroDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.escenario)

        self.retranslateUi(ParametroDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ParametroDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ParametroDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(ParametroDlgClass)
        ParametroDlgClass.setTabOrder(self.nombre, self.escenario)

    def retranslateUi(self, ParametroDlgClass):
        ParametroDlgClass.setWindowTitle(_translate("ParametroDlgClass", "Datos de parámetro", None))
        self.label_3.setText(_translate("ParametroDlgClass", "Nombre", None))
        self.label_2.setText(_translate("ParametroDlgClass", "Escenario", None))
        self.label.setText(_translate("ParametroDlgClass", "Valor", None))
        self.label_4.setText(_translate("ParametroDlgClass", "Descripción", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ParametroDlgClass = QtGui.DataDialog()
    ui = Ui_ParametroDlgClass()
    ui.setupUi(ParametroDlgClass)
    ParametroDlgClass.show()
    sys.exit(app.exec_())

