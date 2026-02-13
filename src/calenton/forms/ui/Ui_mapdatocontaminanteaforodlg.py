# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapdatocontaminanteaforodlg.ui'
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

class Ui_MapDatoContaminanteAforoDlgClass(object):
    def setupUi(self, MapDatoContaminanteAforoDlgClass):
        MapDatoContaminanteAforoDlgClass.setObjectName(_fromUtf8("MapDatoContaminanteAforoDlgClass"))
        MapDatoContaminanteAforoDlgClass.resize(458, 392)
        self.verticalLayout = QtGui.QVBoxLayout(MapDatoContaminanteAforoDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(MapDatoContaminanteAforoDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dato = TComboBox(MapDatoContaminanteAforoDlgClass)
        self.dato.setObjectName(_fromUtf8("dato"))
        self.gridLayout.addWidget(self.dato, 1, 1, 1, 1)
        self.label = QtGui.QLabel(MapDatoContaminanteAforoDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.clasificacion = TComboBox(MapDatoContaminanteAforoDlgClass)
        self.clasificacion.setObjectName(_fromUtf8("clasificacion"))
        self.gridLayout.addWidget(self.clasificacion, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(MapDatoContaminanteAforoDlgClass)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.contaminante = TComboBox(MapDatoContaminanteAforoDlgClass)
        self.contaminante.setObjectName(_fromUtf8("contaminante"))
        self.gridLayout.addWidget(self.contaminante, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(MapDatoContaminanteAforoDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.p = QtGui.QLineEdit(MapDatoContaminanteAforoDlgClass)
        self.p.setObjectName(_fromUtf8("p"))
        self.gridLayout.addWidget(self.p, 4, 1, 1, 1)
        self.aforo = TComboBox(MapDatoContaminanteAforoDlgClass)
        self.aforo.setObjectName(_fromUtf8("aforo"))
        self.gridLayout.addWidget(self.aforo, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(MapDatoContaminanteAforoDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(MapDatoContaminanteAforoDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.dato)
        self.label_4.setBuddy(self.p)

        self.retranslateUi(MapDatoContaminanteAforoDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MapDatoContaminanteAforoDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MapDatoContaminanteAforoDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(MapDatoContaminanteAforoDlgClass)
        MapDatoContaminanteAforoDlgClass.setTabOrder(self.dato, self.p)
        MapDatoContaminanteAforoDlgClass.setTabOrder(self.p, self.buttonBox)

    def retranslateUi(self, MapDatoContaminanteAforoDlgClass):
        MapDatoContaminanteAforoDlgClass.setWindowTitle(_translate("MapDatoContaminanteAforoDlgClass", "Datos de factores de contaminantes por aforo", None))
        self.label_2.setText(_translate("MapDatoContaminanteAforoDlgClass", "Dato", None))
        self.label.setText(_translate("MapDatoContaminanteAforoDlgClass", "Clasificación", None))
        self.label_5.setText(_translate("MapDatoContaminanteAforoDlgClass", "Contaminante", None))
        self.label_4.setText(_translate("MapDatoContaminanteAforoDlgClass", "Factor", None))
        self.label_3.setText(_translate("MapDatoContaminanteAforoDlgClass", "Aforo", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MapDatoContaminanteAforoDlgClass = QtGui.DataDialog()
    ui = Ui_MapDatoContaminanteAforoDlgClass()
    ui.setupUi(MapDatoContaminanteAforoDlgClass)
    MapDatoContaminanteAforoDlgClass.show()
    sys.exit(app.exec_())

