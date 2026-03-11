# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contaminantelist.ui'
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

from ts import TSqlTableNavigator
from ...widgets.datalist import DataList

class Ui_ContaminanteListClass(object):
    def setupUi(self, ContaminanteListClass):
        if not ContaminanteListClass.objectName():
            ContaminanteListClass.setObjectName(u"ContaminanteListClass")
        ContaminanteListClass.resize(426, 342)
        self.verticalLayout = QVBoxLayout(ContaminanteListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nav = TSqlTableNavigator(ContaminanteListClass)
        self.nav.setObjectName(u"nav")
        self.nav.setAutoResizeRows(True)
        self.nav.setAutoResizeColumns(True)

        self.verticalLayout.addWidget(self.nav)


        self.retranslateUi(ContaminanteListClass)

        QMetaObject.connectSlotsByName(ContaminanteListClass)
    # setupUi

    def retranslateUi(self, ContaminanteListClass):
        ContaminanteListClass.setWindowTitle(QCoreApplication.translate("ContaminanteListClass", u"Contaminante ...", None))
    # retranslateUi

