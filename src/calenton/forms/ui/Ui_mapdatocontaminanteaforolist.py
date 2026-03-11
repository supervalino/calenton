# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapdatocontaminanteaforolist.ui'
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
from PyQt6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from ts import (TSqlTableNavigator, TTabWidget)
from ...widgets.datalist import DataList

class Ui_MapDatoContaminanteAforoListClass(object):
    def setupUi(self, MapDatoContaminanteAforoListClass):
        if not MapDatoContaminanteAforoListClass.objectName():
            MapDatoContaminanteAforoListClass.setObjectName(u"MapDatoContaminanteAforoListClass")
        MapDatoContaminanteAforoListClass.resize(462, 365)
        self.verticalLayout = QVBoxLayout(MapDatoContaminanteAforoListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_3 = TTabWidget(MapDatoContaminanteAforoListClass)
        self.tab_3.setObjectName(u"tab_3")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nav = TSqlTableNavigator(self.tab)
        self.nav.setObjectName(u"nav")
        self.nav.setShowButtons(False)

        self.verticalLayout_2.addWidget(self.nav)

        self.tab_3.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_3.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tab_3)


        self.retranslateUi(MapDatoContaminanteAforoListClass)

        QMetaObject.connectSlotsByName(MapDatoContaminanteAforoListClass)
    # setupUi

    def retranslateUi(self, MapDatoContaminanteAforoListClass):
        MapDatoContaminanteAforoListClass.setWindowTitle(QCoreApplication.translate("MapDatoContaminanteAforoListClass", u"Datos de conversi\u00f3n de contaminantes por aforo", None))
        self.tab_3.setTabText(self.tab_3.indexOf(self.tab), QCoreApplication.translate("MapDatoContaminanteAforoListClass", u"Tab 1", None))
        self.tab_3.setTabText(self.tab_3.indexOf(self.tab_2), QCoreApplication.translate("MapDatoContaminanteAforoListClass", u"Tab 2", None))
    # retranslateUi

