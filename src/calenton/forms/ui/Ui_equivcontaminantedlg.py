# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equivcontaminantedlg.ui'
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

class Ui_EquivContaminanteDlgClass(object):
    def setupUi(self, EquivContaminanteDlgClass):
        if not EquivContaminanteDlgClass.objectName():
            EquivContaminanteDlgClass.setObjectName(u"EquivContaminanteDlgClass")
        EquivContaminanteDlgClass.resize(448, 329)
        self.verticalLayout = QVBoxLayout(EquivContaminanteDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(EquivContaminanteDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.escenario = TComboBox(EquivContaminanteDlgClass)
        self.escenario.setObjectName(u"escenario")

        self.gridLayout.addWidget(self.escenario, 0, 2, 1, 1)

        self.label = QLabel(EquivContaminanteDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.contaminante = TComboBox(EquivContaminanteDlgClass)
        self.contaminante.setObjectName(u"contaminante")

        self.gridLayout.addWidget(self.contaminante, 1, 2, 1, 1)

        self.label_4 = QLabel(EquivContaminanteDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)

        self.p = QLineEdit(EquivContaminanteDlgClass)
        self.p.setObjectName(u"p")

        self.gridLayout.addWidget(self.p, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(206, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(EquivContaminanteDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.escenario)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(EquivContaminanteDlgClass)
        self.buttonBox.accepted.connect(EquivContaminanteDlgClass.accept)
        self.buttonBox.rejected.connect(EquivContaminanteDlgClass.reject)

        QMetaObject.connectSlotsByName(EquivContaminanteDlgClass)
    # setupUi

    def retranslateUi(self, EquivContaminanteDlgClass):
        EquivContaminanteDlgClass.setWindowTitle(QCoreApplication.translate("EquivContaminanteDlgClass", u"Datos de equivalente de CO2", None))
        self.label_2.setText(QCoreApplication.translate("EquivContaminanteDlgClass", u"Escenario", None))
        self.label.setText(QCoreApplication.translate("EquivContaminanteDlgClass", u"Contaminante", None))
        self.label_4.setText(QCoreApplication.translate("EquivContaminanteDlgClass", u"Valor", None))
    # retranslateUi

