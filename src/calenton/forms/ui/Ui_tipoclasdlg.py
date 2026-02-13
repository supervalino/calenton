# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tipoclasdlg.ui'
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

class Ui_TipoclasDlgClass(object):
    def setupUi(self, TipoclasDlgClass):
        TipoclasDlgClass.setObjectName(_fromUtf8("TipoclasDlgClass"))
        TipoclasDlgClass.resize(475, 355)
        self.verticalLayout = QtGui.QVBoxLayout(TipoclasDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_8 = QtGui.QLabel(TipoclasDlgClass)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.nombre = QtGui.QLineEdit(TipoclasDlgClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nombre)
        self.label_9 = QtGui.QLabel(TipoclasDlgClass)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.descripcion = QtGui.QTextEdit(TipoclasDlgClass)
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.descripcion)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(TipoclasDlgClass)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_8.setBuddy(self.nombre)
        self.label_9.setBuddy(self.descripcion)

        self.retranslateUi(TipoclasDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TipoclasDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TipoclasDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(TipoclasDlgClass)
        TipoclasDlgClass.setTabOrder(self.nombre, self.descripcion)
        TipoclasDlgClass.setTabOrder(self.descripcion, self.buttonBox)

    def retranslateUi(self, TipoclasDlgClass):
        TipoclasDlgClass.setWindowTitle(_translate("TipoclasDlgClass", "Tipo de clasificación", None))
        self.label_8.setText(_translate("TipoclasDlgClass", "Nombre", None))
        self.label_9.setText(_translate("TipoclasDlgClass", "Descripción", None))

from ts import DataDialog

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TipoclasDlgClass = QtGui.DataDialog()
    ui = Ui_TipoclasDlgClass()
    ui.setupUi(TipoclasDlgClass)
    TipoclasDlgClass.show()
    sys.exit(app.exec_())

