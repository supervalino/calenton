# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plantillalist.ui'
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

class Ui_PlantillaListClass(object):
    def setupUi(self, PlantillaListClass):
        PlantillaListClass.setObjectName(_fromUtf8("PlantillaListClass"))
        PlantillaListClass.resize(482, 458)
        self.verticalLayout = QtGui.QVBoxLayout(PlantillaListClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.plantilla = QtGui.QLineEdit(PlantillaListClass)
        self.plantilla.setEnabled(False)
        self.plantilla.setObjectName(_fromUtf8("plantilla"))
        self.gridLayout.addWidget(self.plantilla, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(PlantillaListClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.descripcion = QtGui.QTextEdit(PlantillaListClass)
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.gridLayout.addWidget(self.descripcion, 1, 2, 1, 1)
        self.label = QtGui.QLabel(PlantillaListClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 160, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(228, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.nueva = QtGui.QPushButton(PlantillaListClass)
        self.nueva.setObjectName(_fromUtf8("nueva"))
        self.horizontalLayout.addWidget(self.nueva)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(PlantillaListClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.descripcion)
        self.label.setBuddy(self.plantilla)

        self.retranslateUi(PlantillaListClass)
        QtCore.QMetaObject.connectSlotsByName(PlantillaListClass)
        PlantillaListClass.setTabOrder(self.plantilla, self.descripcion)
        PlantillaListClass.setTabOrder(self.descripcion, self.nueva)

    def retranslateUi(self, PlantillaListClass):
        PlantillaListClass.setWindowTitle(_translate("PlantillaListClass", "Plantillas de informes", None))
        self.label_2.setText(_translate("PlantillaListClass", "Descripción:", None))
        self.label.setText(_translate("PlantillaListClass", "Plantilla Actual:", None))
        self.nueva.setText(_translate("PlantillaListClass", "Cargar Nueva", None))

from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PlantillaListClass = QtGui.DataList()
    ui = Ui_PlantillaListClass()
    ui.setupUi(PlantillaListClass)
    PlantillaListClass.show()
    sys.exit(app.exec_())

