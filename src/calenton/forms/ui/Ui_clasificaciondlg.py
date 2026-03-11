# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clasificaciondlg.ui'
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
from PyQt6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

from ts import DataDialog

class Ui_ClasificacionDialogClass(object):
    def setupUi(self, ClasificacionDialogClass):
        if not ClasificacionDialogClass.objectName():
            ClasificacionDialogClass.setObjectName(u"ClasificacionDialogClass")
        ClasificacionDialogClass.resize(524, 450)
        self.verticalLayout = QVBoxLayout(ClasificacionDialogClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(ClasificacionDialogClass)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(ClasificacionDialogClass)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(ClasificacionDialogClass)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(ClasificacionDialogClass)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(ClasificacionDialogClass)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(ClasificacionDialogClass)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(ClasificacionDialogClass)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(ClasificacionDialogClass)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(ClasificacionDialogClass)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.textEdit = QTextEdit(ClasificacionDialogClass)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_5.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line = QFrame(ClasificacionDialogClass)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer = QSpacerItem(20, 54, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ClasificacionDialogClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ClasificacionDialogClass)
        self.buttonBox.accepted.connect(ClasificacionDialogClass.accept)
        self.buttonBox.rejected.connect(ClasificacionDialogClass.reject)

        QMetaObject.connectSlotsByName(ClasificacionDialogClass)
    # setupUi

    def retranslateUi(self, ClasificacionDialogClass):
        ClasificacionDialogClass.setWindowTitle(QCoreApplication.translate("ClasificacionDialogClass", u"Datos de clasificaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("ClasificacionDialogClass", u"Id", None))
        self.label_2.setText(QCoreApplication.translate("ClasificacionDialogClass", u"Idtipoclas", None))
        self.label_3.setText(QCoreApplication.translate("ClasificacionDialogClass", u"Idpadre", None))
        self.label_4.setText(QCoreApplication.translate("ClasificacionDialogClass", u"C\u00f3digo", None))
        self.label_5.setText(QCoreApplication.translate("ClasificacionDialogClass", u"Descripci\u00f3n", None))
    # retranslateUi

