# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapaforozonadlg.ui'
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

class Ui_MapAforoZonaDlgClass(object):
    def setupUi(self, MapAforoZonaDlgClass):
        MapAforoZonaDlgClass.setObjectName(_fromUtf8("MapAforoZonaDlgClass"))
        MapAforoZonaDlgClass.resize(458, 392)
        self.verticalLayout = QtGui.QVBoxLayout(MapAforoZonaDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(MapAforoZonaDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.aforo = TComboBox(MapAforoZonaDlgClass)
        self.aforo.setObjectName(_fromUtf8("aforo"))
        self.gridLayout.addWidget(self.aforo, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(MapAforoZonaDlgClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.zona = TComboBox(MapAforoZonaDlgClass)
        self.zona.setObjectName(_fromUtf8("zona"))
        self.gridLayout.addWidget(self.zona, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(MapAforoZonaDlgClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.p = QtGui.QLineEdit(MapAforoZonaDlgClass)
        self.p.setObjectName(_fromUtf8("p"))
        self.gridLayout.addWidget(self.p, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(MapAforoZonaDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.aforo)
        self.label_2.setBuddy(self.zona)
        self.label_4.setBuddy(self.p)

        self.retranslateUi(MapAforoZonaDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MapAforoZonaDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MapAforoZonaDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(MapAforoZonaDlgClass)
        MapAforoZonaDlgClass.setTabOrder(self.aforo, self.zona)
        MapAforoZonaDlgClass.setTabOrder(self.zona, self.p)
        MapAforoZonaDlgClass.setTabOrder(self.p, self.buttonBox)

    def retranslateUi(self, MapAforoZonaDlgClass):
        MapAforoZonaDlgClass.setWindowTitle(_translate("MapAforoZonaDlgClass", "Contribución de contaminantes en un aforo", None))
        self.label_3.setText(_translate("MapAforoZonaDlgClass", "Aforo", None))
        self.label_2.setText(_translate("MapAforoZonaDlgClass", "Zona", None))
        self.label_4.setText(_translate("MapAforoZonaDlgClass", "Valor", None))

from ts import DataDialog, TComboBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MapAforoZonaDlgClass = QtGui.DataDialog()
    ui = Ui_MapAforoZonaDlgClass()
    ui.setupUi(MapAforoZonaDlgClass)
    MapAforoZonaDlgClass.show()
    sys.exit(app.exec_())

