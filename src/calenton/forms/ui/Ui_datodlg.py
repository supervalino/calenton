# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datodlg.ui'
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

class Ui_DatoDlgClass(object):
    def setupUi(self, DatoDlgClass):
        DatoDlgClass.setObjectName(_fromUtf8("DatoDlgClass"))
        DatoDlgClass.resize(713, 483)
        self.verticalLayout = QtGui.QVBoxLayout(DatoDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(DatoDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.nombre = QtGui.QLineEdit(DatoDlgClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nombre)
        self.label_2 = QtGui.QLabel(DatoDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.clasificacion = TComboBox(DatoDlgClass)
        self.clasificacion.setObjectName(_fromUtf8("clasificacion"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.clasificacion)
        self.label = QtGui.QLabel(DatoDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.unidades = QtGui.QLineEdit(DatoDlgClass)
        self.unidades.setObjectName(_fromUtf8("unidades"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.unidades)
        self.label_4 = QtGui.QLabel(DatoDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.descripcion = QtGui.QTextEdit(DatoDlgClass)
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.descripcion)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(DatoDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.clasificacion)
        self.label.setBuddy(self.unidades)
        self.label_4.setBuddy(self.descripcion)

        self.retranslateUi(DatoDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DatoDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DatoDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(DatoDlgClass)
        DatoDlgClass.setTabOrder(self.nombre, self.clasificacion)
        DatoDlgClass.setTabOrder(self.clasificacion, self.unidades)
        DatoDlgClass.setTabOrder(self.unidades, self.descripcion)
        DatoDlgClass.setTabOrder(self.descripcion, self.buttonBox)

    def retranslateUi(self, DatoDlgClass):
        DatoDlgClass.setWindowTitle(_translate("DatoDlgClass", "Características del punto de toma", None))
        self.label_3.setText(_translate("DatoDlgClass", "Nombre", None))
        self.label_2.setText(_translate("DatoDlgClass", "Clasificación", None))
        self.label.setText(_translate("DatoDlgClass", "Unidades", None))
        self.label_4.setText(_translate("DatoDlgClass", "Descripción", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DatoDlgClass = QtGui.DataDialog()
    ui = Ui_DatoDlgClass()
    ui.setupUi(DatoDlgClass)
    DatoDlgClass.show()
    sys.exit(app.exec_())

