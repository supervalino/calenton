# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listadoresultadosdlg.ui'
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
from PyQt6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from ts import TComboBox

class Ui_ListadoResultadosDlgClass(object):
    def setupUi(self, ListadoResultadosDlgClass):
        if not ListadoResultadosDlgClass.objectName():
            ListadoResultadosDlgClass.setObjectName(u"ListadoResultadosDlgClass")
        ListadoResultadosDlgClass.resize(489, 199)
        self.verticalLayout = QVBoxLayout(ListadoResultadosDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(ListadoResultadosDlgClass)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.escenario = TComboBox(ListadoResultadosDlgClass)
        self.escenario.setObjectName(u"escenario")

        self.horizontalLayout_5.addWidget(self.escenario)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 4)

        self.label = QLabel(ListadoResultadosDlgClass)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.agregaContaminante = QRadioButton(ListadoResultadosDlgClass)
        self.agregaContaminante.setObjectName(u"agregaContaminante")
        self.agregaContaminante.setChecked(False)

        self.gridLayout.addWidget(self.agregaContaminante, 1, 1, 1, 1)

        self.todosContaminante = QRadioButton(ListadoResultadosDlgClass)
        self.todosContaminante.setObjectName(u"todosContaminante")

        self.gridLayout.addWidget(self.todosContaminante, 1, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.soloContaminante = QRadioButton(ListadoResultadosDlgClass)
        self.soloContaminante.setObjectName(u"soloContaminante")

        self.horizontalLayout.addWidget(self.soloContaminante)

        self.contaminante = TComboBox(ListadoResultadosDlgClass)
        self.contaminante.setObjectName(u"contaminante")
        self.contaminante.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contaminante.sizePolicy().hasHeightForWidth())
        self.contaminante.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.contaminante)

        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 4, 1, 1)

        self.label_2 = QLabel(ListadoResultadosDlgClass)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.agregaFuente = QRadioButton(ListadoResultadosDlgClass)
        self.agregaFuente.setObjectName(u"agregaFuente")
        self.agregaFuente.setChecked(False)

        self.gridLayout.addWidget(self.agregaFuente, 2, 1, 1, 1)

        self.todosFuente = QRadioButton(ListadoResultadosDlgClass)
        self.todosFuente.setObjectName(u"todosFuente")

        self.gridLayout.addWidget(self.todosFuente, 2, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.soloFuente = QRadioButton(ListadoResultadosDlgClass)
        self.soloFuente.setObjectName(u"soloFuente")

        self.horizontalLayout_2.addWidget(self.soloFuente)

        self.fuente = TComboBox(ListadoResultadosDlgClass)
        self.fuente.setObjectName(u"fuente")
        self.fuente.setEnabled(False)
        sizePolicy.setHeightForWidth(self.fuente.sizePolicy().hasHeightForWidth())
        self.fuente.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.fuente)

        self.horizontalLayout_2.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 4, 1, 1)

        self.label_3 = QLabel(ListadoResultadosDlgClass)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.agregaZona = QRadioButton(ListadoResultadosDlgClass)
        self.agregaZona.setObjectName(u"agregaZona")
        self.agregaZona.setChecked(False)

        self.gridLayout.addWidget(self.agregaZona, 3, 1, 1, 1)

        self.todosZona = QRadioButton(ListadoResultadosDlgClass)
        self.todosZona.setObjectName(u"todosZona")

        self.gridLayout.addWidget(self.todosZona, 3, 2, 1, 1)

        self.nivelZona = TComboBox(ListadoResultadosDlgClass)
        self.nivelZona.setObjectName(u"nivelZona")
        self.nivelZona.setEnabled(False)

        self.gridLayout.addWidget(self.nivelZona, 3, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.soloZona = QRadioButton(ListadoResultadosDlgClass)
        self.soloZona.setObjectName(u"soloZona")

        self.horizontalLayout_3.addWidget(self.soloZona)

        self.zona = TComboBox(ListadoResultadosDlgClass)
        self.zona.setObjectName(u"zona")
        self.zona.setEnabled(False)
        sizePolicy.setHeightForWidth(self.zona.sizePolicy().hasHeightForWidth())
        self.zona.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.zona)

        self.horizontalLayout_3.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 4, 1, 1)

        self.label_4 = QLabel(ListadoResultadosDlgClass)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.agregaClasificacion = QRadioButton(ListadoResultadosDlgClass)
        self.agregaClasificacion.setObjectName(u"agregaClasificacion")
        self.agregaClasificacion.setChecked(True)

        self.gridLayout.addWidget(self.agregaClasificacion, 4, 1, 1, 1)

        self.todosClasificacion = QRadioButton(ListadoResultadosDlgClass)
        self.todosClasificacion.setObjectName(u"todosClasificacion")

        self.gridLayout.addWidget(self.todosClasificacion, 4, 2, 1, 1)

        self.nivelClasificacion = TComboBox(ListadoResultadosDlgClass)
        self.nivelClasificacion.setObjectName(u"nivelClasificacion")
        self.nivelClasificacion.setEnabled(False)
        sizePolicy.setHeightForWidth(self.nivelClasificacion.sizePolicy().hasHeightForWidth())
        self.nivelClasificacion.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.nivelClasificacion, 4, 3, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.soloClasificacion = QRadioButton(ListadoResultadosDlgClass)
        self.soloClasificacion.setObjectName(u"soloClasificacion")

        self.horizontalLayout_4.addWidget(self.soloClasificacion)

        self.clasificacion = TComboBox(ListadoResultadosDlgClass)
        self.clasificacion.setObjectName(u"clasificacion")
        self.clasificacion.setEnabled(False)
        sizePolicy.setHeightForWidth(self.clasificacion.sizePolicy().hasHeightForWidth())
        self.clasificacion.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.clasificacion)

        self.horizontalLayout_4.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ListadoResultadosDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.agregaContaminante)
        self.label_2.setBuddy(self.agregaFuente)
        self.label_3.setBuddy(self.agregaZona)
        self.label_4.setBuddy(self.agregaClasificacion)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.agregaContaminante, self.todosContaminante)
        QWidget.setTabOrder(self.todosContaminante, self.soloContaminante)
        QWidget.setTabOrder(self.soloContaminante, self.contaminante)
        QWidget.setTabOrder(self.contaminante, self.agregaFuente)
        QWidget.setTabOrder(self.agregaFuente, self.todosFuente)
        QWidget.setTabOrder(self.todosFuente, self.soloFuente)
        QWidget.setTabOrder(self.soloFuente, self.fuente)
        QWidget.setTabOrder(self.fuente, self.agregaZona)
        QWidget.setTabOrder(self.agregaZona, self.todosZona)
        QWidget.setTabOrder(self.todosZona, self.nivelZona)
        QWidget.setTabOrder(self.nivelZona, self.soloZona)
        QWidget.setTabOrder(self.soloZona, self.zona)
        QWidget.setTabOrder(self.zona, self.agregaClasificacion)
        QWidget.setTabOrder(self.agregaClasificacion, self.todosClasificacion)
        QWidget.setTabOrder(self.todosClasificacion, self.nivelClasificacion)
        QWidget.setTabOrder(self.nivelClasificacion, self.soloClasificacion)
        QWidget.setTabOrder(self.soloClasificacion, self.clasificacion)
        QWidget.setTabOrder(self.clasificacion, self.buttonBox)

        self.retranslateUi(ListadoResultadosDlgClass)
        self.buttonBox.accepted.connect(ListadoResultadosDlgClass.accept)
        self.buttonBox.rejected.connect(ListadoResultadosDlgClass.reject)
        self.soloContaminante.toggled.connect(self.contaminante.setEnabled)
        self.soloFuente.toggled.connect(self.fuente.setEnabled)
        self.soloZona.toggled.connect(self.zona.setEnabled)
        self.soloClasificacion.toggled.connect(self.clasificacion.setEnabled)
        self.agregaZona.toggled.connect(self.nivelZona.setDisabled)
        self.agregaClasificacion.toggled.connect(self.nivelClasificacion.setDisabled)

        QMetaObject.connectSlotsByName(ListadoResultadosDlgClass)
    # setupUi

    def retranslateUi(self, ListadoResultadosDlgClass):
        ListadoResultadosDlgClass.setWindowTitle(QCoreApplication.translate("ListadoResultadosDlgClass", u"Seleccione el listado...", None))
        self.label_5.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Escenario", None))
        self.label.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Contaminante", None))
        self.agregaContaminante.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Agregar equiv.", None))
        self.todosContaminante.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Todos", None))
        self.soloContaminante.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"S\u00f3lo", None))
        self.label_2.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Fuente", None))
        self.agregaFuente.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Agregar", None))
        self.todosFuente.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Todos", None))
        self.soloFuente.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"S\u00f3lo", None))
        self.label_3.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Zona", None))
        self.agregaZona.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Agregar", None))
        self.todosZona.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Todos", None))
        self.soloZona.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"S\u00f3lo", None))
        self.label_4.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Clasificaci\u00f3n", None))
        self.agregaClasificacion.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Agregar", None))
        self.todosClasificacion.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"Todos", None))
        self.soloClasificacion.setText(QCoreApplication.translate("ListadoResultadosDlgClass", u"S\u00f3lo", None))
    # retranslateUi

