# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tablelist.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from ts import TComboBox
from ...widgets.datalist import DataList

class Ui_TableListClass(object):
    def setupUi(self, TableListClass):
        if not TableListClass.objectName():
            TableListClass.setObjectName(u"TableListClass")
        TableListClass.resize(614, 457)
        self.insertFromClipboard = QAction(TableListClass)
        self.insertFromClipboard.setObjectName(u"insertFromClipboard")
        self.verticalLayout = QVBoxLayout(TableListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(TableListClass)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.escenario = TComboBox(TableListClass)
        self.escenario.setObjectName(u"escenario")
        self.escenario.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.escenario)

        self.horizontalSpacer_2 = QSpacerItem(168, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabla = QTableWidget(TableListClass)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tabla)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.crear = QPushButton(TableListClass)
        self.crear.setObjectName(u"crear")

        self.horizontalLayout.addWidget(self.crear)

        self.crearTodas = QPushButton(TableListClass)
        self.crearTodas.setObjectName(u"crearTodas")

        self.horizontalLayout.addWidget(self.crearTodas)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.recarga = QPushButton(TableListClass)
        self.recarga.setObjectName(u"recarga")

        self.horizontalLayout.addWidget(self.recarga)

        self.elimina = QPushButton(TableListClass)
        self.elimina.setObjectName(u"elimina")

        self.horizontalLayout.addWidget(self.elimina)

        self.edita = QPushButton(TableListClass)
        self.edita.setObjectName(u"edita")

        self.horizontalLayout.addWidget(self.edita)

        self.anade = QPushButton(TableListClass)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.escenario, self.tabla)
        QWidget.setTabOrder(self.tabla, self.crear)
        QWidget.setTabOrder(self.crear, self.crearTodas)
        QWidget.setTabOrder(self.crearTodas, self.recarga)
        QWidget.setTabOrder(self.recarga, self.elimina)
        QWidget.setTabOrder(self.elimina, self.edita)
        QWidget.setTabOrder(self.edita, self.anade)

        self.retranslateUi(TableListClass)
        self.insertFromClipboard.triggered["bool"].connect(TableListClass.dataFromClipboard)

        QMetaObject.connectSlotsByName(TableListClass)
    # setupUi

    def retranslateUi(self, TableListClass):
        TableListClass.setWindowTitle(QCoreApplication.translate("TableListClass", u"Lista de tablas", None))
        self.insertFromClipboard.setText(QCoreApplication.translate("TableListClass", u"Insertar desde portapapeles", None))
        self.label.setText(QCoreApplication.translate("TableListClass", u"Escenario:", None))
        self.crear.setText(QCoreApplication.translate("TableListClass", u"Crear Tabla", None))
        self.crearTodas.setText(QCoreApplication.translate("TableListClass", u"Crear Todas", None))
        self.recarga.setText(QCoreApplication.translate("TableListClass", u"Recargar", None))
        self.elimina.setText(QCoreApplication.translate("TableListClass", u"Eliminar", None))
        self.edita.setText(QCoreApplication.translate("TableListClass", u"Editar", None))
        self.anade.setText(QCoreApplication.translate("TableListClass", u"A\u00f1adir", None))
    # retranslateUi

