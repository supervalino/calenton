# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fuentelist.ui'
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

from ts import (TComboBox, TSqlTableNavigator, TTabWidget)
from ...widgets.datalist import DataList

class Ui_FuenteListClass(object):
    def setupUi(self, FuenteListClass):
        if not FuenteListClass.objectName():
            FuenteListClass.setObjectName(u"FuenteListClass")
        FuenteListClass.resize(662, 338)
        FuenteListClass.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.clipboardAforo = QAction(FuenteListClass)
        self.clipboardAforo.setObjectName(u"clipboardAforo")
        self.clipboardDatoTabular = QAction(FuenteListClass)
        self.clipboardDatoTabular.setObjectName(u"clipboardDatoTabular")
        self.copyHeaderDatoTabular = QAction(FuenteListClass)
        self.copyHeaderDatoTabular.setObjectName(u"copyHeaderDatoTabular")
        self.clipboardDato = QAction(FuenteListClass)
        self.clipboardDato.setObjectName(u"clipboardDato")
        self.clipboardParametros = QAction(FuenteListClass)
        self.clipboardParametros.setObjectName(u"clipboardParametros")
        self.calcularAforo = QAction(FuenteListClass)
        self.calcularAforo.setObjectName(u"calcularAforo")
        self.calcularFuente = QAction(FuenteListClass)
        self.calcularFuente.setObjectName(u"calcularFuente")
        self.verticalLayout = QVBoxLayout(FuenteListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab = TTabWidget(FuenteListClass)
        self.tab.setObjectName(u"tab")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_2 = QVBoxLayout(self.tab_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.tab_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.escenario = TComboBox(self.tab_5)
        self.escenario.setObjectName(u"escenario")

        self.horizontalLayout_5.addWidget(self.escenario)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.tablaFuente = QTableView(self.tab_5)
        self.tablaFuente.setObjectName(u"tablaFuente")
        self.tablaFuente.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tablaFuente.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaFuente.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_2.addWidget(self.tablaFuente)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.deseleccionaFuente = QPushButton(self.tab_5)
        self.deseleccionaFuente.setObjectName(u"deseleccionaFuente")

        self.horizontalLayout.addWidget(self.deseleccionaFuente)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.eliminaFuente = QPushButton(self.tab_5)
        self.eliminaFuente.setObjectName(u"eliminaFuente")

        self.horizontalLayout.addWidget(self.eliminaFuente)

        self.editaFuente = QPushButton(self.tab_5)
        self.editaFuente.setObjectName(u"editaFuente")

        self.horizontalLayout.addWidget(self.editaFuente)

        self.anadeFuente = QPushButton(self.tab_5)
        self.anadeFuente.setObjectName(u"anadeFuente")

        self.horizontalLayout.addWidget(self.anadeFuente)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tab.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_6 = QVBoxLayout(self.tab_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tablaAforo = QTableView(self.tab_6)
        self.tablaAforo.setObjectName(u"tablaAforo")
        self.tablaAforo.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tablaAforo.setEditTriggers(QAbstractItemView.EditTrigger.SelectedClicked)
        self.tablaAforo.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_6.addWidget(self.tablaAforo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.guardaAforo = QPushButton(self.tab_6)
        self.guardaAforo.setObjectName(u"guardaAforo")

        self.horizontalLayout_2.addWidget(self.guardaAforo)

        self.descartaAforo = QPushButton(self.tab_6)
        self.descartaAforo.setObjectName(u"descartaAforo")

        self.horizontalLayout_2.addWidget(self.descartaAforo)

        self.deseleccionaAforo = QPushButton(self.tab_6)
        self.deseleccionaAforo.setObjectName(u"deseleccionaAforo")

        self.horizontalLayout_2.addWidget(self.deseleccionaAforo)

        self.buscaAforo = QPushButton(self.tab_6)
        self.buscaAforo.setObjectName(u"buscaAforo")

        self.horizontalLayout_2.addWidget(self.buscaAforo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.eliminaAforo = QPushButton(self.tab_6)
        self.eliminaAforo.setObjectName(u"eliminaAforo")

        self.horizontalLayout_2.addWidget(self.eliminaAforo)

        self.editaAforo = QPushButton(self.tab_6)
        self.editaAforo.setObjectName(u"editaAforo")

        self.horizontalLayout_2.addWidget(self.editaAforo)

        self.anadeAforo = QPushButton(self.tab_6)
        self.anadeAforo.setObjectName(u"anadeAforo")

        self.horizontalLayout_2.addWidget(self.anadeAforo)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.tab.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_3 = QVBoxLayout(self.tab_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tablaParametros = QTableView(self.tab_7)
        self.tablaParametros.setObjectName(u"tablaParametros")
        self.tablaParametros.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.verticalLayout_3.addWidget(self.tablaParametros)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.guardaParametros = QPushButton(self.tab_7)
        self.guardaParametros.setObjectName(u"guardaParametros")

        self.horizontalLayout_6.addWidget(self.guardaParametros)

        self.descartaParametros = QPushButton(self.tab_7)
        self.descartaParametros.setObjectName(u"descartaParametros")

        self.horizontalLayout_6.addWidget(self.descartaParametros)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.anadeParametros = QPushButton(self.tab_7)
        self.anadeParametros.setObjectName(u"anadeParametros")

        self.horizontalLayout_6.addWidget(self.anadeParametros)

        self.eliminaParametros = QPushButton(self.tab_7)
        self.eliminaParametros.setObjectName(u"eliminaParametros")

        self.horizontalLayout_6.addWidget(self.eliminaParametros)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.tab.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_7 = QVBoxLayout(self.tab_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tablaDato = QTableView(self.tab_8)
        self.tablaDato.setObjectName(u"tablaDato")
        self.tablaDato.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tablaDato.setEditTriggers(QAbstractItemView.EditTrigger.SelectedClicked)
        self.tablaDato.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_7.addWidget(self.tablaDato)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.guardaDato = QPushButton(self.tab_8)
        self.guardaDato.setObjectName(u"guardaDato")

        self.horizontalLayout_3.addWidget(self.guardaDato)

        self.descartaDato = QPushButton(self.tab_8)
        self.descartaDato.setObjectName(u"descartaDato")

        self.horizontalLayout_3.addWidget(self.descartaDato)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.eliminaDato = QPushButton(self.tab_8)
        self.eliminaDato.setObjectName(u"eliminaDato")

        self.horizontalLayout_3.addWidget(self.eliminaDato)

        self.editaDato = QPushButton(self.tab_8)
        self.editaDato.setObjectName(u"editaDato")

        self.horizontalLayout_3.addWidget(self.editaDato)

        self.anadeDato = QPushButton(self.tab_8)
        self.anadeDato.setObjectName(u"anadeDato")

        self.horizontalLayout_3.addWidget(self.anadeDato)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tab.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_8 = QVBoxLayout(self.tab_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tablaDatoTabular = QTableView(self.tab_9)
        self.tablaDatoTabular.setObjectName(u"tablaDatoTabular")
        self.tablaDatoTabular.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tablaDatoTabular.setAlternatingRowColors(True)

        self.verticalLayout_8.addWidget(self.tablaDatoTabular)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.guardaDatoTabular = QPushButton(self.tab_9)
        self.guardaDatoTabular.setObjectName(u"guardaDatoTabular")
        self.guardaDatoTabular.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.guardaDatoTabular)

        self.descartaDatoTabular = QPushButton(self.tab_9)
        self.descartaDatoTabular.setObjectName(u"descartaDatoTabular")
        self.descartaDatoTabular.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.descartaDatoTabular)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.eliminaDatoTabular = QPushButton(self.tab_9)
        self.eliminaDatoTabular.setObjectName(u"eliminaDatoTabular")
        self.eliminaDatoTabular.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.eliminaDatoTabular)

        self.editaDatoTabular = QPushButton(self.tab_9)
        self.editaDatoTabular.setObjectName(u"editaDatoTabular")
        self.editaDatoTabular.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.editaDatoTabular)

        self.anadeDatoTabular = QPushButton(self.tab_9)
        self.anadeDatoTabular.setObjectName(u"anadeDatoTabular")
        self.anadeDatoTabular.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.anadeDatoTabular)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.tab.addTab(self.tab_9, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.navValidado = TSqlTableNavigator(self.tab_2)
        self.navValidado.setObjectName(u"navValidado")
        self.navValidado.setAutoResizeRows(True)
        self.navValidado.setAutoResizeColumns(True)

        self.verticalLayout_4.addWidget(self.navValidado)

        self.tab.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.navResultados = TSqlTableNavigator(self.tab_3)
        self.navResultados.setObjectName(u"navResultados")
        self.navResultados.setAutoResizeRows(True)
        self.navResultados.setAutoResizeColumns(True)
        self.navResultados.setShowButtons(False)
        self.navResultados.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.navResultados.setAlternatingRowColors(True)
        self.navResultados.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.navResultados.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_5.addWidget(self.navResultados)

        self.tab.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tab)

        QWidget.setTabOrder(self.tablaFuente, self.deseleccionaFuente)
        QWidget.setTabOrder(self.deseleccionaFuente, self.eliminaFuente)
        QWidget.setTabOrder(self.eliminaFuente, self.editaFuente)
        QWidget.setTabOrder(self.editaFuente, self.anadeFuente)
        QWidget.setTabOrder(self.anadeFuente, self.tablaAforo)
        QWidget.setTabOrder(self.tablaAforo, self.guardaAforo)
        QWidget.setTabOrder(self.guardaAforo, self.descartaAforo)
        QWidget.setTabOrder(self.descartaAforo, self.deseleccionaAforo)
        QWidget.setTabOrder(self.deseleccionaAforo, self.buscaAforo)
        QWidget.setTabOrder(self.buscaAforo, self.eliminaAforo)
        QWidget.setTabOrder(self.eliminaAforo, self.editaAforo)
        QWidget.setTabOrder(self.editaAforo, self.anadeAforo)
        QWidget.setTabOrder(self.anadeAforo, self.tablaDato)
        QWidget.setTabOrder(self.tablaDato, self.guardaDato)
        QWidget.setTabOrder(self.guardaDato, self.descartaDato)
        QWidget.setTabOrder(self.descartaDato, self.eliminaDato)
        QWidget.setTabOrder(self.eliminaDato, self.editaDato)
        QWidget.setTabOrder(self.editaDato, self.anadeDato)
        QWidget.setTabOrder(self.anadeDato, self.tablaDatoTabular)
        QWidget.setTabOrder(self.tablaDatoTabular, self.guardaDatoTabular)
        QWidget.setTabOrder(self.guardaDatoTabular, self.descartaDatoTabular)
        QWidget.setTabOrder(self.descartaDatoTabular, self.eliminaDatoTabular)
        QWidget.setTabOrder(self.eliminaDatoTabular, self.editaDatoTabular)
        QWidget.setTabOrder(self.editaDatoTabular, self.anadeDatoTabular)

        self.retranslateUi(FuenteListClass)
        self.tablaAforo.customContextMenuRequested.connect(FuenteListClass.showContextMenu)
        self.tablaDatoTabular.customContextMenuRequested.connect(FuenteListClass.showContextMenu)
        self.tablaDato.customContextMenuRequested.connect(FuenteListClass.showContextMenu)
        self.tablaParametros.customContextMenuRequested.connect(FuenteListClass.showContextMenu)
        self.tablaFuente.customContextMenuRequested.connect(FuenteListClass.showContextMenu)

        self.tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FuenteListClass)
    # setupUi

    def retranslateUi(self, FuenteListClass):
        FuenteListClass.setWindowTitle(QCoreApplication.translate("FuenteListClass", u"Lista de fuentes", None))
        self.clipboardAforo.setText(QCoreApplication.translate("FuenteListClass", u"Insertar desde portapapeles", None))
        self.clipboardDatoTabular.setText(QCoreApplication.translate("FuenteListClass", u"Insertar dato desde portapapeles", None))
#if QT_CONFIG(tooltip)
        self.clipboardDatoTabular.setToolTip(QCoreApplication.translate("FuenteListClass", u"Insertar dato desde portapapeles", None))
#endif // QT_CONFIG(tooltip)
        self.copyHeaderDatoTabular.setText(QCoreApplication.translate("FuenteListClass", u"Copiar cabecera", None))
#if QT_CONFIG(tooltip)
        self.copyHeaderDatoTabular.setToolTip(QCoreApplication.translate("FuenteListClass", u"Copiar cabecera", None))
#endif // QT_CONFIG(tooltip)
        self.clipboardDato.setText(QCoreApplication.translate("FuenteListClass", u"Inserta dato desde portapapeles", None))
#if QT_CONFIG(tooltip)
        self.clipboardDato.setToolTip(QCoreApplication.translate("FuenteListClass", u"Inserta dato desde portapapeles", None))
#endif // QT_CONFIG(tooltip)
        self.clipboardParametros.setText(QCoreApplication.translate("FuenteListClass", u"Insertar desde el portapaleles...", None))
        self.calcularAforo.setText(QCoreApplication.translate("FuenteListClass", u"Calcular", None))
        self.calcularFuente.setText(QCoreApplication.translate("FuenteListClass", u"Calcular", None))
        self.label.setText(QCoreApplication.translate("FuenteListClass", u"Escenario", None))
        self.deseleccionaFuente.setText(QCoreApplication.translate("FuenteListClass", u"Deseleccionar", None))
        self.eliminaFuente.setText(QCoreApplication.translate("FuenteListClass", u"Eliminar", None))
        self.editaFuente.setText(QCoreApplication.translate("FuenteListClass", u"Editar", None))
        self.anadeFuente.setText(QCoreApplication.translate("FuenteListClass", u"A\u00f1adir", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_5), QCoreApplication.translate("FuenteListClass", u"Fuentes", None))
        self.guardaAforo.setText(QCoreApplication.translate("FuenteListClass", u"Guardar", None))
        self.descartaAforo.setText(QCoreApplication.translate("FuenteListClass", u"Descartar", None))
        self.deseleccionaAforo.setText(QCoreApplication.translate("FuenteListClass", u"Deseleccionar", None))
        self.buscaAforo.setText(QCoreApplication.translate("FuenteListClass", u"Buscar", None))
        self.eliminaAforo.setText(QCoreApplication.translate("FuenteListClass", u"Eliminar", None))
        self.editaAforo.setText(QCoreApplication.translate("FuenteListClass", u"Editar", None))
        self.anadeAforo.setText(QCoreApplication.translate("FuenteListClass", u"A\u00f1adir", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_6), QCoreApplication.translate("FuenteListClass", u"Aforos", None))
        self.guardaParametros.setText(QCoreApplication.translate("FuenteListClass", u"Guardar", None))
        self.descartaParametros.setText(QCoreApplication.translate("FuenteListClass", u"Descartar", None))
        self.anadeParametros.setText(QCoreApplication.translate("FuenteListClass", u"A\u00f1adir", None))
        self.eliminaParametros.setText(QCoreApplication.translate("FuenteListClass", u"Eliminar", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_7), QCoreApplication.translate("FuenteListClass", u"Parametros", None))
        self.guardaDato.setText(QCoreApplication.translate("FuenteListClass", u"Guardar", None))
        self.descartaDato.setText(QCoreApplication.translate("FuenteListClass", u"Descartar", None))
        self.eliminaDato.setText(QCoreApplication.translate("FuenteListClass", u"Eliminar", None))
        self.editaDato.setText(QCoreApplication.translate("FuenteListClass", u"Editar", None))
        self.anadeDato.setText(QCoreApplication.translate("FuenteListClass", u"A\u00f1adir", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_8), QCoreApplication.translate("FuenteListClass", u"Datos", None))
        self.guardaDatoTabular.setText(QCoreApplication.translate("FuenteListClass", u"Guardar", None))
        self.descartaDatoTabular.setText(QCoreApplication.translate("FuenteListClass", u"Descartar", None))
        self.eliminaDatoTabular.setText(QCoreApplication.translate("FuenteListClass", u"Eliminar", None))
        self.editaDatoTabular.setText(QCoreApplication.translate("FuenteListClass", u"Editar", None))
        self.anadeDatoTabular.setText(QCoreApplication.translate("FuenteListClass", u"A\u00f1adir", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_9), QCoreApplication.translate("FuenteListClass", u"Dato tabular", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_2), QCoreApplication.translate("FuenteListClass", u"Contaminantes validados", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_3), QCoreApplication.translate("FuenteListClass", u"Resultados", None))
    # retranslateUi

