# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapdatocontaminanteaforodlg.ui'
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

class Ui_MapDatoContaminanteAforoDlgClass(object):
    def setupUi(self, MapDatoContaminanteAforoDlgClass):
        if not MapDatoContaminanteAforoDlgClass.objectName():
            MapDatoContaminanteAforoDlgClass.setObjectName(u"MapDatoContaminanteAforoDlgClass")
        MapDatoContaminanteAforoDlgClass.resize(458, 392)
        self.verticalLayout = QVBoxLayout(MapDatoContaminanteAforoDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(MapDatoContaminanteAforoDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.dato = TComboBox(MapDatoContaminanteAforoDlgClass)
        self.dato.setObjectName(u"dato")

        self.gridLayout.addWidget(self.dato, 1, 1, 1, 1)

        self.label = QLabel(MapDatoContaminanteAforoDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.clasificacion = TComboBox(MapDatoContaminanteAforoDlgClass)
        self.clasificacion.setObjectName(u"clasificacion")

        self.gridLayout.addWidget(self.clasificacion, 2, 1, 1, 1)

        self.label_5 = QLabel(MapDatoContaminanteAforoDlgClass)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.contaminante = TComboBox(MapDatoContaminanteAforoDlgClass)
        self.contaminante.setObjectName(u"contaminante")

        self.gridLayout.addWidget(self.contaminante, 3, 1, 1, 1)

        self.label_4 = QLabel(MapDatoContaminanteAforoDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.p = QLineEdit(MapDatoContaminanteAforoDlgClass)
        self.p.setObjectName(u"p")

        self.gridLayout.addWidget(self.p, 4, 1, 1, 1)

        self.aforo = TComboBox(MapDatoContaminanteAforoDlgClass)
        self.aforo.setObjectName(u"aforo")

        self.gridLayout.addWidget(self.aforo, 0, 1, 1, 1)

        self.label_3 = QLabel(MapDatoContaminanteAforoDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(206, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(MapDatoContaminanteAforoDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.dato)
        self.label_4.setBuddy(self.p)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.dato, self.p)
        QWidget.setTabOrder(self.p, self.buttonBox)

        self.retranslateUi(MapDatoContaminanteAforoDlgClass)
        self.buttonBox.accepted.connect(MapDatoContaminanteAforoDlgClass.accept)
        self.buttonBox.rejected.connect(MapDatoContaminanteAforoDlgClass.reject)

        QMetaObject.connectSlotsByName(MapDatoContaminanteAforoDlgClass)
    # setupUi

    def retranslateUi(self, MapDatoContaminanteAforoDlgClass):
        MapDatoContaminanteAforoDlgClass.setWindowTitle(QCoreApplication.translate("MapDatoContaminanteAforoDlgClass", u"Datos de factores de contaminantes por aforo", None))
        self.label_2.setText(QCoreApplication.translate("MapDatoContaminanteAforoDlgClass", u"Dato", None))
        self.label.setText(QCoreApplication.translate("MapDatoContaminanteAforoDlgClass", u"Clasificaci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("MapDatoContaminanteAforoDlgClass", u"Contaminante", None))
        self.label_4.setText(QCoreApplication.translate("MapDatoContaminanteAforoDlgClass", u"Factor", None))
        self.label_3.setText(QCoreApplication.translate("MapDatoContaminanteAforoDlgClass", u"Aforo", None))
    # retranslateUi

