# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscardlg.ui'
#
# Created: Fri Feb 21 12:06:28 2014
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

class Ui_BuscarDlg(object):
    def setupUi(self, BuscarDlg):
        BuscarDlg.setObjectName(_fromUtf8("BuscarDlg"))
        BuscarDlg.resize(452, 215)
        self.verticalLayout_2 = QtGui.QVBoxLayout(BuscarDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(BuscarDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.campos = QtGui.QComboBox(BuscarDlg)
        self.campos.setObjectName(_fromUtf8("campos"))
        self.gridLayout.addWidget(self.campos, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.texto = QtGui.QLineEdit(BuscarDlg)
        self.texto.setObjectName(_fromUtf8("texto"))
        self.verticalLayout.addWidget(self.texto)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 84, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(BuscarDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(BuscarDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BuscarDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BuscarDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(BuscarDlg)

    def retranslateUi(self, BuscarDlg):
        BuscarDlg.setWindowTitle(_translate("BuscarDlg", "Buscar", None))
        self.label.setText(_translate("BuscarDlg", "Buscar en:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BuscarDlg = QtGui.QDialog()
    ui = Ui_BuscarDlg()
    ui.setupUi(BuscarDlg)
    BuscarDlg.show()
    sys.exit(app.exec_())

