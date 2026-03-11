# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapaforozonadlg.ui'
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

class Ui_MapAforoZonaDlgClass(object):
    def setupUi(self, MapAforoZonaDlgClass):
        if not MapAforoZonaDlgClass.objectName():
            MapAforoZonaDlgClass.setObjectName(u"MapAforoZonaDlgClass")
        MapAforoZonaDlgClass.resize(458, 392)
        self.verticalLayout = QVBoxLayout(MapAforoZonaDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(MapAforoZonaDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.aforo = TComboBox(MapAforoZonaDlgClass)
        self.aforo.setObjectName(u"aforo")

        self.gridLayout.addWidget(self.aforo, 0, 1, 1, 1)

        self.label_2 = QLabel(MapAforoZonaDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.zona = TComboBox(MapAforoZonaDlgClass)
        self.zona.setObjectName(u"zona")

        self.gridLayout.addWidget(self.zona, 1, 1, 1, 1)

        self.label_4 = QLabel(MapAforoZonaDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.p = QLineEdit(MapAforoZonaDlgClass)
        self.p.setObjectName(u"p")

        self.gridLayout.addWidget(self.p, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(206, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(MapAforoZonaDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.aforo)
        self.label_2.setBuddy(self.zona)
        self.label_4.setBuddy(self.p)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.aforo, self.zona)
        QWidget.setTabOrder(self.zona, self.p)
        QWidget.setTabOrder(self.p, self.buttonBox)

        self.retranslateUi(MapAforoZonaDlgClass)
        self.buttonBox.accepted.connect(MapAforoZonaDlgClass.accept)
        self.buttonBox.rejected.connect(MapAforoZonaDlgClass.reject)

        QMetaObject.connectSlotsByName(MapAforoZonaDlgClass)
    # setupUi

    def retranslateUi(self, MapAforoZonaDlgClass):
        MapAforoZonaDlgClass.setWindowTitle(QCoreApplication.translate("MapAforoZonaDlgClass", u"Contribuci\u00f3n de contaminantes en un aforo", None))
        self.label_3.setText(QCoreApplication.translate("MapAforoZonaDlgClass", u"Aforo", None))
        self.label_2.setText(QCoreApplication.translate("MapAforoZonaDlgClass", u"Zona", None))
        self.label_4.setText(QCoreApplication.translate("MapAforoZonaDlgClass", u"Valor", None))
    # retranslateUi

