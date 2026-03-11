# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datodlg.ui'
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
    QTextEdit, QVBoxLayout, QWidget)

from ts import (DataDialog, TComboBox)

class Ui_DatoDlgClass(object):
    def setupUi(self, DatoDlgClass):
        if not DatoDlgClass.objectName():
            DatoDlgClass.setObjectName(u"DatoDlgClass")
        DatoDlgClass.resize(713, 483)
        self.verticalLayout = QVBoxLayout(DatoDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(DatoDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.nombre = QLineEdit(DatoDlgClass)
        self.nombre.setObjectName(u"nombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nombre)

        self.label_2 = QLabel(DatoDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.clasificacion = TComboBox(DatoDlgClass)
        self.clasificacion.setObjectName(u"clasificacion")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.clasificacion)

        self.label = QLabel(DatoDlgClass)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label)

        self.unidades = QLineEdit(DatoDlgClass)
        self.unidades.setObjectName(u"unidades")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.unidades)

        self.label_4 = QLabel(DatoDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.descripcion = QTextEdit(DatoDlgClass)
        self.descripcion.setObjectName(u"descripcion")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.descripcion)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(206, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(DatoDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.clasificacion)
        self.label.setBuddy(self.unidades)
        self.label_4.setBuddy(self.descripcion)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nombre, self.clasificacion)
        QWidget.setTabOrder(self.clasificacion, self.unidades)
        QWidget.setTabOrder(self.unidades, self.descripcion)
        QWidget.setTabOrder(self.descripcion, self.buttonBox)

        self.retranslateUi(DatoDlgClass)
        self.buttonBox.accepted.connect(DatoDlgClass.accept)
        self.buttonBox.rejected.connect(DatoDlgClass.reject)

        QMetaObject.connectSlotsByName(DatoDlgClass)
    # setupUi

    def retranslateUi(self, DatoDlgClass):
        DatoDlgClass.setWindowTitle(QCoreApplication.translate("DatoDlgClass", u"Caracter\u00edsticas del punto de toma", None))
        self.label_3.setText(QCoreApplication.translate("DatoDlgClass", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("DatoDlgClass", u"Clasificaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("DatoDlgClass", u"Unidades", None))
        self.label_4.setText(QCoreApplication.translate("DatoDlgClass", u"Descripci\u00f3n", None))
    # retranslateUi

