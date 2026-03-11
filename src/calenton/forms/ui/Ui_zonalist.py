# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zonalist.ui'
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
    QTableView, QVBoxLayout, QWidget)

from ts import (TComboBox, TTabWidget)
from ...widgets.datalist import DataList

class Ui_ZonaListClass(object):
    def setupUi(self, ZonaListClass):
        if not ZonaListClass.objectName():
            ZonaListClass.setObjectName(u"ZonaListClass")
        ZonaListClass.resize(500, 376)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ZonaListClass.sizePolicy().hasHeightForWidth())
        ZonaListClass.setSizePolicy(sizePolicy)
        ZonaListClass.setMinimumSize(QSize(500, 0))
        self.clipboardDatos = QAction(ZonaListClass)
        self.clipboardDatos.setObjectName(u"clipboardDatos")
        self.clipboardParametros = QAction(ZonaListClass)
        self.clipboardParametros.setObjectName(u"clipboardParametros")
        self.verticalLayout_2 = QVBoxLayout(ZonaListClass)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tab = TTabWidget(ZonaListClass)
        self.tab.setObjectName(u"tab")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout = QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tablaNiveles = QTableView(self.tab_4)
        self.tablaNiveles.setObjectName(u"tablaNiveles")
        self.tablaNiveles.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.tablaNiveles)

        self.tab.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_3 = QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabla = QTableView(self.tab_5)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla.setAlternatingRowColors(True)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_3.addWidget(self.tabla)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.anade = QPushButton(self.tab_5)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)

        self.edita = QPushButton(self.tab_5)
        self.edita.setObjectName(u"edita")
        self.edita.setEnabled(False)

        self.horizontalLayout.addWidget(self.edita)

        self.elimina = QPushButton(self.tab_5)
        self.elimina.setObjectName(u"elimina")
        self.elimina.setEnabled(False)

        self.horizontalLayout.addWidget(self.elimina)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tab.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_5 = QVBoxLayout(self.tab_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.tab_6)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.escenario = TComboBox(self.tab_6)
        self.escenario.setObjectName(u"escenario")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.escenario.sizePolicy().hasHeightForWidth())
        self.escenario.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.escenario)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.tablaDatos = QTableView(self.tab_6)
        self.tablaDatos.setObjectName(u"tablaDatos")
        self.tablaDatos.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tablaDatos.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)
        self.tablaDatos.setAlternatingRowColors(True)

        self.verticalLayout_5.addWidget(self.tablaDatos)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.guardaDatos = QPushButton(self.tab_6)
        self.guardaDatos.setObjectName(u"guardaDatos")

        self.horizontalLayout_2.addWidget(self.guardaDatos)

        self.descartaDatos = QPushButton(self.tab_6)
        self.descartaDatos.setObjectName(u"descartaDatos")

        self.horizontalLayout_2.addWidget(self.descartaDatos)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.anadeDatos = QPushButton(self.tab_6)
        self.anadeDatos.setObjectName(u"anadeDatos")

        self.horizontalLayout_2.addWidget(self.anadeDatos)

        self.eliminaDatos = QPushButton(self.tab_6)
        self.eliminaDatos.setObjectName(u"eliminaDatos")

        self.horizontalLayout_2.addWidget(self.eliminaDatos)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.tab.addTab(self.tab_6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.escenarioParam = TComboBox(self.tab_2)
        self.escenarioParam.setObjectName(u"escenarioParam")

        self.horizontalLayout_5.addWidget(self.escenarioParam)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.tablaParametros = QTableView(self.tab_2)
        self.tablaParametros.setObjectName(u"tablaParametros")
        self.tablaParametros.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.verticalLayout_4.addWidget(self.tablaParametros)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.guardaParametros = QPushButton(self.tab_2)
        self.guardaParametros.setObjectName(u"guardaParametros")

        self.horizontalLayout_4.addWidget(self.guardaParametros)

        self.descartaParametros = QPushButton(self.tab_2)
        self.descartaParametros.setObjectName(u"descartaParametros")

        self.horizontalLayout_4.addWidget(self.descartaParametros)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.anadeParametros = QPushButton(self.tab_2)
        self.anadeParametros.setObjectName(u"anadeParametros")

        self.horizontalLayout_4.addWidget(self.anadeParametros)

        self.eliminaParametros = QPushButton(self.tab_2)
        self.eliminaParametros.setObjectName(u"eliminaParametros")

        self.horizontalLayout_4.addWidget(self.eliminaParametros)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.tab.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tab)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.escenario)
        self.label_2.setBuddy(self.escenarioParam)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.tablaNiveles, self.tab)
        QWidget.setTabOrder(self.tab, self.tabla)
        QWidget.setTabOrder(self.tabla, self.anade)
        QWidget.setTabOrder(self.anade, self.edita)
        QWidget.setTabOrder(self.edita, self.elimina)
        QWidget.setTabOrder(self.elimina, self.escenario)
        QWidget.setTabOrder(self.escenario, self.tablaDatos)
        QWidget.setTabOrder(self.tablaDatos, self.anadeDatos)
        QWidget.setTabOrder(self.anadeDatos, self.eliminaDatos)
        QWidget.setTabOrder(self.eliminaDatos, self.guardaDatos)
        QWidget.setTabOrder(self.guardaDatos, self.descartaDatos)
        QWidget.setTabOrder(self.descartaDatos, self.escenarioParam)
        QWidget.setTabOrder(self.escenarioParam, self.tablaParametros)
        QWidget.setTabOrder(self.tablaParametros, self.anadeParametros)
        QWidget.setTabOrder(self.anadeParametros, self.eliminaParametros)
        QWidget.setTabOrder(self.eliminaParametros, self.guardaParametros)
        QWidget.setTabOrder(self.guardaParametros, self.descartaParametros)

        self.retranslateUi(ZonaListClass)
        self.tablaDatos.customContextMenuRequested.connect(ZonaListClass.showContextMenu)
        self.tablaParametros.customContextMenuRequested.connect(ZonaListClass.showContextMenu)

        self.tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ZonaListClass)
    # setupUi

    def retranslateUi(self, ZonaListClass):
        ZonaListClass.setWindowTitle(QCoreApplication.translate("ZonaListClass", u"Form", None))
        self.clipboardDatos.setText(QCoreApplication.translate("ZonaListClass", u"Insertar desde el portapapeles", None))
        self.clipboardParametros.setText(QCoreApplication.translate("ZonaListClass", u"Insertar desde el portapapeles...", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_4), QCoreApplication.translate("ZonaListClass", u"Niveles", None))
        self.anade.setText(QCoreApplication.translate("ZonaListClass", u"A\u00f1adir...", None))
        self.edita.setText(QCoreApplication.translate("ZonaListClass", u"Editar...", None))
        self.elimina.setText(QCoreApplication.translate("ZonaListClass", u"Eliminar", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_5), QCoreApplication.translate("ZonaListClass", u"Zonas", None))
        self.label.setText(QCoreApplication.translate("ZonaListClass", u"Escenario", None))
        self.guardaDatos.setText(QCoreApplication.translate("ZonaListClass", u"Guardar", None))
        self.descartaDatos.setText(QCoreApplication.translate("ZonaListClass", u"Descartar", None))
        self.anadeDatos.setText(QCoreApplication.translate("ZonaListClass", u"A\u00f1adir", None))
        self.eliminaDatos.setText(QCoreApplication.translate("ZonaListClass", u"Eliminar", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_6), QCoreApplication.translate("ZonaListClass", u"Datos", None))
        self.label_2.setText(QCoreApplication.translate("ZonaListClass", u"Escenario", None))
        self.guardaParametros.setText(QCoreApplication.translate("ZonaListClass", u"Guardar", None))
        self.descartaParametros.setText(QCoreApplication.translate("ZonaListClass", u"Descartar", None))
        self.anadeParametros.setText(QCoreApplication.translate("ZonaListClass", u"A\u00f1adir", None))
        self.eliminaParametros.setText(QCoreApplication.translate("ZonaListClass", u"Eliminar", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_2), QCoreApplication.translate("ZonaListClass", u"Par\u00e1metros", None))
    # retranslateUi

