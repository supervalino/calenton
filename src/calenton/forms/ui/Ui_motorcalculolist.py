# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'motorcalculolist.ui'
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

class Ui_MotorCalculoListClass(object):
    def setupUi(self, MotorCalculoListClass):
        if not MotorCalculoListClass.objectName():
            MotorCalculoListClass.setObjectName(u"MotorCalculoListClass")
        MotorCalculoListClass.resize(400, 300)
        self.verticalLayout = QVBoxLayout(MotorCalculoListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabla = QTableView(MotorCalculoListClass)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tabla)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.anade = QPushButton(MotorCalculoListClass)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)

        self.edita = QPushButton(MotorCalculoListClass)
        self.edita.setObjectName(u"edita")
        self.edita.setEnabled(False)

        self.horizontalLayout.addWidget(self.edita)

        self.elimina = QPushButton(MotorCalculoListClass)
        self.elimina.setObjectName(u"elimina")
        self.elimina.setEnabled(False)

        self.horizontalLayout.addWidget(self.elimina)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.tabla, self.anade)
        QWidget.setTabOrder(self.anade, self.edita)
        QWidget.setTabOrder(self.edita, self.elimina)

        self.retranslateUi(MotorCalculoListClass)

        QMetaObject.connectSlotsByName(MotorCalculoListClass)
    # setupUi

    def retranslateUi(self, MotorCalculoListClass):
        MotorCalculoListClass.setWindowTitle(QCoreApplication.translate("MotorCalculoListClass", u"Motores de c\u00e1lculo...", None))
        self.anade.setText(QCoreApplication.translate("MotorCalculoListClass", u"A\u00f1adir...", None))
        self.edita.setText(QCoreApplication.translate("MotorCalculoListClass", u"Editar...", None))
        self.elimina.setText(QCoreApplication.translate("MotorCalculoListClass", u"Eliminar", None))
    # retranslateUi

