# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contaminanteaforodlg.ui'
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

class Ui_ContaminanteAforoDlgClass(object):
    def setupUi(self, ContaminanteAforoDlgClass):
        ContaminanteAforoDlgClass.setObjectName(_fromUtf8("ContaminanteAforoDlgClass"))
        ContaminanteAforoDlgClass.resize(458, 392)
        self.verticalLayout = QtGui.QVBoxLayout(ContaminanteAforoDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(ContaminanteAforoDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.contaminante = TComboBox(ContaminanteAforoDlgClass)
        self.contaminante.setObjectName(_fromUtf8("contaminante"))
        self.gridLayout.addWidget(self.contaminante, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ContaminanteAforoDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.aforo = TComboBox(ContaminanteAforoDlgClass)
        self.aforo.setObjectName(_fromUtf8("aforo"))
        self.gridLayout.addWidget(self.aforo, 1, 1, 1, 1)
        self.label = QtGui.QLabel(ContaminanteAforoDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.clasificacion = TComboBox(ContaminanteAforoDlgClass)
        self.clasificacion.setObjectName(_fromUtf8("clasificacion"))
        self.gridLayout.addWidget(self.clasificacion, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(ContaminanteAforoDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.valor = QtGui.QLineEdit(ContaminanteAforoDlgClass)
        self.valor.setObjectName(_fromUtf8("valor"))
        self.gridLayout.addWidget(self.valor, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(ContaminanteAforoDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.aforo)
        self.label_4.setBuddy(self.valor)

        self.retranslateUi(ContaminanteAforoDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ContaminanteAforoDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ContaminanteAforoDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(ContaminanteAforoDlgClass)
        ContaminanteAforoDlgClass.setTabOrder(self.aforo, self.valor)
        ContaminanteAforoDlgClass.setTabOrder(self.valor, self.buttonBox)

    def retranslateUi(self, ContaminanteAforoDlgClass):
        ContaminanteAforoDlgClass.setWindowTitle(_translate("ContaminanteAforoDlgClass", "Contaminante emitido por aforo", None))
        self.label_3.setText(_translate("ContaminanteAforoDlgClass", "Contaminante", None))
        self.label_2.setText(_translate("ContaminanteAforoDlgClass", "Aforo", None))
        self.label.setText(_translate("ContaminanteAforoDlgClass", "Clasificación", None))
        self.label_4.setText(_translate("ContaminanteAforoDlgClass", "Valor", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ContaminanteAforoDlgClass = QtGui.DataDialog()
    ui = Ui_ContaminanteAforoDlgClass()
    ui.setupUi(ContaminanteAforoDlgClass)
    ContaminanteAforoDlgClass.show()
    sys.exit(app.exec_())

