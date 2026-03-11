# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buscardlg.ui'
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
from PyQt6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_BuscarDlg(object):
    def setupUi(self, BuscarDlg):
        if not BuscarDlg.objectName():
            BuscarDlg.setObjectName(u"BuscarDlg")
        BuscarDlg.resize(452, 215)
        self.verticalLayout_2 = QVBoxLayout(BuscarDlg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(BuscarDlg)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.campos = QComboBox(BuscarDlg)
        self.campos.setObjectName(u"campos")

        self.gridLayout.addWidget(self.campos, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.texto = QLineEdit(BuscarDlg)
        self.texto.setObjectName(u"texto")

        self.verticalLayout.addWidget(self.texto)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 84, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(BuscarDlg)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(BuscarDlg)
        self.buttonBox.accepted.connect(BuscarDlg.accept)
        self.buttonBox.rejected.connect(BuscarDlg.reject)

        QMetaObject.connectSlotsByName(BuscarDlg)
    # setupUi

    def retranslateUi(self, BuscarDlg):
        BuscarDlg.setWindowTitle(QCoreApplication.translate("BuscarDlg", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("BuscarDlg", u"Buscar en:", None))
    # retranslateUi

