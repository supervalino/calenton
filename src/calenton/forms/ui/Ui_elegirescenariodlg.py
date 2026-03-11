# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elegirescenariodlg.ui'
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
from PyQt6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from ts import TComboBox

class Ui_ElegirEscenarioDlgClass(object):
    def setupUi(self, ElegirEscenarioDlgClass):
        if not ElegirEscenarioDlgClass.objectName():
            ElegirEscenarioDlgClass.setObjectName(u"ElegirEscenarioDlgClass")
        ElegirEscenarioDlgClass.resize(273, 90)
        self.verticalLayout = QVBoxLayout(ElegirEscenarioDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(ElegirEscenarioDlgClass)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.escenario = TComboBox(ElegirEscenarioDlgClass)
        self.escenario.setObjectName(u"escenario")

        self.horizontalLayout.addWidget(self.escenario)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ElegirEscenarioDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.escenario)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.escenario, self.buttonBox)

        self.retranslateUi(ElegirEscenarioDlgClass)
        self.buttonBox.accepted.connect(ElegirEscenarioDlgClass.accept)
        self.buttonBox.rejected.connect(ElegirEscenarioDlgClass.reject)

        QMetaObject.connectSlotsByName(ElegirEscenarioDlgClass)
    # setupUi

    def retranslateUi(self, ElegirEscenarioDlgClass):
        ElegirEscenarioDlgClass.setWindowTitle(QCoreApplication.translate("ElegirEscenarioDlgClass", u"Elija un escenario", None))
        self.label.setText(QCoreApplication.translate("ElegirEscenarioDlgClass", u"Escenario", None))
    # retranslateUi

