# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zonadlg.ui'
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

class Ui_ZonaDialogClass(object):
    def setupUi(self, ZonaDialogClass):
        ZonaDialogClass.setObjectName(_fromUtf8("ZonaDialogClass"))
        ZonaDialogClass.resize(539, 333)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ZonaDialogClass)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(ZonaDialogClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.nombre = QtGui.QLineEdit(ZonaDialogClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.gridLayout_2.addWidget(self.nombre, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ZonaDialogClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.nivel = TComboBox(ZonaDialogClass)
        self.nivel.setEditable(False)
        self.nivel.setObjectName(_fromUtf8("nivel"))
        self.gridLayout_2.addWidget(self.nivel, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.groupBox = QtGui.QGroupBox(ZonaDialogClass)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.borrapadre = QtGui.QPushButton(self.groupBox)
        self.borrapadre.setObjectName(_fromUtf8("borrapadre"))
        self.gridLayout.addWidget(self.borrapadre, 2, 1, 1, 1)
        self.listapadres = QtGui.QListView(self.groupBox)
        self.listapadres.setObjectName(_fromUtf8("listapadres"))
        self.gridLayout.addWidget(self.listapadres, 2, 0, 1, 1)
        self.zonapadre = TComboBox(self.groupBox)
        self.zonapadre.setObjectName(_fromUtf8("zonapadre"))
        self.gridLayout.addWidget(self.zonapadre, 3, 0, 1, 1)
        self.asignapadre = QtGui.QPushButton(self.groupBox)
        self.asignapadre.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asignapadre.sizePolicy().hasHeightForWidth())
        self.asignapadre.setSizePolicy(sizePolicy)
        self.asignapadre.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.asignapadre.setObjectName(_fromUtf8("asignapadre"))
        self.gridLayout.addWidget(self.asignapadre, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 125, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(ZonaDialogClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label.setBuddy(self.nombre)
        self.label_2.setBuddy(self.nivel)

        self.retranslateUi(ZonaDialogClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ZonaDialogClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ZonaDialogClass.reject)
        QtCore.QMetaObject.connectSlotsByName(ZonaDialogClass)
        ZonaDialogClass.setTabOrder(self.nombre, self.nivel)
        ZonaDialogClass.setTabOrder(self.nivel, self.asignapadre)
        ZonaDialogClass.setTabOrder(self.asignapadre, self.listapadres)
        ZonaDialogClass.setTabOrder(self.listapadres, self.buttonBox)

    def retranslateUi(self, ZonaDialogClass):
        ZonaDialogClass.setWindowTitle(_translate("ZonaDialogClass", "Datos de zonas", None))
        self.label.setText(_translate("ZonaDialogClass", "Nombre", None))
        self.label_2.setText(_translate("ZonaDialogClass", "Nivel", None))
        self.groupBox.setTitle(_translate("ZonaDialogClass", "Pertenece a", None))
        self.borrapadre.setText(_translate("ZonaDialogClass", "Eliminar", None))
        self.asignapadre.setText(_translate("ZonaDialogClass", "Añadir", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ZonaDialogClass = QtGui.DataDialog()
    ui = Ui_ZonaDialogClass()
    ui.setupUi(ZonaDialogClass)
    ZonaDialogClass.show()
    sys.exit(app.exec_())

