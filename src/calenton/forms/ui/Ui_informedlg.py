# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'informedlg.ui'
#
# Created: Fri Feb 21 12:06:30 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_InformeDlgClass(object):
    def setupUi(self, InformeDlgClass):
        InformeDlgClass.setObjectName(_fromUtf8("InformeDlgClass"))
        InformeDlgClass.resize(400, 388)
        self.verticalLayout = QtGui.QVBoxLayout(InformeDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.informe = QtGui.QPlainTextEdit(InformeDlgClass)
        self.informe.setUndoRedoEnabled(False)
        self.informe.setPlainText(_fromUtf8(""))
        self.informe.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.informe.setObjectName(_fromUtf8("informe"))
        self.verticalLayout.addWidget(self.informe)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.texto = QtGui.QLineEdit(InformeDlgClass)
        self.texto.setObjectName(_fromUtf8("texto"))
        self.horizontalLayout.addWidget(self.texto)
        self.busca = QtGui.QPushButton(InformeDlgClass)
        self.busca.setObjectName(_fromUtf8("busca"))
        self.horizontalLayout.addWidget(self.busca)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(InformeDlgClass)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.actionCopiar = QtGui.QAction(InformeDlgClass)
        self.actionCopiar.setObjectName(_fromUtf8("actionCopiar"))
        self.actionSelectAll = QtGui.QAction(InformeDlgClass)
        self.actionSelectAll.setObjectName(_fromUtf8("actionSelectAll"))

        self.retranslateUi(InformeDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), InformeDlgClass.reject)
        QtCore.QObject.connect(self.actionCopiar, QtCore.SIGNAL(_fromUtf8("triggered()")), self.informe.copy)
        QtCore.QObject.connect(self.actionSelectAll, QtCore.SIGNAL(_fromUtf8("triggered()")), self.informe.selectAll)
        QtCore.QMetaObject.connectSlotsByName(InformeDlgClass)

    def retranslateUi(self, InformeDlgClass):
        InformeDlgClass.setWindowTitle(_translate("InformeDlgClass", "Informe de aforo", None))
        self.busca.setText(_translate("InformeDlgClass", "Buscar...", None))
        self.actionCopiar.setText(_translate("InformeDlgClass", "Copiar", None))
        self.actionCopiar.setShortcut(_translate("InformeDlgClass", "Ctrl+C", None))
        self.actionSelectAll.setText(_translate("InformeDlgClass", "Select All", None))
        self.actionSelectAll.setShortcut(_translate("InformeDlgClass", "Ctrl+A", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    InformeDlgClass = QtGui.QDialog()
    ui = Ui_InformeDlgClass()
    ui.setupUi(InformeDlgClass)
    InformeDlgClass.show()
    sys.exit(app.exec_())

