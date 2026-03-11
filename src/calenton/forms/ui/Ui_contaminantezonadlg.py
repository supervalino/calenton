# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contaminantezonadlg.ui'
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
    QVBoxLayout, QWidget)

from ts import (DataDialog, TComboBox)

class Ui_ContaminanteZonaDlgClass(object):
    def setupUi(self, ContaminanteZonaDlgClass):
        if not ContaminanteZonaDlgClass.objectName():
            ContaminanteZonaDlgClass.setObjectName(u"ContaminanteZonaDlgClass")
        ContaminanteZonaDlgClass.resize(728, 396)
        self.verticalLayout = QVBoxLayout(ContaminanteZonaDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(ContaminanteZonaDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.contaminante = TComboBox(ContaminanteZonaDlgClass)
        self.contaminante.setObjectName(u"contaminante")

        self.gridLayout.addWidget(self.contaminante, 0, 1, 1, 1)

        self.label_2 = QLabel(ContaminanteZonaDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.fuente = TComboBox(ContaminanteZonaDlgClass)
        self.fuente.setObjectName(u"fuente")

        self.gridLayout.addWidget(self.fuente, 1, 1, 1, 1)

        self.label = QLabel(ContaminanteZonaDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.clasificacion = TComboBox(ContaminanteZonaDlgClass)
        self.clasificacion.setObjectName(u"clasificacion")

        self.gridLayout.addWidget(self.clasificacion, 2, 1, 1, 1)

        self.label_4 = QLabel(ContaminanteZonaDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.valor = QLineEdit(ContaminanteZonaDlgClass)
        self.valor.setObjectName(u"valor")

        self.gridLayout.addWidget(self.valor, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(206, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ContaminanteZonaDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.contaminante)
        self.label_2.setBuddy(self.fuente)
        self.label_4.setBuddy(self.valor)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.contaminante, self.fuente)
        QWidget.setTabOrder(self.fuente, self.valor)
        QWidget.setTabOrder(self.valor, self.buttonBox)

        self.retranslateUi(ContaminanteZonaDlgClass)
        self.buttonBox.accepted.connect(ContaminanteZonaDlgClass.accept)
        self.buttonBox.rejected.connect(ContaminanteZonaDlgClass.reject)

        QMetaObject.connectSlotsByName(ContaminanteZonaDlgClass)
    # setupUi

    def retranslateUi(self, ContaminanteZonaDlgClass):
        ContaminanteZonaDlgClass.setWindowTitle(QCoreApplication.translate("ContaminanteZonaDlgClass", u"Emisi\u00f3n de contaminantes por fuente ", None))
        self.label_3.setText(QCoreApplication.translate("ContaminanteZonaDlgClass", u"Contaminante", None))
        self.label_2.setText(QCoreApplication.translate("ContaminanteZonaDlgClass", u"Fuente", None))
        self.label.setText(QCoreApplication.translate("ContaminanteZonaDlgClass", u"Clasificaci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("ContaminanteZonaDlgClass", u"Valor", None))
    # retranslateUi

