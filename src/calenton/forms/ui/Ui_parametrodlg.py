# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parametrodlg.ui'
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

from ts import (DataDialog, TComboBox)

class Ui_ParametroDlgClass(object):
    def setupUi(self, ParametroDlgClass):
        if not ParametroDlgClass.objectName():
            ParametroDlgClass.setObjectName(u"ParametroDlgClass")
        ParametroDlgClass.resize(545, 542)
        self.verticalLayout = QVBoxLayout(ParametroDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(ParametroDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.nombre = QLineEdit(ParametroDlgClass)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)

        self.label_2 = QLabel(ParametroDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.escenario = TComboBox(ParametroDlgClass)
        self.escenario.setObjectName(u"escenario")

        self.gridLayout.addWidget(self.escenario, 1, 1, 1, 1)

        self.label = QLabel(ParametroDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.valor = QLineEdit(ParametroDlgClass)
        self.valor.setObjectName(u"valor")

        self.gridLayout.addWidget(self.valor, 2, 1, 1, 1)

        self.label_4 = QLabel(ParametroDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.descripcion = QTextEdit(ParametroDlgClass)
        self.descripcion.setObjectName(u"descripcion")

        self.gridLayout.addWidget(self.descripcion, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(206, 183, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ParametroDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.escenario)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nombre, self.escenario)

        self.retranslateUi(ParametroDlgClass)
        self.buttonBox.accepted.connect(ParametroDlgClass.accept)
        self.buttonBox.rejected.connect(ParametroDlgClass.reject)

        QMetaObject.connectSlotsByName(ParametroDlgClass)
    # setupUi

    def retranslateUi(self, ParametroDlgClass):
        ParametroDlgClass.setWindowTitle(QCoreApplication.translate("ParametroDlgClass", u"Datos de par\u00e1metro", None))
        self.label_3.setText(QCoreApplication.translate("ParametroDlgClass", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("ParametroDlgClass", u"Escenario", None))
        self.label.setText(QCoreApplication.translate("ParametroDlgClass", u"Valor", None))
        self.label_4.setText(QCoreApplication.translate("ParametroDlgClass", u"Descripci\u00f3n", None))
    # retranslateUi

