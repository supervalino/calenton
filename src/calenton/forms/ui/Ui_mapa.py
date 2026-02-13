# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapa.ui'
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

class Ui_MapaClass(object):
    def setupUi(self, MapaClass):
        MapaClass.setObjectName(_fromUtf8("MapaClass"))
        MapaClass.resize(563, 485)
        self.verticalLayout = QtGui.QVBoxLayout(MapaClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mapa = QgsMapCanvas(MapaClass)
        self.mapa.setObjectName(_fromUtf8("mapa"))
        self.verticalLayout.addWidget(self.mapa)

        self.retranslateUi(MapaClass)
        QtCore.QMetaObject.connectSlotsByName(MapaClass)

    def retranslateUi(self, MapaClass):
        MapaClass.setWindowTitle(_translate("MapaClass", "Mapa", None))

from widgets.subwindow import SubWindow
from qgis.gui import QgsMapCanvas

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MapaClass = QtGui.SubWindow()
    ui = Ui_MapaClass()
    ui.setupUi(MapaClass)
    MapaClass.show()
    sys.exit(app.exec_())

