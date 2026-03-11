# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fuenteclasificaciondlg.ui'
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
    QVBoxLayout, QWidget)

from ts import (DataDialog, TComboBox)

class Ui_FuenteClasificacionDlgClass(object):
    def setupUi(self, FuenteClasificacionDlgClass):
        if not FuenteClasificacionDlgClass.objectName():
            FuenteClasificacionDlgClass.setObjectName(u"FuenteClasificacionDlgClass")
        FuenteClasificacionDlgClass.resize(448, 329)
        self.verticalLayout = QVBoxLayout(FuenteClasificacionDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(FuenteClasificacionDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.nombre = QLineEdit(FuenteClasificacionDlgClass)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 2)

        self.label_2 = QLabel(FuenteClasificacionDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.fuente = TComboBox(FuenteClasificacionDlgClass)
        self.fuente.setObjectName(u"fuente")

        self.gridLayout.addWidget(self.fuente, 1, 2, 1, 1)

        self.label = QLabel(FuenteClasificacionDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)

        self.clasificacion = TComboBox(FuenteClasificacionDlgClass)
        self.clasificacion.setObjectName(u"clasificacion")

        self.gridLayout.addWidget(self.clasificacion, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(206, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(FuenteClasificacionDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.nombre)
        self.label_2.setBuddy(self.fuente)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nombre, self.fuente)

        self.retranslateUi(FuenteClasificacionDlgClass)
        self.buttonBox.accepted.connect(FuenteClasificacionDlgClass.accept)
        self.buttonBox.rejected.connect(FuenteClasificacionDlgClass.reject)

        QMetaObject.connectSlotsByName(FuenteClasificacionDlgClass)
    # setupUi

    def retranslateUi(self, FuenteClasificacionDlgClass):
        FuenteClasificacionDlgClass.setWindowTitle(QCoreApplication.translate("FuenteClasificacionDlgClass", u"Datos de tipo de clasificaci\u00f3n por fuente", None))
        self.label_3.setText(QCoreApplication.translate("FuenteClasificacionDlgClass", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("FuenteClasificacionDlgClass", u"Fuente", None))
        self.label.setText(QCoreApplication.translate("FuenteClasificacionDlgClass", u"Clasificaci\u00f3n", None))
    # retranslateUi

