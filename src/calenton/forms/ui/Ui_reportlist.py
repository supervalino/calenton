# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reportlist.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from ...widgets.datalist import DataList

class Ui_ReportListClass(object):
    def setupUi(self, ReportListClass):
        if not ReportListClass.objectName():
            ReportListClass.setObjectName(u"ReportListClass")
        ReportListClass.resize(614, 457)
        self.insertFromClipboard = QAction(ReportListClass)
        self.insertFromClipboard.setObjectName(u"insertFromClipboard")
        self.verticalLayout = QVBoxLayout(ReportListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(ReportListClass)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.informeAc = QLineEdit(ReportListClass)
        self.informeAc.setObjectName(u"informeAc")
        self.informeAc.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.informeAc)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabla = QTableWidget(ReportListClass)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.tabla)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.crear = QPushButton(ReportListClass)
        self.crear.setObjectName(u"crear")

        self.horizontalLayout.addWidget(self.crear)

        self.activar = QPushButton(ReportListClass)
        self.activar.setObjectName(u"activar")

        self.horizontalLayout.addWidget(self.activar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.elimina = QPushButton(ReportListClass)
        self.elimina.setObjectName(u"elimina")

        self.horizontalLayout.addWidget(self.elimina)

        self.edita = QPushButton(ReportListClass)
        self.edita.setObjectName(u"edita")

        self.horizontalLayout.addWidget(self.edita)

        self.anade = QPushButton(ReportListClass)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.elimina, self.edita)
        QWidget.setTabOrder(self.edita, self.anade)

        self.retranslateUi(ReportListClass)
        self.insertFromClipboard.triggered["bool"].connect(ReportListClass.dataFromClipboard)

        QMetaObject.connectSlotsByName(ReportListClass)
    # setupUi

    def retranslateUi(self, ReportListClass):
        ReportListClass.setWindowTitle(QCoreApplication.translate("ReportListClass", u"Lista de informes", None))
        self.insertFromClipboard.setText(QCoreApplication.translate("ReportListClass", u"Insertar desde portapapeles", None))
        self.label.setText(QCoreApplication.translate("ReportListClass", u"Informe Activo:", None))
        self.crear.setText(QCoreApplication.translate("ReportListClass", u"Crear", None))
        self.activar.setText(QCoreApplication.translate("ReportListClass", u"Activar", None))
        self.elimina.setText(QCoreApplication.translate("ReportListClass", u"Eliminar", None))
        self.edita.setText(QCoreApplication.translate("ReportListClass", u"Editar", None))
        self.anade.setText(QCoreApplication.translate("ReportListClass", u"A\u00f1adir", None))
    # retranslateUi

