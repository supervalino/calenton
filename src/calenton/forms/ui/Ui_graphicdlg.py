# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphicdlg.ui'
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

class Ui_GraphicDlgClass(object):
    def setupUi(self, GraphicDlgClass):
        GraphicDlgClass.setObjectName(_fromUtf8("GraphicDlgClass"))
        GraphicDlgClass.resize(492, 570)
        self.verticalLayout_3 = QtGui.QVBoxLayout(GraphicDlgClass)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabs = QtGui.QTabWidget(GraphicDlgClass)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.general = QtGui.QWidget()
        self.general.setObjectName(_fromUtf8("general"))
        self.verticalLayout = QtGui.QVBoxLayout(self.general)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.general)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.nombre = QtGui.QLineEdit(self.general)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.general)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.descripcion = QtGui.QTextEdit(self.general)
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.gridLayout.addWidget(self.descripcion, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.general)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.sql = QtGui.QTextEdit(self.general)
        self.sql.setObjectName(_fromUtf8("sql"))
        self.gridLayout.addWidget(self.sql, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabs.addTab(self.general, _fromUtf8(""))
        self.parametros = QtGui.QWidget()
        self.parametros.setObjectName(_fromUtf8("parametros"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.parametros)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.parametros)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.titulo = QtGui.QLineEdit(self.parametros)
        self.titulo.setObjectName(_fromUtf8("titulo"))
        self.gridLayout_2.addWidget(self.titulo, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.parametros)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.nombreX = QtGui.QLineEdit(self.parametros)
        self.nombreX.setObjectName(_fromUtf8("nombreX"))
        self.gridLayout_2.addWidget(self.nombreX, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.parametros)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.nombreY = QtGui.QLineEdit(self.parametros)
        self.nombreY.setObjectName(_fromUtf8("nombreY"))
        self.gridLayout_2.addWidget(self.nombreY, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.groupBox = QtGui.QGroupBox(self.parametros)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.barras = QtGui.QRadioButton(self.groupBox)
        self.barras.setGeometry(QtCore.QRect(20, 30, 105, 23))
        self.barras.setObjectName(_fromUtf8("barras"))
        self.barrasAc = QtGui.QRadioButton(self.groupBox)
        self.barrasAc.setGeometry(QtCore.QRect(20, 60, 161, 23))
        self.barrasAc.setObjectName(_fromUtf8("barrasAc"))
        self.tarta = QtGui.QRadioButton(self.groupBox)
        self.tarta.setGeometry(QtCore.QRect(20, 90, 105, 23))
        self.tarta.setObjectName(_fromUtf8("tarta"))
        self.lineas = QtGui.QRadioButton(self.groupBox)
        self.lineas.setGeometry(QtCore.QRect(20, 120, 105, 23))
        self.lineas.setObjectName(_fromUtf8("lineas"))
        self.verticalLayout_2.addWidget(self.groupBox)
        self.tabs.addTab(self.parametros, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabs)
        spacerItem = QtGui.QSpacerItem(206, 31, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(GraphicDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.nombre)
        self.label.setBuddy(self.descripcion)
        self.label_2.setBuddy(self.sql)
        self.label_4.setBuddy(self.titulo)
        self.label_5.setBuddy(self.nombreX)
        self.label_6.setBuddy(self.nombreY)

        self.retranslateUi(GraphicDlgClass)
        self.tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GraphicDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GraphicDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(GraphicDlgClass)
        GraphicDlgClass.setTabOrder(self.tabs, self.nombre)
        GraphicDlgClass.setTabOrder(self.nombre, self.descripcion)
        GraphicDlgClass.setTabOrder(self.descripcion, self.sql)
        GraphicDlgClass.setTabOrder(self.sql, self.titulo)
        GraphicDlgClass.setTabOrder(self.titulo, self.nombreX)
        GraphicDlgClass.setTabOrder(self.nombreX, self.nombreY)
        GraphicDlgClass.setTabOrder(self.nombreY, self.barras)
        GraphicDlgClass.setTabOrder(self.barras, self.barrasAc)
        GraphicDlgClass.setTabOrder(self.barrasAc, self.tarta)
        GraphicDlgClass.setTabOrder(self.tarta, self.lineas)
        GraphicDlgClass.setTabOrder(self.lineas, self.buttonBox)

    def retranslateUi(self, GraphicDlgClass):
        GraphicDlgClass.setWindowTitle(_translate("GraphicDlgClass", "Datos del Gráfico", None))
        self.label_3.setText(_translate("GraphicDlgClass", "Nombre", None))
        self.label.setText(_translate("GraphicDlgClass", "Descripción", None))
        self.label_2.setText(_translate("GraphicDlgClass", "SQL", None))
        self.tabs.setTabText(self.tabs.indexOf(self.general), _translate("GraphicDlgClass", "General", None))
        self.label_4.setText(_translate("GraphicDlgClass", "Título", None))
        self.label_5.setText(_translate("GraphicDlgClass", "Nombre eje X", None))
        self.label_6.setText(_translate("GraphicDlgClass", "Nombre eje Y", None))
        self.groupBox.setTitle(_translate("GraphicDlgClass", "Tipo Gráfico", None))
        self.barras.setText(_translate("GraphicDlgClass", "Barras", None))
        self.barrasAc.setText(_translate("GraphicDlgClass", "Barras acumulativo", None))
        self.tarta.setText(_translate("GraphicDlgClass", "Tarta", None))
        self.lineas.setText(_translate("GraphicDlgClass", "Líneas", None))
        self.tabs.setTabText(self.tabs.indexOf(self.parametros), _translate("GraphicDlgClass", "Parámetros", None))

from ts import DataDialog

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    GraphicDlgClass = QtGui.DataDialog()
    ui = Ui_GraphicDlgClass()
    ui.setupUi(GraphicDlgClass)
    GraphicDlgClass.show()
    sys.exit(app.exec_())

