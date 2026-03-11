# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'escenariodlg.ui'
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
from PyQt6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from ts import DataDialog

class Ui_EscenarioDlgClass(object):
    def setupUi(self, EscenarioDlgClass):
        if not EscenarioDlgClass.objectName():
            EscenarioDlgClass.setObjectName(u"EscenarioDlgClass")
        EscenarioDlgClass.resize(331, 85)
        self.verticalLayout = QVBoxLayout(EscenarioDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(EscenarioDlgClass)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.nombre = QLineEdit(EscenarioDlgClass)
        self.nombre.setObjectName(u"nombre")

        self.horizontalLayout.addWidget(self.nombre)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(EscenarioDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.nombre)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nombre, self.buttonBox)

        self.retranslateUi(EscenarioDlgClass)
        self.buttonBox.accepted.connect(EscenarioDlgClass.accept)
        self.buttonBox.rejected.connect(EscenarioDlgClass.reject)

        QMetaObject.connectSlotsByName(EscenarioDlgClass)
    # setupUi

    def retranslateUi(self, EscenarioDlgClass):
        EscenarioDlgClass.setWindowTitle(QCoreApplication.translate("EscenarioDlgClass", u"Datos de escenario", None))
        self.label.setText(QCoreApplication.translate("EscenarioDlgClass", u"Nombre", None))
    # retranslateUi

