# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tipoclaslist.ui'
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

class Ui_TipoclasListClass(object):
    def setupUi(self, TipoclasListClass):
        if not TipoclasListClass.objectName():
            TipoclasListClass.setObjectName(u"TipoclasListClass")
        TipoclasListClass.resize(400, 300)
        self.verticalLayout = QVBoxLayout(TipoclasListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabla = QTableView(TipoclasListClass)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tabla)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.anade = QPushButton(TipoclasListClass)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)

        self.edita = QPushButton(TipoclasListClass)
        self.edita.setObjectName(u"edita")
        self.edita.setEnabled(False)

        self.horizontalLayout.addWidget(self.edita)

        self.elimina = QPushButton(TipoclasListClass)
        self.elimina.setObjectName(u"elimina")
        self.elimina.setEnabled(False)

        self.horizontalLayout.addWidget(self.elimina)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.tabla, self.anade)
        QWidget.setTabOrder(self.anade, self.edita)
        QWidget.setTabOrder(self.edita, self.elimina)

        self.retranslateUi(TipoclasListClass)

        QMetaObject.connectSlotsByName(TipoclasListClass)
    # setupUi

    def retranslateUi(self, TipoclasListClass):
        TipoclasListClass.setWindowTitle(QCoreApplication.translate("TipoclasListClass", u"Tipo de clasificaci\u00f3n ...", None))
        self.anade.setText(QCoreApplication.translate("TipoclasListClass", u"A\u00f1adir...", None))
        self.edita.setText(QCoreApplication.translate("TipoclasListClass", u"Editar...", None))
        self.elimina.setText(QCoreApplication.translate("TipoclasListClass", u"Eliminar", None))
    # retranslateUi

