# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'escenariolist.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

from ...widgets.datalist import DataList

class Ui_EscenarioListClass(object):
    def setupUi(self, EscenarioListClass):
        if not EscenarioListClass.objectName():
            EscenarioListClass.setObjectName(u"EscenarioListClass")
        EscenarioListClass.resize(479, 387)
        self.verticalLayout = QVBoxLayout(EscenarioListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(EscenarioListClass)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tablaEscenario = QTableView(self.tab)
        self.tablaEscenario.setObjectName(u"tablaEscenario")

        self.verticalLayout_2.addWidget(self.tablaEscenario)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.duplicaEscenario = QPushButton(self.tab)
        self.duplicaEscenario.setObjectName(u"duplicaEscenario")

        self.horizontalLayout.addWidget(self.duplicaEscenario)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.eliminaEscenario = QPushButton(self.tab)
        self.eliminaEscenario.setObjectName(u"eliminaEscenario")

        self.horizontalLayout.addWidget(self.eliminaEscenario)

        self.editaEscenario = QPushButton(self.tab)
        self.editaEscenario.setObjectName(u"editaEscenario")

        self.horizontalLayout.addWidget(self.editaEscenario)

        self.anadeEscenario = QPushButton(self.tab)
        self.anadeEscenario.setObjectName(u"anadeEscenario")

        self.horizontalLayout.addWidget(self.anadeEscenario)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tablaOrigen = QTableView(self.tab_2)
        self.tablaOrigen.setObjectName(u"tablaOrigen")
        self.tablaOrigen.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaOrigen.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_3.addWidget(self.tablaOrigen)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.eliminaOrigen = QPushButton(self.tab_2)
        self.eliminaOrigen.setObjectName(u"eliminaOrigen")

        self.horizontalLayout_2.addWidget(self.eliminaOrigen)

        self.editaOrigen = QPushButton(self.tab_2)
        self.editaOrigen.setObjectName(u"editaOrigen")

        self.horizontalLayout_2.addWidget(self.editaOrigen)

        self.anadeOrigen = QPushButton(self.tab_2)
        self.anadeOrigen.setObjectName(u"anadeOrigen")

        self.horizontalLayout_2.addWidget(self.anadeOrigen)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tablaParametro = QTableView(self.tab_3)
        self.tablaParametro.setObjectName(u"tablaParametro")
        self.tablaParametro.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaParametro.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_4.addWidget(self.tablaParametro)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.eliminaParametro = QPushButton(self.tab_3)
        self.eliminaParametro.setObjectName(u"eliminaParametro")

        self.horizontalLayout_3.addWidget(self.eliminaParametro)

        self.editaParametro = QPushButton(self.tab_3)
        self.editaParametro.setObjectName(u"editaParametro")

        self.horizontalLayout_3.addWidget(self.editaParametro)

        self.anadeParametro = QPushButton(self.tab_3)
        self.anadeParametro.setObjectName(u"anadeParametro")

        self.horizontalLayout_3.addWidget(self.anadeParametro)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tablaTipoDato = QTableView(self.tab_4)
        self.tablaTipoDato.setObjectName(u"tablaTipoDato")
        self.tablaTipoDato.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaTipoDato.setAlternatingRowColors(True)
        self.tablaTipoDato.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_5.addWidget(self.tablaTipoDato)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.guardaTipoDato = QPushButton(self.tab_4)
        self.guardaTipoDato.setObjectName(u"guardaTipoDato")

        self.horizontalLayout_4.addWidget(self.guardaTipoDato)

        self.descartaTipoDato = QPushButton(self.tab_4)
        self.descartaTipoDato.setObjectName(u"descartaTipoDato")

        self.horizontalLayout_4.addWidget(self.descartaTipoDato)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.eliminaTipoDato = QPushButton(self.tab_4)
        self.eliminaTipoDato.setObjectName(u"eliminaTipoDato")

        self.horizontalLayout_4.addWidget(self.eliminaTipoDato)

        self.editaTipoDato = QPushButton(self.tab_4)
        self.editaTipoDato.setObjectName(u"editaTipoDato")

        self.horizontalLayout_4.addWidget(self.editaTipoDato)

        self.anadeTipoDato = QPushButton(self.tab_4)
        self.anadeTipoDato.setObjectName(u"anadeTipoDato")

        self.horizontalLayout_4.addWidget(self.anadeTipoDato)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(EscenarioListClass)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EscenarioListClass)
    # setupUi

    def retranslateUi(self, EscenarioListClass):
        EscenarioListClass.setWindowTitle(QCoreApplication.translate("EscenarioListClass", u"Lista de escenarios", None))
        self.duplicaEscenario.setText(QCoreApplication.translate("EscenarioListClass", u"Duplicar", None))
        self.eliminaEscenario.setText(QCoreApplication.translate("EscenarioListClass", u"Eliminar", None))
        self.editaEscenario.setText(QCoreApplication.translate("EscenarioListClass", u"Editar", None))
        self.anadeEscenario.setText(QCoreApplication.translate("EscenarioListClass", u"A\u00f1adir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("EscenarioListClass", u"Escenarios", None))
        self.eliminaOrigen.setText(QCoreApplication.translate("EscenarioListClass", u"Eliminar", None))
        self.editaOrigen.setText(QCoreApplication.translate("EscenarioListClass", u"Editar", None))
        self.anadeOrigen.setText(QCoreApplication.translate("EscenarioListClass", u"A\u00f1adir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("EscenarioListClass", u"Or\u00edgenes", None))
        self.eliminaParametro.setText(QCoreApplication.translate("EscenarioListClass", u"Eliminar", None))
        self.editaParametro.setText(QCoreApplication.translate("EscenarioListClass", u"Editar", None))
        self.anadeParametro.setText(QCoreApplication.translate("EscenarioListClass", u"A\u00f1adir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("EscenarioListClass", u"Par\u00e1metros", None))
        self.guardaTipoDato.setText(QCoreApplication.translate("EscenarioListClass", u"Guardar", None))
        self.descartaTipoDato.setText(QCoreApplication.translate("EscenarioListClass", u"Descartar", None))
        self.eliminaTipoDato.setText(QCoreApplication.translate("EscenarioListClass", u"Eliminar", None))
        self.editaTipoDato.setText(QCoreApplication.translate("EscenarioListClass", u"Editar", None))
        self.anadeTipoDato.setText(QCoreApplication.translate("EscenarioListClass", u"A\u00f1adir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("EscenarioListClass", u"Datos geogr\u00e1ficos", None))
    # retranslateUi

