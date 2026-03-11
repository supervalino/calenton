# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapaforozonalist.ui'
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
from PyQt6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableView, QTreeView,
    QVBoxLayout, QWidget)

from ...widgets.datalist import DataList

class Ui_MapAforoZonaListClass(object):
    def setupUi(self, MapAforoZonaListClass):
        if not MapAforoZonaListClass.objectName():
            MapAforoZonaListClass.setObjectName(u"MapAforoZonaListClass")
        MapAforoZonaListClass.resize(492, 370)
        self.insertFromClipboard = QAction(MapAforoZonaListClass)
        self.insertFromClipboard.setObjectName(u"insertFromClipboard")
        self.deleteAll = QAction(MapAforoZonaListClass)
        self.deleteAll.setObjectName(u"deleteAll")
        self.surfaceGeneration = QAction(MapAforoZonaListClass)
        self.surfaceGeneration.setObjectName(u"surfaceGeneration")
        self.one2OneGeneration = QAction(MapAforoZonaListClass)
        self.one2OneGeneration.setObjectName(u"one2OneGeneration")
        self.verticalLayout_2 = QVBoxLayout(MapAforoZonaListClass)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tablaDatos = QTabWidget(MapAforoZonaListClass)
        self.tablaDatos.setObjectName(u"tablaDatos")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.comboEscenario = QComboBox(self.tab)
        self.comboEscenario.setObjectName(u"comboEscenario")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboEscenario.sizePolicy().hasHeightForWidth())
        self.comboEscenario.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.comboEscenario)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tablaFuentes = QTableView(self.tab)
        self.tablaFuentes.setObjectName(u"tablaFuentes")

        self.verticalLayout_3.addWidget(self.tablaFuentes)

        self.tablaDatos.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comboTipoClasificacion = QComboBox(self.tab_2)
        self.comboTipoClasificacion.setObjectName(u"comboTipoClasificacion")
        sizePolicy.setHeightForWidth(self.comboTipoClasificacion.sizePolicy().hasHeightForWidth())
        self.comboTipoClasificacion.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.comboTipoClasificacion)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.treeView = QTreeView(self.tab_2)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_4.addWidget(self.treeView)

        self.tablaDatos.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableView_2 = QTableView(self.tab_4)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_5.addWidget(self.tableView_2)

        self.tablaDatos.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout = QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tablaMap = QTableView(self.tab_3)
        self.tablaMap.setObjectName(u"tablaMap")
        self.tablaMap.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tablaMap.setEditTriggers(QAbstractItemView.EditTrigger.SelectedClicked)
        self.tablaMap.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.tablaMap)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.guardar = QPushButton(self.tab_3)
        self.guardar.setObjectName(u"guardar")

        self.horizontalLayout.addWidget(self.guardar)

        self.descartar = QPushButton(self.tab_3)
        self.descartar.setObjectName(u"descartar")

        self.horizontalLayout.addWidget(self.descartar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.elimina = QPushButton(self.tab_3)
        self.elimina.setObjectName(u"elimina")

        self.horizontalLayout.addWidget(self.elimina)

        self.edita = QPushButton(self.tab_3)
        self.edita.setObjectName(u"edita")

        self.horizontalLayout.addWidget(self.edita)

        self.anade = QPushButton(self.tab_3)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tablaDatos.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tablaDatos)

        QWidget.setTabOrder(self.tablaMap, self.elimina)
        QWidget.setTabOrder(self.elimina, self.edita)
        QWidget.setTabOrder(self.edita, self.anade)

        self.retranslateUi(MapAforoZonaListClass)
        self.tablaMap.customContextMenuRequested.connect(MapAforoZonaListClass.showContextMenu)

        self.tablaDatos.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MapAforoZonaListClass)
    # setupUi

    def retranslateUi(self, MapAforoZonaListClass):
        MapAforoZonaListClass.setWindowTitle(QCoreApplication.translate("MapAforoZonaListClass", u"Contribuci\u00f3n de contaminantes por aforo y zona", None))
        self.insertFromClipboard.setText(QCoreApplication.translate("MapAforoZonaListClass", u"Insertar desde portapapeles", None))
        self.deleteAll.setText(QCoreApplication.translate("MapAforoZonaListClass", u"Borrar todos", None))
        self.surfaceGeneration.setText(QCoreApplication.translate("MapAforoZonaListClass", u"Generar por superficie", None))
        self.one2OneGeneration.setText(QCoreApplication.translate("MapAforoZonaListClass", u"Generar uno a uno", None))
        self.label.setText(QCoreApplication.translate("MapAforoZonaListClass", u"Escenario", None))
        self.tablaDatos.setTabText(self.tablaDatos.indexOf(self.tab), QCoreApplication.translate("MapAforoZonaListClass", u"Fuentes", None))
        self.label_2.setText(QCoreApplication.translate("MapAforoZonaListClass", u"Tipo  de clasificaci\u00f3n", None))
        self.tablaDatos.setTabText(self.tablaDatos.indexOf(self.tab_2), QCoreApplication.translate("MapAforoZonaListClass", u"Clasificaci\u00f3n", None))
        self.tablaDatos.setTabText(self.tablaDatos.indexOf(self.tab_4), QCoreApplication.translate("MapAforoZonaListClass", u"Datos", None))
        self.guardar.setText(QCoreApplication.translate("MapAforoZonaListClass", u"Guardar", None))
        self.descartar.setText(QCoreApplication.translate("MapAforoZonaListClass", u"Descartar", None))
        self.elimina.setText(QCoreApplication.translate("MapAforoZonaListClass", u"Eliminar", None))
        self.edita.setText(QCoreApplication.translate("MapAforoZonaListClass", u"Editar", None))
        self.anade.setText(QCoreApplication.translate("MapAforoZonaListClass", u"A\u00f1adir", None))
        self.tablaDatos.setTabText(self.tablaDatos.indexOf(self.tab_3), QCoreApplication.translate("MapAforoZonaListClass", u"Distribuci\u00f3n por zona", None))
    # retranslateUi

