# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contaminantezonadlg.ui'
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

class Ui_ContaminanteZonaDlgClass(object):
    def setupUi(self, ContaminanteZonaDlgClass):
        ContaminanteZonaDlgClass.setObjectName(_fromUtf8("ContaminanteZonaDlgClass"))
        ContaminanteZonaDlgClass.resize(728, 396)
        self.verticalLayout = QtGui.QVBoxLayout(ContaminanteZonaDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(ContaminanteZonaDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.contaminante = TComboBox(ContaminanteZonaDlgClass)
        self.contaminante.setObjectName(_fromUtf8("contaminante"))
        self.gridLayout.addWidget(self.contaminante, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ContaminanteZonaDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.fuente = TComboBox(ContaminanteZonaDlgClass)
        self.fuente.setObjectName(_fromUtf8("fuente"))
        self.gridLayout.addWidget(self.fuente, 1, 1, 1, 1)
        self.label = QtGui.QLabel(ContaminanteZonaDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.clasificacion = TComboBox(ContaminanteZonaDlgClass)
        self.clasificacion.setObjectName(_fromUtf8("clasificacion"))
        self.gridLayout.addWidget(self.clasificacion, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(ContaminanteZonaDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.valor = QtGui.QLineEdit(ContaminanteZonaDlgClass)
        self.valor.setObjectName(_fromUtf8("valor"))
        self.gridLayout.addWidget(self.valor, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(ContaminanteZonaDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.contaminante)
        self.label_2.setBuddy(self.fuente)
        self.label_4.setBuddy(self.valor)

        self.retranslateUi(ContaminanteZonaDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ContaminanteZonaDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ContaminanteZonaDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(ContaminanteZonaDlgClass)
        ContaminanteZonaDlgClass.setTabOrder(self.contaminante, self.fuente)
        ContaminanteZonaDlgClass.setTabOrder(self.fuente, self.valor)
        ContaminanteZonaDlgClass.setTabOrder(self.valor, self.buttonBox)

    def retranslateUi(self, ContaminanteZonaDlgClass):
        ContaminanteZonaDlgClass.setWindowTitle(_translate("ContaminanteZonaDlgClass", "Emisión de contaminantes por fuente ", None))
        self.label_3.setText(_translate("ContaminanteZonaDlgClass", "Contaminante", None))
        self.label_2.setText(_translate("ContaminanteZonaDlgClass", "Fuente", None))
        self.label.setText(_translate("ContaminanteZonaDlgClass", "Clasificación", None))
        self.label_4.setText(_translate("ContaminanteZonaDlgClass", "Valor", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ContaminanteZonaDlgClass = QtGui.DataDialog()
    ui = Ui_ContaminanteZonaDlgClass()
    ui.setupUi(ContaminanteZonaDlgClass)
    ContaminanteZonaDlgClass.show()
    sys.exit(app.exec_())

