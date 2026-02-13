# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contaminantelist.ui'
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

class Ui_ContaminanteListClass(object):
    def setupUi(self, ContaminanteListClass):
        ContaminanteListClass.setObjectName(_fromUtf8("ContaminanteListClass"))
        ContaminanteListClass.resize(426, 342)
        self.verticalLayout = QtGui.QVBoxLayout(ContaminanteListClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.nav = TSqlTableNavigator(ContaminanteListClass)
        self.nav.setAutoResizeRows(True)
        self.nav.setAutoResizeColumns(True)
        self.nav.setObjectName(_fromUtf8("nav"))
        self.verticalLayout.addWidget(self.nav)

        self.retranslateUi(ContaminanteListClass)
        QtCore.QMetaObject.connectSlotsByName(ContaminanteListClass)

    def retranslateUi(self, ContaminanteListClass):
        ContaminanteListClass.setWindowTitle(_translate("ContaminanteListClass", "Contaminante ...", None))

from ts import TSqlTableNavigator
from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ContaminanteListClass = QtGui.DataList()
    ui = Ui_ContaminanteListClass()
    ui.setupUi(ContaminanteListClass)
    ContaminanteListClass.show()
    sys.exit(app.exec_())

