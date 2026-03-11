# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'relzonalist.ui'
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
from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

from ...widgets.datalist import DataList

class Ui_ZonaListClass(object):
    def setupUi(self, ZonaListClass):
        if not ZonaListClass.objectName():
            ZonaListClass.setObjectName(u"ZonaListClass")
        ZonaListClass.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ZonaListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabla = QTableView(ZonaListClass)
        self.tabla.setObjectName(u"tabla")

        self.verticalLayout.addWidget(self.tabla)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.anade = QPushButton(ZonaListClass)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)

        self.edita = QPushButton(ZonaListClass)
        self.edita.setObjectName(u"edita")
        self.edita.setEnabled(False)

        self.horizontalLayout.addWidget(self.edita)

        self.elimina = QPushButton(ZonaListClass)
        self.elimina.setObjectName(u"elimina")
        self.elimina.setEnabled(False)

        self.horizontalLayout.addWidget(self.elimina)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ZonaListClass)

        QMetaObject.connectSlotsByName(ZonaListClass)
    # setupUi

    def retranslateUi(self, ZonaListClass):
        ZonaListClass.setWindowTitle(QCoreApplication.translate("ZonaListClass", u"Form", None))
        self.anade.setText(QCoreApplication.translate("ZonaListClass", u"A\u00f1adir...", None))
        self.edita.setText(QCoreApplication.translate("ZonaListClass", u"Editar...", None))
        self.elimina.setText(QCoreApplication.translate("ZonaListClass", u"Eliminar", None))
    # retranslateUi

