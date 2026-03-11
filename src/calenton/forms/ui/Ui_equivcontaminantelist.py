# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equivcontaminantelist.ui'
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
from PyQt6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

from ...widgets.datalist import DataList

class Ui_EquivContaminanteListClass(object):
    def setupUi(self, EquivContaminanteListClass):
        if not EquivContaminanteListClass.objectName():
            EquivContaminanteListClass.setObjectName(u"EquivContaminanteListClass")
        EquivContaminanteListClass.resize(412, 308)
        self.verticalLayout = QVBoxLayout(EquivContaminanteListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabla = QTableView(EquivContaminanteListClass)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tabla)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.elimina = QPushButton(EquivContaminanteListClass)
        self.elimina.setObjectName(u"elimina")

        self.horizontalLayout.addWidget(self.elimina)

        self.edita = QPushButton(EquivContaminanteListClass)
        self.edita.setObjectName(u"edita")

        self.horizontalLayout.addWidget(self.edita)

        self.anade = QPushButton(EquivContaminanteListClass)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(EquivContaminanteListClass)

        QMetaObject.connectSlotsByName(EquivContaminanteListClass)
    # setupUi

    def retranslateUi(self, EquivContaminanteListClass):
        EquivContaminanteListClass.setWindowTitle(QCoreApplication.translate("EquivContaminanteListClass", u"Lista de equivalentes de CO2", None))
        self.elimina.setText(QCoreApplication.translate("EquivContaminanteListClass", u"Eliminar", None))
        self.edita.setText(QCoreApplication.translate("EquivContaminanteListClass", u"Editar", None))
        self.anade.setText(QCoreApplication.translate("EquivContaminanteListClass", u"A\u00f1adir", None))
    # retranslateUi

