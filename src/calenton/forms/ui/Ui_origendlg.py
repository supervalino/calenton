# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'origendlg.ui'
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

class Ui_OrigenDlgClass(object):
    def setupUi(self, OrigenDlgClass):
        OrigenDlgClass.setObjectName(_fromUtf8("OrigenDlgClass"))
        OrigenDlgClass.resize(306, 313)
        self.verticalLayout = QtGui.QVBoxLayout(OrigenDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(OrigenDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.nombre = QtGui.QLineEdit(OrigenDlgClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(OrigenDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.escenario = TComboBox(OrigenDlgClass)
        self.escenario.setObjectName(_fromUtf8("escenario"))
        self.gridLayout.addWidget(self.escenario, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(OrigenDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.escenario)

        self.retranslateUi(OrigenDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), OrigenDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), OrigenDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(OrigenDlgClass)
        OrigenDlgClass.setTabOrder(self.nombre, self.escenario)

    def retranslateUi(self, OrigenDlgClass):
        OrigenDlgClass.setWindowTitle(_translate("OrigenDlgClass", "Datos de origen", None))
        self.label_3.setText(_translate("OrigenDlgClass", "Nombre", None))
        self.label_2.setText(_translate("OrigenDlgClass", "Escenario", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    OrigenDlgClass = QtGui.DataDialog()
    ui = Ui_OrigenDlgClass()
    ui.setupUi(OrigenDlgClass)
    OrigenDlgClass.show()
    sys.exit(app.exec_())

