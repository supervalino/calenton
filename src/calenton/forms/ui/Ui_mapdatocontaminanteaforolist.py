# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapdatocontaminanteaforolist.ui'
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

class Ui_MapDatoContaminanteAforoListClass(object):
    def setupUi(self, MapDatoContaminanteAforoListClass):
        MapDatoContaminanteAforoListClass.setObjectName(_fromUtf8("MapDatoContaminanteAforoListClass"))
        MapDatoContaminanteAforoListClass.resize(462, 365)
        self.verticalLayout = QtGui.QVBoxLayout(MapDatoContaminanteAforoListClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tab_3 = TTabWidget(MapDatoContaminanteAforoListClass)
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.nav = TSqlTableNavigator(self.tab)
        self.nav.setShowButtons(False)
        self.nav.setObjectName(_fromUtf8("nav"))
        self.verticalLayout_2.addWidget(self.nav)
        self.tab_3.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tab_3.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tab_3)

        self.retranslateUi(MapDatoContaminanteAforoListClass)
        QtCore.QMetaObject.connectSlotsByName(MapDatoContaminanteAforoListClass)

    def retranslateUi(self, MapDatoContaminanteAforoListClass):
        MapDatoContaminanteAforoListClass.setWindowTitle(_translate("MapDatoContaminanteAforoListClass", "Datos de conversión de contaminantes por aforo", None))
        self.tab_3.setTabText(self.tab_3.indexOf(self.tab), _translate("MapDatoContaminanteAforoListClass", "Tab 1", None))
        self.tab_3.setTabText(self.tab_3.indexOf(self.tab_2), _translate("MapDatoContaminanteAforoListClass", "Tab 2", None))

from ts import TTabWidget, TSqlTableNavigator
from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MapDatoContaminanteAforoListClass = QtGui.DataList()
    ui = Ui_MapDatoContaminanteAforoListClass()
    ui.setupUi(MapDatoContaminanteAforoListClass)
    MapDatoContaminanteAforoListClass.show()
    sys.exit(app.exec_())

