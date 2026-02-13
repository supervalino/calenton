# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'escenariodlg.ui'
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

class Ui_EscenarioDlgClass(object):
    def setupUi(self, EscenarioDlgClass):
        EscenarioDlgClass.setObjectName(_fromUtf8("EscenarioDlgClass"))
        EscenarioDlgClass.resize(331, 85)
        self.verticalLayout = QtGui.QVBoxLayout(EscenarioDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(EscenarioDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.nombre = QtGui.QLineEdit(EscenarioDlgClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.horizontalLayout.addWidget(self.nombre)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(EscenarioDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.nombre)

        self.retranslateUi(EscenarioDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EscenarioDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EscenarioDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(EscenarioDlgClass)
        EscenarioDlgClass.setTabOrder(self.nombre, self.buttonBox)

    def retranslateUi(self, EscenarioDlgClass):
        EscenarioDlgClass.setWindowTitle(_translate("EscenarioDlgClass", "Datos de escenario", None))
        self.label.setText(_translate("EscenarioDlgClass", "Nombre", None))

from ts import DataDialog

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EscenarioDlgClass = QtGui.DataDialog()
    ui = Ui_EscenarioDlgClass()
    ui.setupUi(EscenarioDlgClass)
    EscenarioDlgClass.show()
    sys.exit(app.exec_())

