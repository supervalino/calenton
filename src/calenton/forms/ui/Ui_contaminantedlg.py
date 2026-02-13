# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contaminantedlg.ui'
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

class Ui_ContaminanteDlgClass(object):
    def setupUi(self, ContaminanteDlgClass):
        ContaminanteDlgClass.setObjectName(_fromUtf8("ContaminanteDlgClass"))
        ContaminanteDlgClass.resize(464, 420)
        self.verticalLayout = QtGui.QVBoxLayout(ContaminanteDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(ContaminanteDlgClass)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.nombre = QtGui.QLineEdit(ContaminanteDlgClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)
        self.label = QtGui.QLabel(ContaminanteDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.unidades = QtGui.QLineEdit(ContaminanteDlgClass)
        self.unidades.setObjectName(_fromUtf8("unidades"))
        self.gridLayout.addWidget(self.unidades, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(ContaminanteDlgClass)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.descripcion = QtGui.QTextEdit(ContaminanteDlgClass)
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.gridLayout.addWidget(self.descripcion, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ContaminanteDlgClass)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_8.setBuddy(self.nombre)
        self.label_9.setBuddy(self.descripcion)

        self.retranslateUi(ContaminanteDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ContaminanteDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ContaminanteDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(ContaminanteDlgClass)
        ContaminanteDlgClass.setTabOrder(self.nombre, self.descripcion)
        ContaminanteDlgClass.setTabOrder(self.descripcion, self.buttonBox)

    def retranslateUi(self, ContaminanteDlgClass):
        ContaminanteDlgClass.setWindowTitle(_translate("ContaminanteDlgClass", "Contaminante", None))
        self.label_8.setText(_translate("ContaminanteDlgClass", "Nombre", None))
        self.label.setText(_translate("ContaminanteDlgClass", "Unidades", None))
        self.label_9.setText(_translate("ContaminanteDlgClass", "Descripción", None))

from ts import DataDialog

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ContaminanteDlgClass = QtGui.DataDialog()
    ui = Ui_ContaminanteDlgClass()
    ui.setupUi(ContaminanteDlgClass)
    ContaminanteDlgClass.show()
    sys.exit(app.exec_())

