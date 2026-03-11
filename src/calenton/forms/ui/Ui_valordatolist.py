# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'valordatolist.ui'
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
from PyQt6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QWidget)

from ...widgets.datalist import DataList

class Ui_ValorDatoListClass(object):
    def setupUi(self, ValorDatoListClass):
        if not ValorDatoListClass.objectName():
            ValorDatoListClass.setObjectName(u"ValorDatoListClass")
        ValorDatoListClass.resize(614, 549)
        self.gridLayout = QGridLayout(ValorDatoListClass)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabla = QTableView(ValorDatoListClass)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setEditTriggers(QAbstractItemView.EditTrigger.SelectedClicked)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.gridLayout.addWidget(self.tabla, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.guardar = QPushButton(ValorDatoListClass)
        self.guardar.setObjectName(u"guardar")

        self.horizontalLayout.addWidget(self.guardar)

        self.descartar = QPushButton(ValorDatoListClass)
        self.descartar.setObjectName(u"descartar")

        self.horizontalLayout.addWidget(self.descartar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.elimina = QPushButton(ValorDatoListClass)
        self.elimina.setObjectName(u"elimina")

        self.horizontalLayout.addWidget(self.elimina)

        self.edita = QPushButton(ValorDatoListClass)
        self.edita.setObjectName(u"edita")

        self.horizontalLayout.addWidget(self.edita)

        self.anade = QPushButton(ValorDatoListClass)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        QWidget.setTabOrder(self.tabla, self.elimina)
        QWidget.setTabOrder(self.elimina, self.edita)
        QWidget.setTabOrder(self.edita, self.anade)

        self.retranslateUi(ValorDatoListClass)

        QMetaObject.connectSlotsByName(ValorDatoListClass)
    # setupUi

    def retranslateUi(self, ValorDatoListClass):
        ValorDatoListClass.setWindowTitle(QCoreApplication.translate("ValorDatoListClass", u"Valores tomados  en cada aforo", None))
        self.guardar.setText(QCoreApplication.translate("ValorDatoListClass", u"Guardar", None))
        self.descartar.setText(QCoreApplication.translate("ValorDatoListClass", u"Descartar", None))
        self.elimina.setText(QCoreApplication.translate("ValorDatoListClass", u"Eliminar", None))
        self.edita.setText(QCoreApplication.translate("ValorDatoListClass", u"Editar", None))
        self.anade.setText(QCoreApplication.translate("ValorDatoListClass", u"A\u00f1adir", None))
    # retranslateUi

