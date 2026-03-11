# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listaresultadodlg.ui'
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
    QHeaderView, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_ListaResultadoDlgClass(object):
    def setupUi(self, ListaResultadoDlgClass):
        if not ListaResultadoDlgClass.objectName():
            ListaResultadoDlgClass.setObjectName(u"ListaResultadoDlgClass")
        ListaResultadoDlgClass.resize(400, 300)
        self.actionCopiar = QAction(ListaResultadoDlgClass)
        self.actionCopiar.setObjectName(u"actionCopiar")
        self.actionCopiar.setShortcutContext(Qt.WidgetWithChildrenShortcut)
        self.verticalLayout = QVBoxLayout(ListaResultadoDlgClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabla = QTableView(ListaResultadoDlgClass)
        self.tabla.setObjectName(u"tabla")

        self.verticalLayout.addWidget(self.tabla)

        self.buttonBox = QDialogButtonBox(ListaResultadoDlgClass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ListaResultadoDlgClass)
        self.buttonBox.accepted.connect(ListaResultadoDlgClass.accept)
        self.buttonBox.rejected.connect(ListaResultadoDlgClass.reject)
        self.actionCopiar.triggered["bool"].connect(ListaResultadoDlgClass.copy)

        QMetaObject.connectSlotsByName(ListaResultadoDlgClass)
    # setupUi

    def retranslateUi(self, ListaResultadoDlgClass):
        ListaResultadoDlgClass.setWindowTitle(QCoreApplication.translate("ListaResultadoDlgClass", u"Resultados", None))
        self.actionCopiar.setText(QCoreApplication.translate("ListaResultadoDlgClass", u"Copiar", None))
#if QT_CONFIG(shortcut)
        self.actionCopiar.setShortcut(QCoreApplication.translate("ListaResultadoDlgClass", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

