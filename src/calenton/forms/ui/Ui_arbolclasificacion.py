# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arbolclasificacion.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableView, QTreeView, QVBoxLayout, QWidget)

from ...widgets.datalist import DataList

class Ui_ArbolClasificacionClass(object):
    def setupUi(self, ArbolClasificacionClass):
        if not ArbolClasificacionClass.objectName():
            ArbolClasificacionClass.setObjectName(u"ArbolClasificacionClass")
        ArbolClasificacionClass.resize(572, 465)
        self.clipboardDato = QAction(ArbolClasificacionClass)
        self.clipboardDato.setObjectName(u"clipboardDato")
        self.verticalLayout = QVBoxLayout(ArbolClasificacionClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(ArbolClasificacionClass)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tablaTipos = QTableView(self.tab_3)
        self.tablaTipos.setObjectName(u"tablaTipos")
        self.tablaTipos.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_3.addWidget(self.tablaTipos)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.guardaTipos = QPushButton(self.tab_3)
        self.guardaTipos.setObjectName(u"guardaTipos")

        self.horizontalLayout.addWidget(self.guardaTipos)

        self.descartaTipos = QPushButton(self.tab_3)
        self.descartaTipos.setObjectName(u"descartaTipos")

        self.horizontalLayout.addWidget(self.descartaTipos)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.eliminaTipos = QPushButton(self.tab_3)
        self.eliminaTipos.setObjectName(u"eliminaTipos")

        self.horizontalLayout.addWidget(self.eliminaTipos)

        self.editaTipos = QPushButton(self.tab_3)
        self.editaTipos.setObjectName(u"editaTipos")

        self.horizontalLayout.addWidget(self.editaTipos)

        self.anadeTipos = QPushButton(self.tab_3)
        self.anadeTipos.setObjectName(u"anadeTipos")

        self.horizontalLayout.addWidget(self.anadeTipos)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.arbolClasificacion = QTreeView(self.tab)
        self.arbolClasificacion.setObjectName(u"arbolClasificacion")
        self.arbolClasificacion.setAlternatingRowColors(True)
        self.arbolClasificacion.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_2.addWidget(self.arbolClasificacion)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tablaDato = QTableView(self.tab_2)
        self.tablaDato.setObjectName(u"tablaDato")
        self.tablaDato.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tablaDato.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_4.addWidget(self.tablaDato)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.guardaDato = QPushButton(self.tab_2)
        self.guardaDato.setObjectName(u"guardaDato")

        self.horizontalLayout_2.addWidget(self.guardaDato)

        self.descartaDato = QPushButton(self.tab_2)
        self.descartaDato.setObjectName(u"descartaDato")

        self.horizontalLayout_2.addWidget(self.descartaDato)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.eliminaDato = QPushButton(self.tab_2)
        self.eliminaDato.setObjectName(u"eliminaDato")

        self.horizontalLayout_2.addWidget(self.eliminaDato)

        self.editaDato = QPushButton(self.tab_2)
        self.editaDato.setObjectName(u"editaDato")

        self.horizontalLayout_2.addWidget(self.editaDato)

        self.anadeDato = QPushButton(self.tab_2)
        self.anadeDato.setObjectName(u"anadeDato")

        self.horizontalLayout_2.addWidget(self.anadeDato)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(ArbolClasificacionClass)
        self.tablaDato.customContextMenuRequested.connect(ArbolClasificacionClass.showContextMenu)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(ArbolClasificacionClass)
    # setupUi

    def retranslateUi(self, ArbolClasificacionClass):
        ArbolClasificacionClass.setWindowTitle(QCoreApplication.translate("ArbolClasificacionClass", u"Jerarqu\u00eda de clasificaci\u00f3n", None))
        self.clipboardDato.setText(QCoreApplication.translate("ArbolClasificacionClass", u"Insertar dato desde portapapeles", None))
#if QT_CONFIG(tooltip)
        self.clipboardDato.setToolTip(QCoreApplication.translate("ArbolClasificacionClass", u"Insertar dato desde portapapeles", None))
#endif // QT_CONFIG(tooltip)
        self.guardaTipos.setText(QCoreApplication.translate("ArbolClasificacionClass", u"Guardar", None))
        self.descartaTipos.setText(QCoreApplication.translate("ArbolClasificacionClass", u"Descartar", None))
        self.eliminaTipos.setText(QCoreApplication.translate("ArbolClasificacionClass", u"Eliminar", None))
        self.editaTipos.setText(QCoreApplication.translate("ArbolClasificacionClass", u"Editar", None))
        self.anadeTipos.setText(QCoreApplication.translate("ArbolClasificacionClass", u"A\u00f1adir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("ArbolClasificacionClass", u"Tipos de clasificaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ArbolClasificacionClass", u"Clasificaciones", None))
        self.guardaDato.setText(QCoreApplication.translate("ArbolClasificacionClass", u"Guardar", None))
        self.descartaDato.setText(QCoreApplication.translate("ArbolClasificacionClass", u"Descartar", None))
        self.eliminaDato.setText(QCoreApplication.translate("ArbolClasificacionClass", u"Eliminar", None))
        self.editaDato.setText(QCoreApplication.translate("ArbolClasificacionClass", u"Editar", None))
        self.anadeDato.setText(QCoreApplication.translate("ArbolClasificacionClass", u"A\u00f1adir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ArbolClasificacionClass", u"Datos", None))
    # retranslateUi

