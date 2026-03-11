# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plantillalist.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

from ...widgets.datalist import DataList

class Ui_PlantillaListClass(object):
    def setupUi(self, PlantillaListClass):
        if not PlantillaListClass.objectName():
            PlantillaListClass.setObjectName(u"PlantillaListClass")
        PlantillaListClass.resize(482, 458)
        self.verticalLayout = QVBoxLayout(PlantillaListClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.plantilla = QLineEdit(PlantillaListClass)
        self.plantilla.setObjectName(u"plantilla")
        self.plantilla.setEnabled(False)

        self.gridLayout.addWidget(self.plantilla, 0, 2, 1, 1)

        self.label_2 = QLabel(PlantillaListClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.descripcion = QTextEdit(PlantillaListClass)
        self.descripcion.setObjectName(u"descripcion")

        self.gridLayout.addWidget(self.descripcion, 1, 2, 1, 1)

        self.label = QLabel(PlantillaListClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 160, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.nueva = QPushButton(PlantillaListClass)
        self.nueva.setObjectName(u"nueva")

        self.horizontalLayout.addWidget(self.nueva)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(PlantillaListClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.descripcion)
        self.label.setBuddy(self.plantilla)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.plantilla, self.descripcion)
        QWidget.setTabOrder(self.descripcion, self.nueva)

        self.retranslateUi(PlantillaListClass)

        QMetaObject.connectSlotsByName(PlantillaListClass)
    # setupUi

    def retranslateUi(self, PlantillaListClass):
        PlantillaListClass.setWindowTitle(QCoreApplication.translate("PlantillaListClass", u"Plantillas de informes", None))
        self.label_2.setText(QCoreApplication.translate("PlantillaListClass", u"Descripci\u00f3n:", None))
        self.label.setText(QCoreApplication.translate("PlantillaListClass", u"Plantilla Actual:", None))
        self.nueva.setText(QCoreApplication.translate("PlantillaListClass", u"Cargar Nueva", None))
    # retranslateUi

