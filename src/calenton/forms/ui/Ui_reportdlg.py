# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reportdlg.ui'
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
    QTextEdit, QVBoxLayout, QWidget)

from ts import DataDialog

class Ui_ReportDlgClass(object):
    def setupUi(self, ReportDlgClass):
        if not ReportDlgClass.objectName():
            ReportDlgClass.setObjectName(u"ReportDlgClass")
        ReportDlgClass.resize(458, 392)
        self.verticalLayout = QVBoxLayout(ReportDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(ReportDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.nombre = QLineEdit(ReportDlgClass)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)

        self.label = QLabel(ReportDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.descripcion = QTextEdit(ReportDlgClass)
        self.descripcion.setObjectName(u"descripcion")

        self.gridLayout.addWidget(self.descripcion, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(206, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ReportDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.nombre)
        self.label.setBuddy(self.descripcion)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nombre, self.descripcion)
        QWidget.setTabOrder(self.descripcion, self.buttonBox)

        self.retranslateUi(ReportDlgClass)
        self.buttonBox.accepted.connect(ReportDlgClass.accept)
        self.buttonBox.rejected.connect(ReportDlgClass.reject)

        QMetaObject.connectSlotsByName(ReportDlgClass)
    # setupUi

    def retranslateUi(self, ReportDlgClass):
        ReportDlgClass.setWindowTitle(QCoreApplication.translate("ReportDlgClass", u"Datos de Informe", None))
        self.label_3.setText(QCoreApplication.translate("ReportDlgClass", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("ReportDlgClass", u"Descripci\u00f3n", None))
    # retranslateUi

