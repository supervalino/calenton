# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'motorcalculodlg.ui'
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
from PyQt6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QFormLayout,
    QLabel, QLineEdit, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

from ts import DataDialog

class Ui_MotorcalculoDialogClass(object):
    def setupUi(self, MotorcalculoDialogClass):
        if not MotorcalculoDialogClass.objectName():
            MotorcalculoDialogClass.setObjectName(u"MotorcalculoDialogClass")
        MotorcalculoDialogClass.resize(475, 355)
        self.verticalLayout = QVBoxLayout(MotorcalculoDialogClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_7 = QLabel(MotorcalculoDialogClass)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.codigo = QLineEdit(MotorcalculoDialogClass)
        self.codigo.setObjectName(u"codigo")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.codigo)

        self.label_8 = QLabel(MotorcalculoDialogClass)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.nombre = QLineEdit(MotorcalculoDialogClass)
        self.nombre.setObjectName(u"nombre")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nombre)

        self.label_10 = QLabel(MotorcalculoDialogClass)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.clase = QLineEdit(MotorcalculoDialogClass)
        self.clase.setObjectName(u"clase")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.clase)

        self.label_9 = QLabel(MotorcalculoDialogClass)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.descripcion = QTextEdit(MotorcalculoDialogClass)
        self.descripcion.setObjectName(u"descripcion")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.descripcion)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(MotorcalculoDialogClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_7.setBuddy(self.codigo)
        self.label_8.setBuddy(self.nombre)
        self.label_10.setBuddy(self.clase)
        self.label_9.setBuddy(self.descripcion)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.codigo, self.nombre)
        QWidget.setTabOrder(self.nombre, self.clase)
        QWidget.setTabOrder(self.clase, self.descripcion)
        QWidget.setTabOrder(self.descripcion, self.buttonBox)

        self.retranslateUi(MotorcalculoDialogClass)
        self.buttonBox.accepted.connect(MotorcalculoDialogClass.accept)
        self.buttonBox.rejected.connect(MotorcalculoDialogClass.reject)

        QMetaObject.connectSlotsByName(MotorcalculoDialogClass)
    # setupUi

    def retranslateUi(self, MotorcalculoDialogClass):
        MotorcalculoDialogClass.setWindowTitle(QCoreApplication.translate("MotorcalculoDialogClass", u"Datos de motor de c\u00e1lculo", None))
        self.label_7.setText(QCoreApplication.translate("MotorcalculoDialogClass", u"Codigo", None))
        self.label_8.setText(QCoreApplication.translate("MotorcalculoDialogClass", u"Nombre", None))
        self.label_10.setText(QCoreApplication.translate("MotorcalculoDialogClass", u"Clase", None))
        self.label_9.setText(QCoreApplication.translate("MotorcalculoDialogClass", u"Descripci\u00f3n", None))
    # retranslateUi

