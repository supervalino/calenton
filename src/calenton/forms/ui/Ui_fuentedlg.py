# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuentedlg.ui'
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

class Ui_FuenteDlgClass(object):
    def setupUi(self, FuenteDlgClass):
        FuenteDlgClass.setObjectName(_fromUtf8("FuenteDlgClass"))
        FuenteDlgClass.resize(528, 399)
        self.verticalLayout_2 = QtGui.QVBoxLayout(FuenteDlgClass)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(FuenteDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.nombre = QtGui.QLineEdit(FuenteDlgClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(FuenteDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.escenario = TComboBox(FuenteDlgClass)
        self.escenario.setObjectName(_fromUtf8("escenario"))
        self.gridLayout.addWidget(self.escenario, 1, 1, 1, 1)
        self.label = QtGui.QLabel(FuenteDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.origen = TComboBox(FuenteDlgClass)
        self.origen.setObjectName(_fromUtf8("origen"))
        self.gridLayout.addWidget(self.origen, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(FuenteDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.motorcalculo = TComboBox(FuenteDlgClass)
        self.motorcalculo.setObjectName(_fromUtf8("motorcalculo"))
        self.gridLayout.addWidget(self.motorcalculo, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(FuenteDlgClass)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.nivelZona = TComboBox(FuenteDlgClass)
        self.nivelZona.setObjectName(_fromUtf8("nivelZona"))
        self.gridLayout.addWidget(self.nivelZona, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(FuenteDlgClass)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.tipoDatoZona = TComboBox(FuenteDlgClass)
        self.tipoDatoZona.setObjectName(_fromUtf8("tipoDatoZona"))
        self.gridLayout.addWidget(self.tipoDatoZona, 5, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(FuenteDlgClass)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.borraclasificacion = QtGui.QPushButton(self.groupBox)
        self.borraclasificacion.setObjectName(_fromUtf8("borraclasificacion"))
        self.gridLayout_2.addWidget(self.borraclasificacion, 2, 1, 1, 1)
        self.clasificacion = TComboBox(self.groupBox)
        self.clasificacion.setObjectName(_fromUtf8("clasificacion"))
        self.gridLayout_2.addWidget(self.clasificacion, 3, 0, 1, 1)
        self.asignaclasificacion = QtGui.QPushButton(self.groupBox)
        self.asignaclasificacion.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asignaclasificacion.sizePolicy().hasHeightForWidth())
        self.asignaclasificacion.setSizePolicy(sizePolicy)
        self.asignaclasificacion.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.asignaclasificacion.setObjectName(_fromUtf8("asignaclasificacion"))
        self.gridLayout_2.addWidget(self.asignaclasificacion, 3, 1, 1, 1)
        self.listaclasificacion = QtGui.QTableView(self.groupBox)
        self.listaclasificacion.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listaclasificacion.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.listaclasificacion.setObjectName(_fromUtf8("listaclasificacion"))
        self.gridLayout_2.addWidget(self.listaclasificacion, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(FuenteDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.escenario)
        self.label.setBuddy(self.origen)
        self.label_4.setBuddy(self.motorcalculo)
        self.label_5.setBuddy(self.nivelZona)
        self.label_6.setBuddy(self.tipoDatoZona)

        self.retranslateUi(FuenteDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FuenteDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FuenteDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(FuenteDlgClass)
        FuenteDlgClass.setTabOrder(self.nombre, self.escenario)
        FuenteDlgClass.setTabOrder(self.escenario, self.origen)
        FuenteDlgClass.setTabOrder(self.origen, self.motorcalculo)
        FuenteDlgClass.setTabOrder(self.motorcalculo, self.nivelZona)
        FuenteDlgClass.setTabOrder(self.nivelZona, self.tipoDatoZona)
        FuenteDlgClass.setTabOrder(self.tipoDatoZona, self.listaclasificacion)
        FuenteDlgClass.setTabOrder(self.listaclasificacion, self.borraclasificacion)
        FuenteDlgClass.setTabOrder(self.borraclasificacion, self.clasificacion)
        FuenteDlgClass.setTabOrder(self.clasificacion, self.asignaclasificacion)
        FuenteDlgClass.setTabOrder(self.asignaclasificacion, self.buttonBox)

    def retranslateUi(self, FuenteDlgClass):
        FuenteDlgClass.setWindowTitle(_translate("FuenteDlgClass", "Datos de fuente", None))
        self.label_3.setText(_translate("FuenteDlgClass", "Nombre", None))
        self.label_2.setText(_translate("FuenteDlgClass", "Escenario", None))
        self.label.setText(_translate("FuenteDlgClass", "Origen", None))
        self.label_4.setText(_translate("FuenteDlgClass", "Motor de Cálculo", None))
        self.label_5.setText(_translate("FuenteDlgClass", "Nivel de zona", None))
        self.label_6.setText(_translate("FuenteDlgClass", "Dato Distribución", None))
        self.groupBox.setTitle(_translate("FuenteDlgClass", "Se clasifica por:", None))
        self.borraclasificacion.setText(_translate("FuenteDlgClass", "Eliminar", None))
        self.asignaclasificacion.setText(_translate("FuenteDlgClass", "Añadir", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FuenteDlgClass = QtGui.DataDialog()
    ui = Ui_FuenteDlgClass()
    ui.setupUi(FuenteDlgClass)
    FuenteDlgClass.show()
    sys.exit(app.exec_())

