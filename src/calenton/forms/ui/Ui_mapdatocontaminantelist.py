# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapdatocontaminantelist.ui'
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
    QTabWidget, QTableView, QTreeView, QVBoxLayout,
    QWidget)

from ts import TComboBox
from ...widgets.datalist import DataList

class Ui_MapDatoContaminanteListClass(object):
    def setupUi(self, MapDatoContaminanteListClass):
        if not MapDatoContaminanteListClass.objectName():
            MapDatoContaminanteListClass.setObjectName(u"MapDatoContaminanteListClass")
        MapDatoContaminanteListClass.resize(513, 363)
        self.clipboardMapDatoContaminante = QAction(MapDatoContaminanteListClass)
        self.clipboardMapDatoContaminante.setObjectName(u"clipboardMapDatoContaminante")
        self.verticalLayout_5 = QVBoxLayout(MapDatoContaminanteListClass)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(MapDatoContaminanteListClass)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tablaEscenario = QTableView(self.tab)
        self.tablaEscenario.setObjectName(u"tablaEscenario")
        self.tablaEscenario.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaEscenario.setAlternatingRowColors(True)
        self.tablaEscenario.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablaEscenario.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.tablaEscenario)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label)

        self.comboTipoClasificacion = TComboBox(self.tab_2)
        self.comboTipoClasificacion.setObjectName(u"comboTipoClasificacion")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboTipoClasificacion.sizePolicy().hasHeightForWidth())
        self.comboTipoClasificacion.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.comboTipoClasificacion)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.arbolClasificacion = QTreeView(self.tab_2)
        self.arbolClasificacion.setObjectName(u"arbolClasificacion")
        self.arbolClasificacion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.arbolClasificacion.setAlternatingRowColors(True)

        self.verticalLayout_3.addWidget(self.arbolClasificacion)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_6 = QVBoxLayout(self.tab_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tablaMapClas = QTableView(self.tab_5)
        self.tablaMapClas.setObjectName(u"tablaMapClas")
        self.tablaMapClas.setContextMenuPolicy(Qt.CustomContextMenu)

        self.verticalLayout_6.addWidget(self.tablaMapClas)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.guardaMapClas = QPushButton(self.tab_5)
        self.guardaMapClas.setObjectName(u"guardaMapClas")

        self.horizontalLayout_3.addWidget(self.guardaMapClas)

        self.descartaMapClas = QPushButton(self.tab_5)
        self.descartaMapClas.setObjectName(u"descartaMapClas")

        self.horizontalLayout_3.addWidget(self.descartaMapClas)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.eliminaMapClas = QPushButton(self.tab_5)
        self.eliminaMapClas.setObjectName(u"eliminaMapClas")

        self.horizontalLayout_3.addWidget(self.eliminaMapClas)

        self.editaMapClas = QPushButton(self.tab_5)
        self.editaMapClas.setObjectName(u"editaMapClas")

        self.horizontalLayout_3.addWidget(self.editaMapClas)

        self.anadeMapClas = QPushButton(self.tab_5)
        self.anadeMapClas.setObjectName(u"anadeMapClas")

        self.horizontalLayout_3.addWidget(self.anadeMapClas)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_4 = QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tablaDato = QTableView(self.tab_4)
        self.tablaDato.setObjectName(u"tablaDato")
        self.tablaDato.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaDato.setAlternatingRowColors(True)
        self.tablaDato.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablaDato.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_4.addWidget(self.tablaDato)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout = QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tablaMap = QTableView(self.tab_3)
        self.tablaMap.setObjectName(u"tablaMap")
        self.tablaMap.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tablaMap.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.tablaMap.setAlternatingRowColors(True)
        self.tablaMap.setSelectionBehavior(QAbstractItemView.SelectRows)

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

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.comboTipoClasificacion)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.tablaEscenario, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.arbolClasificacion)
        QWidget.setTabOrder(self.arbolClasificacion, self.comboTipoClasificacion)
        QWidget.setTabOrder(self.comboTipoClasificacion, self.tablaMapClas)
        QWidget.setTabOrder(self.tablaMapClas, self.guardaMapClas)
        QWidget.setTabOrder(self.guardaMapClas, self.descartaMapClas)
        QWidget.setTabOrder(self.descartaMapClas, self.eliminaMapClas)
        QWidget.setTabOrder(self.eliminaMapClas, self.editaMapClas)
        QWidget.setTabOrder(self.editaMapClas, self.anadeMapClas)
        QWidget.setTabOrder(self.anadeMapClas, self.tablaDato)
        QWidget.setTabOrder(self.tablaDato, self.tablaMap)
        QWidget.setTabOrder(self.tablaMap, self.guardar)
        QWidget.setTabOrder(self.guardar, self.descartar)
        QWidget.setTabOrder(self.descartar, self.elimina)
        QWidget.setTabOrder(self.elimina, self.edita)
        QWidget.setTabOrder(self.edita, self.anade)

        self.retranslateUi(MapDatoContaminanteListClass)
        self.tablaMap.customContextMenuRequested.connect(MapDatoContaminanteListClass.showContextMenu)
        self.tablaMapClas.customContextMenuRequested.connect(MapDatoContaminanteListClass.showContextMenu)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MapDatoContaminanteListClass)
    # setupUi

    def retranslateUi(self, MapDatoContaminanteListClass):
        MapDatoContaminanteListClass.setWindowTitle(QCoreApplication.translate("MapDatoContaminanteListClass", u"Datos de conversi\u00f3n de contaminantes", None))
        self.clipboardMapDatoContaminante.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"Inserta desde portapapeles", None))
#if QT_CONFIG(tooltip)
        self.clipboardMapDatoContaminante.setToolTip(QCoreApplication.translate("MapDatoContaminanteListClass", u"Inserta desde portapapeles", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MapDatoContaminanteListClass", u"Escenario", None))
        self.label.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"Tipo de clasificaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MapDatoContaminanteListClass", u"Clasificaci\u00f3n", None))
        self.guardaMapClas.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"Guardar", None))
        self.descartaMapClas.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"Descartar", None))
        self.eliminaMapClas.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"Eliminar", None))
        self.editaMapClas.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"Editar", None))
        self.anadeMapClas.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"A\u00f1adir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MapDatoContaminanteListClass", u"F\u00f3rmulas por clasificaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MapDatoContaminanteListClass", u"Dato", None))
        self.guardar.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"Guardar", None))
        self.descartar.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"Descartar", None))
        self.elimina.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"Eliminar", None))
        self.edita.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"Editar", None))
        self.anade.setText(QCoreApplication.translate("MapDatoContaminanteListClass", u"A\u00f1adir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MapDatoContaminanteListClass", u"F\u00f3rmulas por dato", None))
    # retranslateUi

