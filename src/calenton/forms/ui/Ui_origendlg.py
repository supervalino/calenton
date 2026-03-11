# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'origendlg.ui'
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

class Ui_OrigenDlgClass(object):
    def setupUi(self, OrigenDlgClass):
        if not OrigenDlgClass.objectName():
            OrigenDlgClass.setObjectName(u"OrigenDlgClass")
        OrigenDlgClass.resize(306, 313)
        self.verticalLayout = QVBoxLayout(OrigenDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(OrigenDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.nombre = QLineEdit(OrigenDlgClass)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 2)

        self.label_2 = QLabel(OrigenDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.escenario = TComboBox(OrigenDlgClass)
        self.escenario.setObjectName(u"escenario")

        self.gridLayout.addWidget(self.escenario, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(206, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(OrigenDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.escenario)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nombre, self.escenario)

        self.retranslateUi(OrigenDlgClass)
        self.buttonBox.accepted.connect(OrigenDlgClass.accept)
        self.buttonBox.rejected.connect(OrigenDlgClass.reject)

        QMetaObject.connectSlotsByName(OrigenDlgClass)
    # setupUi

    def retranslateUi(self, OrigenDlgClass):
        OrigenDlgClass.setWindowTitle(QCoreApplication.translate("OrigenDlgClass", u"Datos de origen", None))
        self.label_3.setText(QCoreApplication.translate("OrigenDlgClass", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("OrigenDlgClass", u"Escenario", None))
    # retranslateUi

