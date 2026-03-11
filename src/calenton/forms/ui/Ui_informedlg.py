# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'informedlg.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PyQt6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_InformeDlgClass(object):
    def setupUi(self, InformeDlgClass):
        if not InformeDlgClass.objectName():
            InformeDlgClass.setObjectName(u"InformeDlgClass")
        InformeDlgClass.resize(400, 388)
        self.actionCopiar = QAction(InformeDlgClass)
        self.actionCopiar.setObjectName(u"actionCopiar")
        self.actionSelectAll = QAction(InformeDlgClass)
        self.actionSelectAll.setObjectName(u"actionSelectAll")
        self.verticalLayout = QVBoxLayout(InformeDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.informe = QPlainTextEdit(InformeDlgClass)
        self.informe.setObjectName(u"informe")
        self.informe.setUndoRedoEnabled(False)
        self.informe.setPlainText(u"")
        self.informe.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.informe)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.texto = QLineEdit(InformeDlgClass)
        self.texto.setObjectName(u"texto")

        self.horizontalLayout.addWidget(self.texto)

        self.busca = QPushButton(InformeDlgClass)
        self.busca.setObjectName(u"busca")

        self.horizontalLayout.addWidget(self.busca)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(InformeDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(InformeDlgClass)
        self.buttonBox.rejected.connect(InformeDlgClass.reject)
        self.actionCopiar.triggered.connect(self.informe.copy)
        self.actionSelectAll.triggered.connect(self.informe.selectAll)

        QMetaObject.connectSlotsByName(InformeDlgClass)
    # setupUi

    def retranslateUi(self, InformeDlgClass):
        InformeDlgClass.setWindowTitle(QCoreApplication.translate("InformeDlgClass", u"Informe de aforo", None))
        self.actionCopiar.setText(QCoreApplication.translate("InformeDlgClass", u"Copiar", None))
#if QT_CONFIG(shortcut)
        self.actionCopiar.setShortcut(QCoreApplication.translate("InformeDlgClass", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionSelectAll.setText(QCoreApplication.translate("InformeDlgClass", u"Select All", None))
#if QT_CONFIG(shortcut)
        self.actionSelectAll.setShortcut(QCoreApplication.translate("InformeDlgClass", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.busca.setText(QCoreApplication.translate("InformeDlgClass", u"Buscar...", None))
    # retranslateUi

