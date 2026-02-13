# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'valordatodlg.ui'
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

class Ui_ValorDatoDlgClass(object):
    def setupUi(self, ValorDatoDlgClass):
        ValorDatoDlgClass.setObjectName(_fromUtf8("ValorDatoDlgClass"))
        ValorDatoDlgClass.resize(458, 392)
        self.verticalLayout = QtGui.QVBoxLayout(ValorDatoDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(ValorDatoDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.aforo = TComboBox(ValorDatoDlgClass)
        self.aforo.setObjectName(_fromUtf8("aforo"))
        self.gridLayout.addWidget(self.aforo, 0, 1, 1, 1)
        self.label = QtGui.QLabel(ValorDatoDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.clasificacion = TComboBox(ValorDatoDlgClass)
        self.clasificacion.setObjectName(_fromUtf8("clasificacion"))
        self.gridLayout.addWidget(self.clasificacion, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ValorDatoDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.dato = TComboBox(ValorDatoDlgClass)
        self.dato.setObjectName(_fromUtf8("dato"))
        self.gridLayout.addWidget(self.dato, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(ValorDatoDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.valor = QtGui.QLineEdit(ValorDatoDlgClass)
        self.valor.setObjectName(_fromUtf8("valor"))
        self.gridLayout.addWidget(self.valor, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(ValorDatoDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.dato)
        self.label_4.setBuddy(self.valor)

        self.retranslateUi(ValorDatoDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ValorDatoDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ValorDatoDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(ValorDatoDlgClass)
        ValorDatoDlgClass.setTabOrder(self.dato, self.valor)
        ValorDatoDlgClass.setTabOrder(self.valor, self.buttonBox)

    def retranslateUi(self, ValorDatoDlgClass):
        ValorDatoDlgClass.setWindowTitle(_translate("ValorDatoDlgClass", "Valor en aforo", None))
        self.label_3.setText(_translate("ValorDatoDlgClass", "Aforo", None))
        self.label.setText(_translate("ValorDatoDlgClass", "Clasificación", None))
        self.label_2.setText(_translate("ValorDatoDlgClass", "Dato", None))
        self.label_4.setText(_translate("ValorDatoDlgClass", "Valor", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ValorDatoDlgClass = QtGui.DataDialog()
    ui = Ui_ValorDatoDlgClass()
    ui.setupUi(ValorDatoDlgClass)
    ValorDatoDlgClass.show()
    sys.exit(app.exec_())

