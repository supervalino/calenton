# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fuentedlg.ui'
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
from PyQt6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialogButtonBox,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

from ts import (DataDialog, TComboBox)

class Ui_FuenteDlgClass(object):
    def setupUi(self, FuenteDlgClass):
        if not FuenteDlgClass.objectName():
            FuenteDlgClass.setObjectName(u"FuenteDlgClass")
        FuenteDlgClass.resize(528, 399)
        self.verticalLayout_2 = QVBoxLayout(FuenteDlgClass)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(FuenteDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.nombre = QLineEdit(FuenteDlgClass)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)

        self.label_2 = QLabel(FuenteDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.escenario = TComboBox(FuenteDlgClass)
        self.escenario.setObjectName(u"escenario")

        self.gridLayout.addWidget(self.escenario, 1, 1, 1, 1)

        self.label = QLabel(FuenteDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.origen = TComboBox(FuenteDlgClass)
        self.origen.setObjectName(u"origen")

        self.gridLayout.addWidget(self.origen, 2, 1, 1, 1)

        self.label_4 = QLabel(FuenteDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.motorcalculo = TComboBox(FuenteDlgClass)
        self.motorcalculo.setObjectName(u"motorcalculo")

        self.gridLayout.addWidget(self.motorcalculo, 3, 1, 1, 1)

        self.label_5 = QLabel(FuenteDlgClass)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.nivelZona = TComboBox(FuenteDlgClass)
        self.nivelZona.setObjectName(u"nivelZona")

        self.gridLayout.addWidget(self.nivelZona, 4, 1, 1, 1)

        self.label_6 = QLabel(FuenteDlgClass)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.tipoDatoZona = TComboBox(FuenteDlgClass)
        self.tipoDatoZona.setObjectName(u"tipoDatoZona")

        self.gridLayout.addWidget(self.tipoDatoZona, 5, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.groupBox = QGroupBox(FuenteDlgClass)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.borraclasificacion = QPushButton(self.groupBox)
        self.borraclasificacion.setObjectName(u"borraclasificacion")

        self.gridLayout_2.addWidget(self.borraclasificacion, 2, 1, 1, 1)

        self.clasificacion = TComboBox(self.groupBox)
        self.clasificacion.setObjectName(u"clasificacion")

        self.gridLayout_2.addWidget(self.clasificacion, 3, 0, 1, 1)

        self.asignaclasificacion = QPushButton(self.groupBox)
        self.asignaclasificacion.setObjectName(u"asignaclasificacion")
        self.asignaclasificacion.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asignaclasificacion.sizePolicy().hasHeightForWidth())
        self.asignaclasificacion.setSizePolicy(sizePolicy)
        self.asignaclasificacion.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.asignaclasificacion, 3, 1, 1, 1)

        self.listaclasificacion = QTableView(self.groupBox)
        self.listaclasificacion.setObjectName(u"listaclasificacion")
        self.listaclasificacion.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listaclasificacion.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.gridLayout_2.addWidget(self.listaclasificacion, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(206, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(FuenteDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.escenario)
        self.label.setBuddy(self.origen)
        self.label_4.setBuddy(self.motorcalculo)
        self.label_5.setBuddy(self.nivelZona)
        self.label_6.setBuddy(self.tipoDatoZona)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nombre, self.escenario)
        QWidget.setTabOrder(self.escenario, self.origen)
        QWidget.setTabOrder(self.origen, self.motorcalculo)
        QWidget.setTabOrder(self.motorcalculo, self.nivelZona)
        QWidget.setTabOrder(self.nivelZona, self.tipoDatoZona)
        QWidget.setTabOrder(self.tipoDatoZona, self.listaclasificacion)
        QWidget.setTabOrder(self.listaclasificacion, self.borraclasificacion)
        QWidget.setTabOrder(self.borraclasificacion, self.clasificacion)
        QWidget.setTabOrder(self.clasificacion, self.asignaclasificacion)
        QWidget.setTabOrder(self.asignaclasificacion, self.buttonBox)

        self.retranslateUi(FuenteDlgClass)
        self.buttonBox.accepted.connect(FuenteDlgClass.accept)
        self.buttonBox.rejected.connect(FuenteDlgClass.reject)

        QMetaObject.connectSlotsByName(FuenteDlgClass)
    # setupUi

    def retranslateUi(self, FuenteDlgClass):
        FuenteDlgClass.setWindowTitle(QCoreApplication.translate("FuenteDlgClass", u"Datos de fuente", None))
        self.label_3.setText(QCoreApplication.translate("FuenteDlgClass", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("FuenteDlgClass", u"Escenario", None))
        self.label.setText(QCoreApplication.translate("FuenteDlgClass", u"Origen", None))
        self.label_4.setText(QCoreApplication.translate("FuenteDlgClass", u"Motor de C\u00e1lculo", None))
        self.label_5.setText(QCoreApplication.translate("FuenteDlgClass", u"Nivel de zona", None))
        self.label_6.setText(QCoreApplication.translate("FuenteDlgClass", u"Dato Distribuci\u00f3n", None))
        self.groupBox.setTitle(QCoreApplication.translate("FuenteDlgClass", u"Se clasifica por:", None))
        self.borraclasificacion.setText(QCoreApplication.translate("FuenteDlgClass", u"Eliminar", None))
        self.asignaclasificacion.setText(QCoreApplication.translate("FuenteDlgClass", u"A\u00f1adir", None))
    # retranslateUi

