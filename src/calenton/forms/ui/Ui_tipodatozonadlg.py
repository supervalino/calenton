# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tipodatozonadlg.ui'
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
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from ts import (DataDialog, TComboBox)

class Ui_TipoDatoZonaDlgClass(object):
    def setupUi(self, TipoDatoZonaDlgClass):
        if not TipoDatoZonaDlgClass.objectName():
            TipoDatoZonaDlgClass.setObjectName(u"TipoDatoZonaDlgClass")
        TipoDatoZonaDlgClass.resize(370, 203)
        self.verticalLayout = QVBoxLayout(TipoDatoZonaDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(TipoDatoZonaDlgClass)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(TipoDatoZonaDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.nombre = QLineEdit(TipoDatoZonaDlgClass)
        self.nombre.setObjectName(u"nombre")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nombre)

        self.label_3 = QLabel(TipoDatoZonaDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.unidades = QLineEdit(TipoDatoZonaDlgClass)
        self.unidades.setObjectName(u"unidades")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.unidades)

        self.escenario = TComboBox(TipoDatoZonaDlgClass)
        self.escenario.setObjectName(u"escenario")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.escenario)

        self.variable = QLineEdit(TipoDatoZonaDlgClass)
        self.variable.setObjectName(u"variable")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.variable)

        self.label_4 = QLabel(TipoDatoZonaDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.defecto = QLineEdit(TipoDatoZonaDlgClass)
        self.defecto.setObjectName(u"defecto")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.defecto)

        self.label_5 = QLabel(TipoDatoZonaDlgClass)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_5)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(TipoDatoZonaDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.escenario)
        self.label_2.setBuddy(self.nombre)
        self.label_3.setBuddy(self.unidades)
        self.label_4.setBuddy(self.variable)
        self.label_5.setBuddy(self.defecto)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.escenario, self.nombre)
        QWidget.setTabOrder(self.nombre, self.variable)
        QWidget.setTabOrder(self.variable, self.defecto)
        QWidget.setTabOrder(self.defecto, self.unidades)
        QWidget.setTabOrder(self.unidades, self.buttonBox)

        self.retranslateUi(TipoDatoZonaDlgClass)
        self.buttonBox.accepted.connect(TipoDatoZonaDlgClass.accept)
        self.buttonBox.rejected.connect(TipoDatoZonaDlgClass.reject)

        QMetaObject.connectSlotsByName(TipoDatoZonaDlgClass)
    # setupUi

    def retranslateUi(self, TipoDatoZonaDlgClass):
        TipoDatoZonaDlgClass.setWindowTitle(QCoreApplication.translate("TipoDatoZonaDlgClass", u"Tipos de datos por zona", None))
        self.label.setText(QCoreApplication.translate("TipoDatoZonaDlgClass", u"Escenario", None))
        self.label_2.setText(QCoreApplication.translate("TipoDatoZonaDlgClass", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("TipoDatoZonaDlgClass", u"Unidades", None))
        self.label_4.setText(QCoreApplication.translate("TipoDatoZonaDlgClass", u"Variable JavaScript", None))
        self.label_5.setText(QCoreApplication.translate("TipoDatoZonaDlgClass", u"Valor por defecto", None))
    # retranslateUi

