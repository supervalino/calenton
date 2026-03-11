# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapdatocontaminantedlg.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from ts import (DataDialog, TComboBox)

class Ui_MapDatoContaminanteDlgClass(object):
    def setupUi(self, MapDatoContaminanteDlgClass):
        if not MapDatoContaminanteDlgClass.objectName():
            MapDatoContaminanteDlgClass.setObjectName(u"MapDatoContaminanteDlgClass")
        MapDatoContaminanteDlgClass.resize(405, 344)
        self.verticalLayout = QVBoxLayout(MapDatoContaminanteDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(MapDatoContaminanteDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.escenario = QLineEdit(MapDatoContaminanteDlgClass)
        self.escenario.setObjectName(u"escenario")
        self.escenario.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.escenario)

        self.label = QLabel(MapDatoContaminanteDlgClass)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.clasificacion = QLineEdit(MapDatoContaminanteDlgClass)
        self.clasificacion.setObjectName(u"clasificacion")
        self.clasificacion.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.clasificacion)

        self.label_2 = QLabel(MapDatoContaminanteDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.dato = QLineEdit(MapDatoContaminanteDlgClass)
        self.dato.setObjectName(u"dato")
        self.dato.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dato)

        self.label_5 = QLabel(MapDatoContaminanteDlgClass)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.comboContaminante = TComboBox(MapDatoContaminanteDlgClass)
        self.comboContaminante.setObjectName(u"comboContaminante")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.comboContaminante)

        self.label_4 = QLabel(MapDatoContaminanteDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.editorFormula = QPlainTextEdit(MapDatoContaminanteDlgClass)
        self.editorFormula.setObjectName(u"editorFormula")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editorFormula.sizePolicy().hasHeightForWidth())
        self.editorFormula.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editorFormula)

        self.label_6 = QLabel(MapDatoContaminanteDlgClass)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.valor = QLineEdit(MapDatoContaminanteDlgClass)
        self.valor.setObjectName(u"valor")
        self.valor.setEnabled(False)

        self.horizontalLayout.addWidget(self.valor)

        self.indenta = QPushButton(MapDatoContaminanteDlgClass)
        self.indenta.setObjectName(u"indenta")

        self.horizontalLayout.addWidget(self.indenta)

        self.probar = QPushButton(MapDatoContaminanteDlgClass)
        self.probar.setObjectName(u"probar")

        self.horizontalLayout.addWidget(self.probar)


        self.formLayout.setLayout(5, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(MapDatoContaminanteDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.escenario)
        self.label.setBuddy(self.clasificacion)
        self.label_2.setBuddy(self.dato)
        self.label_5.setBuddy(self.comboContaminante)
        self.label_4.setBuddy(self.editorFormula)
        self.label_6.setBuddy(self.valor)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboContaminante, self.editorFormula)
        QWidget.setTabOrder(self.editorFormula, self.buttonBox)
        QWidget.setTabOrder(self.buttonBox, self.clasificacion)
        QWidget.setTabOrder(self.clasificacion, self.dato)
        QWidget.setTabOrder(self.dato, self.escenario)
        QWidget.setTabOrder(self.escenario, self.valor)

        self.retranslateUi(MapDatoContaminanteDlgClass)
        self.buttonBox.accepted.connect(MapDatoContaminanteDlgClass.accept)
        self.buttonBox.rejected.connect(MapDatoContaminanteDlgClass.reject)

        QMetaObject.connectSlotsByName(MapDatoContaminanteDlgClass)
    # setupUi

    def retranslateUi(self, MapDatoContaminanteDlgClass):
        MapDatoContaminanteDlgClass.setWindowTitle(QCoreApplication.translate("MapDatoContaminanteDlgClass", u"Datos de factores de contaminantes", None))
        self.label_3.setText(QCoreApplication.translate("MapDatoContaminanteDlgClass", u"Escenario", None))
        self.label.setText(QCoreApplication.translate("MapDatoContaminanteDlgClass", u"Clasificaci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("MapDatoContaminanteDlgClass", u"Dato", None))
        self.label_5.setText(QCoreApplication.translate("MapDatoContaminanteDlgClass", u"Contaminante", None))
        self.label_4.setText(QCoreApplication.translate("MapDatoContaminanteDlgClass", u"Formula", None))
        self.label_6.setText(QCoreApplication.translate("MapDatoContaminanteDlgClass", u"Valor Calculado", None))
        self.indenta.setText(QCoreApplication.translate("MapDatoContaminanteDlgClass", u"Indentar", None))
        self.probar.setText(QCoreApplication.translate("MapDatoContaminanteDlgClass", u"Probar", None))
    # retranslateUi

