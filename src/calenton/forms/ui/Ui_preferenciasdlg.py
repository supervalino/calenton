# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferenciasdlg.ui'
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
from PyQt6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_PreferenciasDlgClass(object):
    def setupUi(self, PreferenciasDlgClass):
        if not PreferenciasDlgClass.objectName():
            PreferenciasDlgClass.setObjectName(u"PreferenciasDlgClass")
        PreferenciasDlgClass.resize(390, 275)
        self.verticalLayout = QVBoxLayout(PreferenciasDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(PreferenciasDlgClass)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout = QFormLayout(self.tab)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.servidor = QLineEdit(self.tab)
        self.servidor.setObjectName(u"servidor")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.servidor)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.basedatos = QLineEdit(self.tab)
        self.basedatos.setObjectName(u"basedatos")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.basedatos)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.password = QLineEdit(self.tab)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.password)

        self.probar = QPushButton(self.tab)
        self.probar.setObjectName(u"probar")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.probar)

        self.usuario = QLineEdit(self.tab)
        self.usuario.setObjectName(u"usuario")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.usuario)

        self.puerto = QLineEdit(self.tab)
        self.puerto.setObjectName(u"puerto")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.puerto)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkScriptStackable = QCheckBox(self.tab_2)
        self.checkScriptStackable.setObjectName(u"checkScriptStackable")

        self.verticalLayout_2.addWidget(self.checkScriptStackable)

        self.beautifier = QCheckBox(self.tab_2)
        self.beautifier.setObjectName(u"beautifier")

        self.verticalLayout_2.addWidget(self.beautifier)

        self.verticalSpacer = QSpacerItem(20, 129, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.botones = QDialogButtonBox(PreferenciasDlgClass)
        self.botones.setObjectName(u"botones")
        self.botones.setOrientation(Qt.Orientation.Horizontal)
        self.botones.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.botones)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.servidor)
        self.label_2.setBuddy(self.basedatos)
        self.label_3.setBuddy(self.usuario)
        self.label_4.setBuddy(self.password)
        self.label_5.setBuddy(self.puerto)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.servidor, self.puerto)
        QWidget.setTabOrder(self.puerto, self.basedatos)
        QWidget.setTabOrder(self.basedatos, self.usuario)
        QWidget.setTabOrder(self.usuario, self.password)
        QWidget.setTabOrder(self.password, self.probar)
        QWidget.setTabOrder(self.probar, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.botones)

        self.retranslateUi(PreferenciasDlgClass)
        self.botones.accepted.connect(PreferenciasDlgClass.accept)
        self.botones.rejected.connect(PreferenciasDlgClass.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PreferenciasDlgClass)
    # setupUi

    def retranslateUi(self, PreferenciasDlgClass):
        PreferenciasDlgClass.setWindowTitle(QCoreApplication.translate("PreferenciasDlgClass", u"Preferencias", None))
        self.label.setText(QCoreApplication.translate("PreferenciasDlgClass", u"Servidor", None))
        self.label_2.setText(QCoreApplication.translate("PreferenciasDlgClass", u"Base de datos", None))
        self.label_3.setText(QCoreApplication.translate("PreferenciasDlgClass", u"Usuario", None))
        self.label_4.setText(QCoreApplication.translate("PreferenciasDlgClass", u"Contrase\u00f1a", None))
        self.probar.setText(QCoreApplication.translate("PreferenciasDlgClass", u"Probar...", None))
        self.label_5.setText(QCoreApplication.translate("PreferenciasDlgClass", u"Puerto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("PreferenciasDlgClass", u"Base de datos", None))
        self.checkScriptStackable.setText(QCoreApplication.translate("PreferenciasDlgClass", u"Emular contextos apilables", None))
        self.beautifier.setText(QCoreApplication.translate("PreferenciasDlgClass", u"Embellecer f\u00f3rmulas en informe de c\u00e1lculo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("PreferenciasDlgClass", u"Script", None))
    # retranslateUi

