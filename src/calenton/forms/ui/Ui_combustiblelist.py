# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combustiblelist.ui'
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

class Ui_CombustibleListClass(object):
    def setupUi(self, CombustibleListClass):
        CombustibleListClass.setObjectName(_fromUtf8("CombustibleListClass"))
        CombustibleListClass.resize(529, 459)
        self.verticalLayout = QtGui.QVBoxLayout(CombustibleListClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(CombustibleListClass)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.navCombustible = TSqlTableNavigator(self.tab)
        self.navCombustible.setAutoResizeRows(True)
        self.navCombustible.setAutoResizeColumns(True)
        self.navCombustible.setAlternatingRowColors(True)
        self.navCombustible.setObjectName(_fromUtf8("navCombustible"))
        self.verticalLayout_2.addWidget(self.navCombustible)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.escenario = TComboBox(self.tab_2)
        self.escenario.setObjectName(_fromUtf8("escenario"))
        self.horizontalLayout.addWidget(self.escenario)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.navClasCombustible = TSqlTableNavigator(self.tab_2)
        self.navClasCombustible.setAutoResizeRows(True)
        self.navClasCombustible.setAutoResizeColumns(True)
        self.navClasCombustible.setAlternatingRowColors(True)
        self.navClasCombustible.setObjectName(_fromUtf8("navClasCombustible"))
        self.verticalLayout_3.addWidget(self.navClasCombustible)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(CombustibleListClass)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CombustibleListClass)

    def retranslateUi(self, CombustibleListClass):
        CombustibleListClass.setWindowTitle(_translate("CombustibleListClass", "Combustibles...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("CombustibleListClass", "Combustibles", None))
        self.label.setText(_translate("CombustibleListClass", "Escenario", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("CombustibleListClass", "Relación clasificación", None))

from ts import TComboBox, TSqlTableNavigator
from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CombustibleListClass = QtGui.DataList()
    ui = Ui_CombustibleListClass()
    ui.setupUi(CombustibleListClass)
    CombustibleListClass.show()
    sys.exit(app.exec_())

