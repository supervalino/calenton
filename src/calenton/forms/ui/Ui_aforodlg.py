# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aforodlg.ui'
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
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

from ts import (DataDialog, TComboBox)

class Ui_AforoDlgClass(object):
    def setupUi(self, AforoDlgClass):
        if not AforoDlgClass.objectName():
            AforoDlgClass.setObjectName(u"AforoDlgClass")
        AforoDlgClass.resize(437, 335)
        self.verticalLayout = QVBoxLayout(AforoDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(AforoDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.nombre = QLineEdit(AforoDlgClass)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)

        self.label_2 = QLabel(AforoDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.fuente = TComboBox(AforoDlgClass)
        self.fuente.setObjectName(u"fuente")

        self.gridLayout.addWidget(self.fuente, 1, 1, 1, 1)

        self.label_4 = QLabel(AforoDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.escala = QLineEdit(AforoDlgClass)
        self.escala.setObjectName(u"escala")

        self.gridLayout.addWidget(self.escala, 2, 1, 1, 1)

        self.label_5 = QLabel(AforoDlgClass)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.nivelZona = TComboBox(AforoDlgClass)
        self.nivelZona.setObjectName(u"nivelZona")

        self.gridLayout.addWidget(self.nivelZona, 3, 1, 1, 1)

        self.label_6 = QLabel(AforoDlgClass)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.zona = TComboBox(AforoDlgClass)
        self.zona.setObjectName(u"zona")

        self.gridLayout.addWidget(self.zona, 4, 1, 1, 1)

        self.label_7 = QLabel(AforoDlgClass)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.tipoDatoZona = TComboBox(AforoDlgClass)
        self.tipoDatoZona.setObjectName(u"tipoDatoZona")

        self.gridLayout.addWidget(self.tipoDatoZona, 5, 1, 1, 1)

        self.label = QLabel(AforoDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)

        self.descripcion = QTextEdit(AforoDlgClass)
        self.descripcion.setObjectName(u"descripcion")

        self.gridLayout.addWidget(self.descripcion, 6, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(206, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(AforoDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.fuente)
        self.label_4.setBuddy(self.escala)
        self.label_5.setBuddy(self.nivelZona)
        self.label_6.setBuddy(self.zona)
        self.label_7.setBuddy(self.tipoDatoZona)
        self.label.setBuddy(self.descripcion)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nombre, self.fuente)
        QWidget.setTabOrder(self.fuente, self.escala)
        QWidget.setTabOrder(self.escala, self.nivelZona)
        QWidget.setTabOrder(self.nivelZona, self.zona)
        QWidget.setTabOrder(self.zona, self.tipoDatoZona)
        QWidget.setTabOrder(self.tipoDatoZona, self.descripcion)
        QWidget.setTabOrder(self.descripcion, self.buttonBox)

        self.retranslateUi(AforoDlgClass)
        self.buttonBox.accepted.connect(AforoDlgClass.accept)
        self.buttonBox.rejected.connect(AforoDlgClass.reject)

        QMetaObject.connectSlotsByName(AforoDlgClass)
    # setupUi

    def retranslateUi(self, AforoDlgClass):
        AforoDlgClass.setWindowTitle(QCoreApplication.translate("AforoDlgClass", u"Datos de aforo", None))
        self.label_3.setText(QCoreApplication.translate("AforoDlgClass", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("AforoDlgClass", u"Fuente", None))
        self.label_4.setText(QCoreApplication.translate("AforoDlgClass", u"Escala", None))
        self.label_5.setText(QCoreApplication.translate("AforoDlgClass", u"Nivel de zona", None))
        self.label_6.setText(QCoreApplication.translate("AforoDlgClass", u"Zona", None))
        self.label_7.setText(QCoreApplication.translate("AforoDlgClass", u"Criterio de distribuci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("AforoDlgClass", u"Descripci\u00f3n", None))
    # retranslateUi

