# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contaminantedlg.ui'
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
    QLabel, QLineEdit, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

from ts import DataDialog

class Ui_ContaminanteDlgClass(object):
    def setupUi(self, ContaminanteDlgClass):
        if not ContaminanteDlgClass.objectName():
            ContaminanteDlgClass.setObjectName(u"ContaminanteDlgClass")
        ContaminanteDlgClass.resize(464, 420)
        self.verticalLayout = QVBoxLayout(ContaminanteDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(ContaminanteDlgClass)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.nombre = QLineEdit(ContaminanteDlgClass)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)

        self.label = QLabel(ContaminanteDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.unidades = QLineEdit(ContaminanteDlgClass)
        self.unidades.setObjectName(u"unidades")

        self.gridLayout.addWidget(self.unidades, 1, 1, 1, 1)

        self.label_9 = QLabel(ContaminanteDlgClass)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.descripcion = QTextEdit(ContaminanteDlgClass)
        self.descripcion.setObjectName(u"descripcion")

        self.gridLayout.addWidget(self.descripcion, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(ContaminanteDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_8.setBuddy(self.nombre)
        self.label_9.setBuddy(self.descripcion)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nombre, self.descripcion)
        QWidget.setTabOrder(self.descripcion, self.buttonBox)

        self.retranslateUi(ContaminanteDlgClass)
        self.buttonBox.accepted.connect(ContaminanteDlgClass.accept)
        self.buttonBox.rejected.connect(ContaminanteDlgClass.reject)

        QMetaObject.connectSlotsByName(ContaminanteDlgClass)
    # setupUi

    def retranslateUi(self, ContaminanteDlgClass):
        ContaminanteDlgClass.setWindowTitle(QCoreApplication.translate("ContaminanteDlgClass", u"Contaminante", None))
        self.label_8.setText(QCoreApplication.translate("ContaminanteDlgClass", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("ContaminanteDlgClass", u"Unidades", None))
        self.label_9.setText(QCoreApplication.translate("ContaminanteDlgClass", u"Descripci\u00f3n", None))
    # retranslateUi

