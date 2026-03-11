# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contaminantezonalist.ui'
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
from PyQt6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QWidget)

from ...widgets.datalist import DataList

class Ui_ContaminanteZonaListClass(object):
    def setupUi(self, ContaminanteZonaListClass):
        if not ContaminanteZonaListClass.objectName():
            ContaminanteZonaListClass.setObjectName(u"ContaminanteZonaListClass")
        ContaminanteZonaListClass.resize(614, 457)
        self.insertFromClipboard = QAction(ContaminanteZonaListClass)
        self.insertFromClipboard.setObjectName(u"insertFromClipboard")
        self.gridLayout = QGridLayout(ContaminanteZonaListClass)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabla = QTableView(ContaminanteZonaListClass)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tabla.setEditTriggers(QAbstractItemView.EditTrigger.SelectedClicked)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.gridLayout.addWidget(self.tabla, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.guardar = QPushButton(ContaminanteZonaListClass)
        self.guardar.setObjectName(u"guardar")

        self.horizontalLayout.addWidget(self.guardar)

        self.descartar = QPushButton(ContaminanteZonaListClass)
        self.descartar.setObjectName(u"descartar")

        self.horizontalLayout.addWidget(self.descartar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.elimina = QPushButton(ContaminanteZonaListClass)
        self.elimina.setObjectName(u"elimina")

        self.horizontalLayout.addWidget(self.elimina)

        self.edita = QPushButton(ContaminanteZonaListClass)
        self.edita.setObjectName(u"edita")

        self.horizontalLayout.addWidget(self.edita)

        self.anade = QPushButton(ContaminanteZonaListClass)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        QWidget.setTabOrder(self.tabla, self.elimina)
        QWidget.setTabOrder(self.elimina, self.edita)
        QWidget.setTabOrder(self.edita, self.anade)

        self.retranslateUi(ContaminanteZonaListClass)
        self.insertFromClipboard.triggered["bool"].connect(ContaminanteZonaListClass.dataFromClipboard)
        self.tabla.customContextMenuRequested.connect(ContaminanteZonaListClass.showContextMenu)

        QMetaObject.connectSlotsByName(ContaminanteZonaListClass)
    # setupUi

    def retranslateUi(self, ContaminanteZonaListClass):
        ContaminanteZonaListClass.setWindowTitle(QCoreApplication.translate("ContaminanteZonaListClass", u"Emisiones de contaminante por fuente", None))
        self.insertFromClipboard.setText(QCoreApplication.translate("ContaminanteZonaListClass", u"Insertar desde portapapeles", None))
        self.guardar.setText(QCoreApplication.translate("ContaminanteZonaListClass", u"Guardar", None))
        self.descartar.setText(QCoreApplication.translate("ContaminanteZonaListClass", u"Descartar", None))
        self.elimina.setText(QCoreApplication.translate("ContaminanteZonaListClass", u"Eliminar", None))
        self.edita.setText(QCoreApplication.translate("ContaminanteZonaListClass", u"Editar", None))
        self.anade.setText(QCoreApplication.translate("ContaminanteZonaListClass", u"A\u00f1adir", None))
    # retranslateUi

