# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tipoclasdlg.ui'
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

class Ui_TipoclasDlgClass(object):
    def setupUi(self, TipoclasDlgClass):
        if not TipoclasDlgClass.objectName():
            TipoclasDlgClass.setObjectName(u"TipoclasDlgClass")
        TipoclasDlgClass.resize(475, 355)
        self.verticalLayout = QVBoxLayout(TipoclasDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_8 = QLabel(TipoclasDlgClass)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.nombre = QLineEdit(TipoclasDlgClass)
        self.nombre.setObjectName(u"nombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nombre)

        self.label_9 = QLabel(TipoclasDlgClass)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.descripcion = QTextEdit(TipoclasDlgClass)
        self.descripcion.setObjectName(u"descripcion")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.descripcion)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(TipoclasDlgClass)
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

        self.retranslateUi(TipoclasDlgClass)
        self.buttonBox.accepted.connect(TipoclasDlgClass.accept)
        self.buttonBox.rejected.connect(TipoclasDlgClass.reject)

        QMetaObject.connectSlotsByName(TipoclasDlgClass)
    # setupUi

    def retranslateUi(self, TipoclasDlgClass):
        TipoclasDlgClass.setWindowTitle(QCoreApplication.translate("TipoclasDlgClass", u"Tipo de clasificaci\u00f3n", None))
        self.label_8.setText(QCoreApplication.translate("TipoclasDlgClass", u"Nombre", None))
        self.label_9.setText(QCoreApplication.translate("TipoclasDlgClass", u"Descripci\u00f3n", None))
    # retranslateUi

