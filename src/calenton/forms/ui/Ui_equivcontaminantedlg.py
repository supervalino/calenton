# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'equivcontaminantedlg.ui'
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

class Ui_EquivContaminanteDlgClass(object):
    def setupUi(self, EquivContaminanteDlgClass):
        EquivContaminanteDlgClass.setObjectName(_fromUtf8("EquivContaminanteDlgClass"))
        EquivContaminanteDlgClass.resize(448, 329)
        self.verticalLayout = QtGui.QVBoxLayout(EquivContaminanteDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(EquivContaminanteDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.escenario = TComboBox(EquivContaminanteDlgClass)
        self.escenario.setObjectName(_fromUtf8("escenario"))
        self.gridLayout.addWidget(self.escenario, 0, 2, 1, 1)
        self.label = QtGui.QLabel(EquivContaminanteDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.contaminante = TComboBox(EquivContaminanteDlgClass)
        self.contaminante.setObjectName(_fromUtf8("contaminante"))
        self.gridLayout.addWidget(self.contaminante, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(EquivContaminanteDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.p = QtGui.QLineEdit(EquivContaminanteDlgClass)
        self.p.setObjectName(_fromUtf8("p"))
        self.gridLayout.addWidget(self.p, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(EquivContaminanteDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.escenario)

        self.retranslateUi(EquivContaminanteDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EquivContaminanteDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EquivContaminanteDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(EquivContaminanteDlgClass)

    def retranslateUi(self, EquivContaminanteDlgClass):
        EquivContaminanteDlgClass.setWindowTitle(_translate("EquivContaminanteDlgClass", "Datos de equivalente de CO2", None))
        self.label_2.setText(_translate("EquivContaminanteDlgClass", "Escenario", None))
        self.label.setText(_translate("EquivContaminanteDlgClass", "Contaminante", None))
        self.label_4.setText(_translate("EquivContaminanteDlgClass", "Valor", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EquivContaminanteDlgClass = QtGui.DataDialog()
    ui = Ui_EquivContaminanteDlgClass()
    ui.setupUi(EquivContaminanteDlgClass)
    EquivContaminanteDlgClass.show()
    sys.exit(app.exec_())

