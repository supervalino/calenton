# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graphicdlg.ui'
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
    QGroupBox, QLabel, QLineEdit, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

from ts import DataDialog

class Ui_GraphicDlgClass(object):
    def setupUi(self, GraphicDlgClass):
        if not GraphicDlgClass.objectName():
            GraphicDlgClass.setObjectName(u"GraphicDlgClass")
        GraphicDlgClass.resize(492, 570)
        self.verticalLayout_3 = QVBoxLayout(GraphicDlgClass)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabs = QTabWidget(GraphicDlgClass)
        self.tabs.setObjectName(u"tabs")
        self.general = QWidget()
        self.general.setObjectName(u"general")
        self.verticalLayout = QVBoxLayout(self.general)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.general)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.nombre = QLineEdit(self.general)
        self.nombre.setObjectName(u"nombre")

        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)

        self.label = QLabel(self.general)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.descripcion = QTextEdit(self.general)
        self.descripcion.setObjectName(u"descripcion")

        self.gridLayout.addWidget(self.descripcion, 1, 1, 1, 1)

        self.label_2 = QLabel(self.general)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.sql = QTextEdit(self.general)
        self.sql.setObjectName(u"sql")

        self.gridLayout.addWidget(self.sql, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tabs.addTab(self.general, "")
        self.parametros = QWidget()
        self.parametros.setObjectName(u"parametros")
        self.verticalLayout_2 = QVBoxLayout(self.parametros)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.parametros)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.titulo = QLineEdit(self.parametros)
        self.titulo.setObjectName(u"titulo")

        self.gridLayout_2.addWidget(self.titulo, 0, 1, 1, 1)

        self.label_5 = QLabel(self.parametros)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.nombreX = QLineEdit(self.parametros)
        self.nombreX.setObjectName(u"nombreX")

        self.gridLayout_2.addWidget(self.nombreX, 1, 1, 1, 1)

        self.label_6 = QLabel(self.parametros)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.nombreY = QLineEdit(self.parametros)
        self.nombreY.setObjectName(u"nombreY")

        self.gridLayout_2.addWidget(self.nombreY, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.groupBox = QGroupBox(self.parametros)
        self.groupBox.setObjectName(u"groupBox")
        self.barras = QRadioButton(self.groupBox)
        self.barras.setObjectName(u"barras")
        self.barras.setGeometry(QRect(20, 30, 105, 23))
        self.barrasAc = QRadioButton(self.groupBox)
        self.barrasAc.setObjectName(u"barrasAc")
        self.barrasAc.setGeometry(QRect(20, 60, 161, 23))
        self.tarta = QRadioButton(self.groupBox)
        self.tarta.setObjectName(u"tarta")
        self.tarta.setGeometry(QRect(20, 90, 105, 23))
        self.lineas = QRadioButton(self.groupBox)
        self.lineas.setObjectName(u"lineas")
        self.lineas.setGeometry(QRect(20, 120, 105, 23))

        self.verticalLayout_2.addWidget(self.groupBox)

        self.tabs.addTab(self.parametros, "")

        self.verticalLayout_3.addWidget(self.tabs)

        self.verticalSpacer = QSpacerItem(206, 31, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(GraphicDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.nombre)
        self.label.setBuddy(self.descripcion)
        self.label_2.setBuddy(self.sql)
        self.label_4.setBuddy(self.titulo)
        self.label_5.setBuddy(self.nombreX)
        self.label_6.setBuddy(self.nombreY)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.tabs, self.nombre)
        QWidget.setTabOrder(self.nombre, self.descripcion)
        QWidget.setTabOrder(self.descripcion, self.sql)
        QWidget.setTabOrder(self.sql, self.titulo)
        QWidget.setTabOrder(self.titulo, self.nombreX)
        QWidget.setTabOrder(self.nombreX, self.nombreY)
        QWidget.setTabOrder(self.nombreY, self.barras)
        QWidget.setTabOrder(self.barras, self.barrasAc)
        QWidget.setTabOrder(self.barrasAc, self.tarta)
        QWidget.setTabOrder(self.tarta, self.lineas)
        QWidget.setTabOrder(self.lineas, self.buttonBox)

        self.retranslateUi(GraphicDlgClass)
        self.buttonBox.accepted.connect(GraphicDlgClass.accept)
        self.buttonBox.rejected.connect(GraphicDlgClass.reject)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(GraphicDlgClass)
    # setupUi

    def retranslateUi(self, GraphicDlgClass):
        GraphicDlgClass.setWindowTitle(QCoreApplication.translate("GraphicDlgClass", u"Datos del Gr\u00e1fico", None))
        self.label_3.setText(QCoreApplication.translate("GraphicDlgClass", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("GraphicDlgClass", u"Descripci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("GraphicDlgClass", u"SQL", None))
        self.tabs.setTabText(self.tabs.indexOf(self.general), QCoreApplication.translate("GraphicDlgClass", u"General", None))
        self.label_4.setText(QCoreApplication.translate("GraphicDlgClass", u"T\u00edtulo", None))
        self.label_5.setText(QCoreApplication.translate("GraphicDlgClass", u"Nombre eje X", None))
        self.label_6.setText(QCoreApplication.translate("GraphicDlgClass", u"Nombre eje Y", None))
        self.groupBox.setTitle(QCoreApplication.translate("GraphicDlgClass", u"Tipo Gr\u00e1fico", None))
        self.barras.setText(QCoreApplication.translate("GraphicDlgClass", u"Barras", None))
        self.barrasAc.setText(QCoreApplication.translate("GraphicDlgClass", u"Barras acumulativo", None))
        self.tarta.setText(QCoreApplication.translate("GraphicDlgClass", u"Tarta", None))
        self.lineas.setText(QCoreApplication.translate("GraphicDlgClass", u"L\u00edneas", None))
        self.tabs.setTabText(self.tabs.indexOf(self.parametros), QCoreApplication.translate("GraphicDlgClass", u"Par\u00e1metros", None))
    # retranslateUi

