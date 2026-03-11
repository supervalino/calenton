# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nivelzonalist.ui'
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

class Ui_NivelZonaListClass(object):
    def setupUi(self, NivelZonaListClass):
        if not NivelZonaListClass.objectName():
            NivelZonaListClass.setObjectName(u"NivelZonaListClass")
        NivelZonaListClass.resize(400, 300)
        self.verticalLayout = QVBoxLayout(NivelZonaListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabla = QTableView(NivelZonaListClass)
        self.tabla.setObjectName(u"tabla")

        self.verticalLayout.addWidget(self.tabla)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.anade = QPushButton(NivelZonaListClass)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)

        self.edita = QPushButton(NivelZonaListClass)
        self.edita.setObjectName(u"edita")
        self.edita.setEnabled(False)

        self.horizontalLayout.addWidget(self.edita)

        self.elimina = QPushButton(NivelZonaListClass)
        self.elimina.setObjectName(u"elimina")
        self.elimina.setEnabled(False)

        self.horizontalLayout.addWidget(self.elimina)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(NivelZonaListClass)

        QMetaObject.connectSlotsByName(NivelZonaListClass)
    # setupUi

    def retranslateUi(self, NivelZonaListClass):
        NivelZonaListClass.setWindowTitle(QCoreApplication.translate("NivelZonaListClass", u"Form", None))
        self.anade.setText(QCoreApplication.translate("NivelZonaListClass", u"A\u00f1adir...", None))
        self.edita.setText(QCoreApplication.translate("NivelZonaListClass", u"Editar...", None))
        self.elimina.setText(QCoreApplication.translate("NivelZonaListClass", u"Eliminar", None))
    # retranslateUi

