# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listaresultadodlg.ui'
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

class Ui_ListaResultadoDlgClass(object):
    def setupUi(self, ListaResultadoDlgClass):
        ListaResultadoDlgClass.setObjectName(_fromUtf8("ListaResultadoDlgClass"))
        ListaResultadoDlgClass.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(ListaResultadoDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabla = QtGui.QTableView(ListaResultadoDlgClass)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.verticalLayout.addWidget(self.tabla)
        self.buttonBox = QtGui.QDialogButtonBox(ListaResultadoDlgClass)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.actionCopiar = QtGui.QAction(ListaResultadoDlgClass)
        self.actionCopiar.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        self.actionCopiar.setObjectName(_fromUtf8("actionCopiar"))

        self.retranslateUi(ListaResultadoDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ListaResultadoDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ListaResultadoDlgClass.reject)
        QtCore.QObject.connect(self.actionCopiar, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), ListaResultadoDlgClass.copy)
        QtCore.QMetaObject.connectSlotsByName(ListaResultadoDlgClass)

    def retranslateUi(self, ListaResultadoDlgClass):
        ListaResultadoDlgClass.setWindowTitle(_translate("ListaResultadoDlgClass", "Resultados", None))
        self.actionCopiar.setText(_translate("ListaResultadoDlgClass", "Copiar", None))
        self.actionCopiar.setShortcut(_translate("ListaResultadoDlgClass", "Ctrl+C", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ListaResultadoDlgClass = QtGui.QDialog()
    ui = Ui_ListaResultadoDlgClass()
    ui.setupUi(ListaResultadoDlgClass)
    ListaResultadoDlgClass.show()
    sys.exit(app.exec_())

