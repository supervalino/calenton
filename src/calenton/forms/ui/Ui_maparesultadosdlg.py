# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maparesultadosdlg.ui'
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
    QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from ts import TComboBox

class Ui_MapaResultadosDlgClass(object):
    def setupUi(self, MapaResultadosDlgClass):
        if not MapaResultadosDlgClass.objectName():
            MapaResultadosDlgClass.setObjectName(u"MapaResultadosDlgClass")
        MapaResultadosDlgClass.resize(363, 229)
        self.verticalLayout = QVBoxLayout(MapaResultadosDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(MapaResultadosDlgClass)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.escenario = TComboBox(MapaResultadosDlgClass)
        self.escenario.setObjectName(u"escenario")

        self.horizontalLayout_5.addWidget(self.escenario)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)

        self.label_3 = QLabel(MapaResultadosDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.nivelZona = TComboBox(MapaResultadosDlgClass)
        self.nivelZona.setObjectName(u"nivelZona")
        self.nivelZona.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.nivelZona)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.label = QLabel(MapaResultadosDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.agregaContaminante = QRadioButton(MapaResultadosDlgClass)
        self.agregaContaminante.setObjectName(u"agregaContaminante")
        self.agregaContaminante.setChecked(False)

        self.gridLayout.addWidget(self.agregaContaminante, 2, 1, 1, 1)

        self.soloContaminante = QRadioButton(MapaResultadosDlgClass)
        self.soloContaminante.setObjectName(u"soloContaminante")

        self.gridLayout.addWidget(self.soloContaminante, 2, 2, 1, 1)

        self.contaminante = TComboBox(MapaResultadosDlgClass)
        self.contaminante.setObjectName(u"contaminante")
        self.contaminante.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contaminante.sizePolicy().hasHeightForWidth())
        self.contaminante.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.contaminante, 2, 3, 1, 1)

        self.label_2 = QLabel(MapaResultadosDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.agregaFuente = QRadioButton(MapaResultadosDlgClass)
        self.agregaFuente.setObjectName(u"agregaFuente")
        self.agregaFuente.setChecked(False)

        self.gridLayout.addWidget(self.agregaFuente, 3, 1, 1, 1)

        self.soloFuente = QRadioButton(MapaResultadosDlgClass)
        self.soloFuente.setObjectName(u"soloFuente")

        self.gridLayout.addWidget(self.soloFuente, 3, 2, 1, 1)

        self.fuente = TComboBox(MapaResultadosDlgClass)
        self.fuente.setObjectName(u"fuente")
        self.fuente.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fuente.sizePolicy().hasHeightForWidth())
        self.fuente.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.fuente, 3, 3, 1, 1)

        self.label_4 = QLabel(MapaResultadosDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.agregaClasificacion = QRadioButton(MapaResultadosDlgClass)
        self.agregaClasificacion.setObjectName(u"agregaClasificacion")
        self.agregaClasificacion.setChecked(True)

        self.gridLayout.addWidget(self.agregaClasificacion, 4, 1, 1, 1)

        self.soloClasificacion = QRadioButton(MapaResultadosDlgClass)
        self.soloClasificacion.setObjectName(u"soloClasificacion")

        self.gridLayout.addWidget(self.soloClasificacion, 4, 2, 1, 1)

        self.nivelClasificacion = TComboBox(MapaResultadosDlgClass)
        self.nivelClasificacion.setObjectName(u"nivelClasificacion")
        self.nivelClasificacion.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.nivelClasificacion.sizePolicy().hasHeightForWidth())
        self.nivelClasificacion.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.nivelClasificacion, 4, 3, 1, 1)

        self.clasificacion = TComboBox(MapaResultadosDlgClass)
        self.clasificacion.setObjectName(u"clasificacion")
        self.clasificacion.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.clasificacion.sizePolicy().hasHeightForWidth())
        self.clasificacion.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.clasificacion, 5, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboColor = QComboBox(MapaResultadosDlgClass)
        self.comboColor.setObjectName(u"comboColor")

        self.horizontalLayout.addWidget(self.comboColor)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 3, 1, 1)

        self.label_6 = QLabel(MapaResultadosDlgClass)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(MapaResultadosDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_5.setBuddy(self.escenario)
        self.label_3.setBuddy(self.nivelZona)
        self.label.setBuddy(self.agregaContaminante)
        self.label_2.setBuddy(self.agregaFuente)
        self.label_4.setBuddy(self.agregaClasificacion)
        self.label_6.setBuddy(self.comboColor)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.escenario, self.nivelZona)
        QWidget.setTabOrder(self.nivelZona, self.comboColor)
        QWidget.setTabOrder(self.comboColor, self.agregaContaminante)
        QWidget.setTabOrder(self.agregaContaminante, self.soloContaminante)
        QWidget.setTabOrder(self.soloContaminante, self.contaminante)
        QWidget.setTabOrder(self.contaminante, self.agregaFuente)
        QWidget.setTabOrder(self.agregaFuente, self.soloFuente)
        QWidget.setTabOrder(self.soloFuente, self.fuente)
        QWidget.setTabOrder(self.fuente, self.agregaClasificacion)
        QWidget.setTabOrder(self.agregaClasificacion, self.soloClasificacion)
        QWidget.setTabOrder(self.soloClasificacion, self.nivelClasificacion)
        QWidget.setTabOrder(self.nivelClasificacion, self.clasificacion)
        QWidget.setTabOrder(self.clasificacion, self.buttonBox)

        self.retranslateUi(MapaResultadosDlgClass)
        self.buttonBox.accepted.connect(MapaResultadosDlgClass.accept)
        self.buttonBox.rejected.connect(MapaResultadosDlgClass.reject)
        self.soloContaminante.toggled.connect(self.contaminante.setEnabled)
        self.soloFuente.toggled.connect(self.fuente.setEnabled)
        self.soloClasificacion.toggled.connect(self.clasificacion.setEnabled)
        self.soloClasificacion.toggled.connect(self.nivelClasificacion.setEnabled)

        QMetaObject.connectSlotsByName(MapaResultadosDlgClass)
    # setupUi

    def retranslateUi(self, MapaResultadosDlgClass):
        MapaResultadosDlgClass.setWindowTitle(QCoreApplication.translate("MapaResultadosDlgClass", u"Seleccione el listado...", None))
        self.label_5.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"Escenario", None))
        self.label_3.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"Zona", None))
        self.label.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"Contaminante", None))
        self.agregaContaminante.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"Agregar equiv.", None))
        self.soloContaminante.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"S\u00f3lo", None))
        self.label_2.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"Fuente", None))
        self.agregaFuente.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"Agregar", None))
        self.soloFuente.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"S\u00f3lo", None))
        self.label_4.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"Clasificaci\u00f3n", None))
        self.agregaClasificacion.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"Agregar", None))
        self.soloClasificacion.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"S\u00f3lo", None))
        self.label_6.setText(QCoreApplication.translate("MapaResultadosDlgClass", u"Colores", None))
    # retranslateUi

