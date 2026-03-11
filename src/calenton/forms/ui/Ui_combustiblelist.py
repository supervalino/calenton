# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'combustiblelist.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

from ts import (TComboBox, TSqlTableNavigator)
from ...widgets.datalist import DataList

class Ui_CombustibleListClass(object):
    def setupUi(self, CombustibleListClass):
        if not CombustibleListClass.objectName():
            CombustibleListClass.setObjectName(u"CombustibleListClass")
        CombustibleListClass.resize(529, 459)
        self.verticalLayout = QVBoxLayout(CombustibleListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(CombustibleListClass)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.navCombustible = TSqlTableNavigator(self.tab)
        self.navCombustible.setObjectName(u"navCombustible")
        self.navCombustible.setAutoResizeRows(True)
        self.navCombustible.setAutoResizeColumns(True)
        self.navCombustible.setAlternatingRowColors(True)

        self.verticalLayout_2.addWidget(self.navCombustible)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.escenario = TComboBox(self.tab_2)
        self.escenario.setObjectName(u"escenario")

        self.horizontalLayout.addWidget(self.escenario)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.navClasCombustible = TSqlTableNavigator(self.tab_2)
        self.navClasCombustible.setObjectName(u"navClasCombustible")
        self.navClasCombustible.setAutoResizeRows(True)
        self.navClasCombustible.setAutoResizeColumns(True)
        self.navClasCombustible.setAlternatingRowColors(True)

        self.verticalLayout_3.addWidget(self.navClasCombustible)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(CombustibleListClass)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CombustibleListClass)
    # setupUi

    def retranslateUi(self, CombustibleListClass):
        CombustibleListClass.setWindowTitle(QCoreApplication.translate("CombustibleListClass", u"Combustibles...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("CombustibleListClass", u"Combustibles", None))
        self.label.setText(QCoreApplication.translate("CombustibleListClass", u"Escenario", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("CombustibleListClass", u"Relaci\u00f3n clasificaci\u00f3n", None))
    # retranslateUi

