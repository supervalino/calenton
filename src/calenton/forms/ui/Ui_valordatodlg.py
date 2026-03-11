# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'valordatodlg.ui'
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

class Ui_ValorDatoDlgClass(object):
    def setupUi(self, ValorDatoDlgClass):
        if not ValorDatoDlgClass.objectName():
            ValorDatoDlgClass.setObjectName(u"ValorDatoDlgClass")
        ValorDatoDlgClass.resize(458, 392)
        self.verticalLayout = QVBoxLayout(ValorDatoDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(ValorDatoDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.aforo = TComboBox(ValorDatoDlgClass)
        self.aforo.setObjectName(u"aforo")

        self.gridLayout.addWidget(self.aforo, 0, 1, 1, 1)

        self.label = QLabel(ValorDatoDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.clasificacion = TComboBox(ValorDatoDlgClass)
        self.clasificacion.setObjectName(u"clasificacion")

        self.gridLayout.addWidget(self.clasificacion, 1, 1, 1, 1)

        self.label_2 = QLabel(ValorDatoDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.dato = TComboBox(ValorDatoDlgClass)
        self.dato.setObjectName(u"dato")

        self.gridLayout.addWidget(self.dato, 2, 1, 1, 1)

        self.label_4 = QLabel(ValorDatoDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.valor = QLineEdit(ValorDatoDlgClass)
        self.valor.setObjectName(u"valor")

        self.gridLayout.addWidget(self.valor, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(206, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ValorDatoDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.dato)
        self.label_4.setBuddy(self.valor)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.dato, self.valor)
        QWidget.setTabOrder(self.valor, self.buttonBox)

        self.retranslateUi(ValorDatoDlgClass)
        self.buttonBox.accepted.connect(ValorDatoDlgClass.accept)
        self.buttonBox.rejected.connect(ValorDatoDlgClass.reject)

        QMetaObject.connectSlotsByName(ValorDatoDlgClass)
    # setupUi

    def retranslateUi(self, ValorDatoDlgClass):
        ValorDatoDlgClass.setWindowTitle(QCoreApplication.translate("ValorDatoDlgClass", u"Valor en aforo", None))
        self.label_3.setText(QCoreApplication.translate("ValorDatoDlgClass", u"Aforo", None))
        self.label.setText(QCoreApplication.translate("ValorDatoDlgClass", u"Clasificaci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("ValorDatoDlgClass", u"Dato", None))
        self.label_4.setText(QCoreApplication.translate("ValorDatoDlgClass", u"Valor", None))
    # retranslateUi

