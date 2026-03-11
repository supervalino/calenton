# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapa.ui'
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

from qgis.gui import QgsMapCanvas
from ...widgets.subwindow import SubWindow

class Ui_MapaClass(object):
    def setupUi(self, MapaClass):
        if not MapaClass.objectName():
            MapaClass.setObjectName(u"MapaClass")
        MapaClass.resize(563, 485)
        self.verticalLayout = QVBoxLayout(MapaClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mapa = QgsMapCanvas(MapaClass)
        self.mapa.setObjectName(u"mapa")

        self.verticalLayout.addWidget(self.mapa)


        self.retranslateUi(MapaClass)

        QMetaObject.connectSlotsByName(MapaClass)
    # setupUi

    def retranslateUi(self, MapaClass):
        MapaClass.setWindowTitle(QCoreApplication.translate("MapaClass", u"Mapa", None))
    # retranslateUi

