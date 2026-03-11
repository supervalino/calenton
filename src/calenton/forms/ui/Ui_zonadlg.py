# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zonadlg.ui'
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
from PyQt6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from ts import (DataDialog, TComboBox)

class Ui_ZonaDialogClass(object):
    def setupUi(self, ZonaDialogClass):
        if not ZonaDialogClass.objectName():
            ZonaDialogClass.setObjectName(u"ZonaDialogClass")
        ZonaDialogClass.resize(539, 333)
        self.verticalLayout_2 = QVBoxLayout(ZonaDialogClass)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(ZonaDialogClass)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.nombre = QLineEdit(ZonaDialogClass)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout_2.addWidget(self.nombre, 0, 1, 1, 1)

        self.label_2 = QLabel(ZonaDialogClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.nivel = TComboBox(ZonaDialogClass)
        self.nivel.setObjectName(u"nivel")
        self.nivel.setEditable(False)

        self.gridLayout_2.addWidget(self.nivel, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.groupBox = QGroupBox(ZonaDialogClass)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.borrapadre = QPushButton(self.groupBox)
        self.borrapadre.setObjectName(u"borrapadre")

        self.gridLayout.addWidget(self.borrapadre, 2, 1, 1, 1)

        self.listapadres = QListView(self.groupBox)
        self.listapadres.setObjectName(u"listapadres")

        self.gridLayout.addWidget(self.listapadres, 2, 0, 1, 1)

        self.zonapadre = TComboBox(self.groupBox)
        self.zonapadre.setObjectName(u"zonapadre")

        self.gridLayout.addWidget(self.zonapadre, 3, 0, 1, 1)

        self.asignapadre = QPushButton(self.groupBox)
        self.asignapadre.setObjectName(u"asignapadre")
        self.asignapadre.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asignapadre.sizePolicy().hasHeightForWidth())
        self.asignapadre.setSizePolicy(sizePolicy)
        self.asignapadre.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.asignapadre, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 125, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ZonaDialogClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.nombre)
        self.label_2.setBuddy(self.nivel)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nombre, self.nivel)
        QWidget.setTabOrder(self.nivel, self.asignapadre)
        QWidget.setTabOrder(self.asignapadre, self.listapadres)
        QWidget.setTabOrder(self.listapadres, self.buttonBox)

        self.retranslateUi(ZonaDialogClass)
        self.buttonBox.accepted.connect(ZonaDialogClass.accept)
        self.buttonBox.rejected.connect(ZonaDialogClass.reject)

        QMetaObject.connectSlotsByName(ZonaDialogClass)
    # setupUi

    def retranslateUi(self, ZonaDialogClass):
        ZonaDialogClass.setWindowTitle(QCoreApplication.translate("ZonaDialogClass", u"Datos de zonas", None))
        self.label.setText(QCoreApplication.translate("ZonaDialogClass", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("ZonaDialogClass", u"Nivel", None))
        self.groupBox.setTitle(QCoreApplication.translate("ZonaDialogClass", u"Pertenece a", None))
        self.borrapadre.setText(QCoreApplication.translate("ZonaDialogClass", u"Eliminar", None))
        self.asignapadre.setText(QCoreApplication.translate("ZonaDialogClass", u"A\u00f1adir", None))
    # retranslateUi

