# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapdatocontaminantedlg.ui'
#
# Created: Fri Feb 21 12:06:30 2014
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

class Ui_MapDatoContaminanteDlgClass(object):
    def setupUi(self, MapDatoContaminanteDlgClass):
        MapDatoContaminanteDlgClass.setObjectName(_fromUtf8("MapDatoContaminanteDlgClass"))
        MapDatoContaminanteDlgClass.resize(405, 344)
        self.verticalLayout = QtGui.QVBoxLayout(MapDatoContaminanteDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(MapDatoContaminanteDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.escenario = QtGui.QLineEdit(MapDatoContaminanteDlgClass)
        self.escenario.setEnabled(False)
        self.escenario.setObjectName(_fromUtf8("escenario"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.escenario)
        self.label = QtGui.QLabel(MapDatoContaminanteDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.clasificacion = QtGui.QLineEdit(MapDatoContaminanteDlgClass)
        self.clasificacion.setEnabled(False)
        self.clasificacion.setObjectName(_fromUtf8("clasificacion"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.clasificacion)
        self.label_2 = QtGui.QLabel(MapDatoContaminanteDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.dato = QtGui.QLineEdit(MapDatoContaminanteDlgClass)
        self.dato.setEnabled(False)
        self.dato.setObjectName(_fromUtf8("dato"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dato)
        self.label_5 = QtGui.QLabel(MapDatoContaminanteDlgClass)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboContaminante = TComboBox(MapDatoContaminanteDlgClass)
        self.comboContaminante.setObjectName(_fromUtf8("comboContaminante"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboContaminante)
        self.label_4 = QtGui.QLabel(MapDatoContaminanteDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.editorFormula = QtGui.QPlainTextEdit(MapDatoContaminanteDlgClass)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editorFormula.sizePolicy().hasHeightForWidth())
        self.editorFormula.setSizePolicy(sizePolicy)
        self.editorFormula.setObjectName(_fromUtf8("editorFormula"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.editorFormula)
        self.label_6 = QtGui.QLabel(MapDatoContaminanteDlgClass)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.valor = QtGui.QLineEdit(MapDatoContaminanteDlgClass)
        self.valor.setEnabled(False)
        self.valor.setObjectName(_fromUtf8("valor"))
        self.horizontalLayout.addWidget(self.valor)
        self.indenta = QtGui.QPushButton(MapDatoContaminanteDlgClass)
        self.indenta.setObjectName(_fromUtf8("indenta"))
        self.horizontalLayout.addWidget(self.indenta)
        self.probar = QtGui.QPushButton(MapDatoContaminanteDlgClass)
        self.probar.setObjectName(_fromUtf8("probar"))
        self.horizontalLayout.addWidget(self.probar)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(MapDatoContaminanteDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.escenario)
        self.label.setBuddy(self.clasificacion)
        self.label_2.setBuddy(self.dato)
        self.label_5.setBuddy(self.comboContaminante)
        self.label_4.setBuddy(self.editorFormula)
        self.label_6.setBuddy(self.valor)

        self.retranslateUi(MapDatoContaminanteDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MapDatoContaminanteDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MapDatoContaminanteDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(MapDatoContaminanteDlgClass)
        MapDatoContaminanteDlgClass.setTabOrder(self.comboContaminante, self.editorFormula)
        MapDatoContaminanteDlgClass.setTabOrder(self.editorFormula, self.buttonBox)
        MapDatoContaminanteDlgClass.setTabOrder(self.buttonBox, self.clasificacion)
        MapDatoContaminanteDlgClass.setTabOrder(self.clasificacion, self.dato)
        MapDatoContaminanteDlgClass.setTabOrder(self.dato, self.escenario)
        MapDatoContaminanteDlgClass.setTabOrder(self.escenario, self.valor)

    def retranslateUi(self, MapDatoContaminanteDlgClass):
        MapDatoContaminanteDlgClass.setWindowTitle(_translate("MapDatoContaminanteDlgClass", "Datos de factores de contaminantes", None))
        self.label_3.setText(_translate("MapDatoContaminanteDlgClass", "Escenario", None))
        self.label.setText(_translate("MapDatoContaminanteDlgClass", "Clasificación", None))
        self.label_2.setText(_translate("MapDatoContaminanteDlgClass", "Dato", None))
        self.label_5.setText(_translate("MapDatoContaminanteDlgClass", "Contaminante", None))
        self.label_4.setText(_translate("MapDatoContaminanteDlgClass", "Formula", None))
        self.label_6.setText(_translate("MapDatoContaminanteDlgClass", "Valor Calculado", None))
        self.indenta.setText(_translate("MapDatoContaminanteDlgClass", "Indentar", None))
        self.probar.setText(_translate("MapDatoContaminanteDlgClass", "Probar", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MapDatoContaminanteDlgClass = QtGui.DataDialog()
    ui = Ui_MapDatoContaminanteDlgClass()
    ui.setupUi(MapDatoContaminanteDlgClass)
    MapDatoContaminanteDlgClass.show()
    sys.exit(app.exec_())

