# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fuenteclasificacionlist.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PyQt6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

from ...widgets.datalist import DataList

class Ui_FuenteClasificacionListClass(object):
    def setupUi(self, FuenteClasificacionListClass):
        if not FuenteClasificacionListClass.objectName():
            FuenteClasificacionListClass.setObjectName(u"FuenteClasificacionListClass")
        FuenteClasificacionListClass.resize(599, 308)
        self.clipboardFuenteClasificacion = QAction(FuenteClasificacionListClass)
        self.clipboardFuenteClasificacion.setObjectName(u"clipboardFuenteClasificacion")
        self.verticalLayout = QVBoxLayout(FuenteClasificacionListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabla = QTableView(FuenteClasificacionListClass)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tabla)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.guarda = QPushButton(FuenteClasificacionListClass)
        self.guarda.setObjectName(u"guarda")

        self.horizontalLayout.addWidget(self.guarda)

        self.descarta = QPushButton(FuenteClasificacionListClass)
        self.descarta.setObjectName(u"descarta")

        self.horizontalLayout.addWidget(self.descarta)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.elimina = QPushButton(FuenteClasificacionListClass)
        self.elimina.setObjectName(u"elimina")

        self.horizontalLayout.addWidget(self.elimina)

        self.edita = QPushButton(FuenteClasificacionListClass)
        self.edita.setObjectName(u"edita")

        self.horizontalLayout.addWidget(self.edita)

        self.anade = QPushButton(FuenteClasificacionListClass)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(FuenteClasificacionListClass)
        self.tabla.customContextMenuRequested.connect(FuenteClasificacionListClass.showContextMenu)

        QMetaObject.connectSlotsByName(FuenteClasificacionListClass)
    # setupUi

    def retranslateUi(self, FuenteClasificacionListClass):
        FuenteClasificacionListClass.setWindowTitle(QCoreApplication.translate("FuenteClasificacionListClass", u"Lista de clasificaci\u00f3n por fuente...", None))
        self.clipboardFuenteClasificacion.setText(QCoreApplication.translate("FuenteClasificacionListClass", u"Insertar desde portapapeles", None))
        self.guarda.setText(QCoreApplication.translate("FuenteClasificacionListClass", u"Guardar", None))
        self.descarta.setText(QCoreApplication.translate("FuenteClasificacionListClass", u"Descartar", None))
        self.elimina.setText(QCoreApplication.translate("FuenteClasificacionListClass", u"Eliminar", None))
        self.edita.setText(QCoreApplication.translate("FuenteClasificacionListClass", u"Editar", None))
        self.anade.setText(QCoreApplication.translate("FuenteClasificacionListClass", u"A\u00f1adir", None))
    # retranslateUi

