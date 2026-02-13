# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'elegirescenariodlg.ui'
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

class Ui_ElegirEscenarioDlgClass(object):
    def setupUi(self, ElegirEscenarioDlgClass):
        ElegirEscenarioDlgClass.setObjectName(_fromUtf8("ElegirEscenarioDlgClass"))
        ElegirEscenarioDlgClass.resize(273, 90)
        self.verticalLayout = QtGui.QVBoxLayout(ElegirEscenarioDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(ElegirEscenarioDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.escenario = TComboBox(ElegirEscenarioDlgClass)
        self.escenario.setObjectName(_fromUtf8("escenario"))
        self.horizontalLayout.addWidget(self.escenario)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(ElegirEscenarioDlgClass)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.escenario)

        self.retranslateUi(ElegirEscenarioDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ElegirEscenarioDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ElegirEscenarioDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(ElegirEscenarioDlgClass)
        ElegirEscenarioDlgClass.setTabOrder(self.escenario, self.buttonBox)

    def retranslateUi(self, ElegirEscenarioDlgClass):
        ElegirEscenarioDlgClass.setWindowTitle(_translate("ElegirEscenarioDlgClass", "Elija un escenario", None))
        self.label.setText(_translate("ElegirEscenarioDlgClass", "Escenario", None))

from ts import TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ElegirEscenarioDlgClass = QtGui.QDialog()
    ui = Ui_ElegirEscenarioDlgClass()
    ui.setupUi(ElegirEscenarioDlgClass)
    ElegirEscenarioDlgClass.show()
    sys.exit(app.exec_())

