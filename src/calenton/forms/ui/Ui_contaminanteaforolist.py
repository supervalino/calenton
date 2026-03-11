# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contaminanteaforolist.ui'
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

class Ui_ContaminanteAforoListClass(object):
    def setupUi(self, ContaminanteAforoListClass):
        if not ContaminanteAforoListClass.objectName():
            ContaminanteAforoListClass.setObjectName(u"ContaminanteAforoListClass")
        ContaminanteAforoListClass.resize(677, 558)
        self.clipboardContaminanteAforo = QAction(ContaminanteAforoListClass)
        self.clipboardContaminanteAforo.setObjectName(u"clipboardContaminanteAforo")
        self.gridLayout = QGridLayout(ContaminanteAforoListClass)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabla = QTableView(ContaminanteAforoListClass)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabla.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tabla, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.guardar = QPushButton(ContaminanteAforoListClass)
        self.guardar.setObjectName(u"guardar")

        self.horizontalLayout.addWidget(self.guardar)

        self.descartar = QPushButton(ContaminanteAforoListClass)
        self.descartar.setObjectName(u"descartar")

        self.horizontalLayout.addWidget(self.descartar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.elimina = QPushButton(ContaminanteAforoListClass)
        self.elimina.setObjectName(u"elimina")

        self.horizontalLayout.addWidget(self.elimina)

        self.edita = QPushButton(ContaminanteAforoListClass)
        self.edita.setObjectName(u"edita")

        self.horizontalLayout.addWidget(self.edita)

        self.anade = QPushButton(ContaminanteAforoListClass)
        self.anade.setObjectName(u"anade")

        self.horizontalLayout.addWidget(self.anade)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        QWidget.setTabOrder(self.tabla, self.elimina)
        QWidget.setTabOrder(self.elimina, self.edita)
        QWidget.setTabOrder(self.edita, self.anade)

        self.retranslateUi(ContaminanteAforoListClass)
        self.tabla.customContextMenuRequested.connect(ContaminanteAforoListClass.showContextMenu)

        QMetaObject.connectSlotsByName(ContaminanteAforoListClass)
    # setupUi

    def retranslateUi(self, ContaminanteAforoListClass):
        ContaminanteAforoListClass.setWindowTitle(QCoreApplication.translate("ContaminanteAforoListClass", u"Contribuci\u00f3n de contaminantes en cada aforo", None))
        self.clipboardContaminanteAforo.setText(QCoreApplication.translate("ContaminanteAforoListClass", u"Inserta desde portapapeles", None))
#if QT_CONFIG(tooltip)
        self.clipboardContaminanteAforo.setToolTip(QCoreApplication.translate("ContaminanteAforoListClass", u"Inserta desde portapapeles", None))
#endif // QT_CONFIG(tooltip)
        self.guardar.setText(QCoreApplication.translate("ContaminanteAforoListClass", u"Guardar", None))
        self.descartar.setText(QCoreApplication.translate("ContaminanteAforoListClass", u"Descartar", None))
        self.elimina.setText(QCoreApplication.translate("ContaminanteAforoListClass", u"Eliminar", None))
        self.edita.setText(QCoreApplication.translate("ContaminanteAforoListClass", u"Editar", None))
        self.anade.setText(QCoreApplication.translate("ContaminanteAforoListClass", u"A\u00f1adir", None))
    # retranslateUi

