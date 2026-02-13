# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reportdlg.ui'
#
# Created: Fri Feb 21 12:06:31 2014
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

class Ui_ReportDlgClass(object):
    def setupUi(self, ReportDlgClass):
        ReportDlgClass.setObjectName(_fromUtf8("ReportDlgClass"))
        ReportDlgClass.resize(458, 392)
        self.verticalLayout = QtGui.QVBoxLayout(ReportDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(ReportDlgClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.nombre = QtGui.QLineEdit(ReportDlgClass)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)
        self.label = QtGui.QLabel(ReportDlgClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.descripcion = QtGui.QTextEdit(ReportDlgClass)
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.gridLayout.addWidget(self.descripcion, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(206, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(ReportDlgClass)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.nombre)
        self.label.setBuddy(self.descripcion)

        self.retranslateUi(ReportDlgClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ReportDlgClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ReportDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(ReportDlgClass)
        ReportDlgClass.setTabOrder(self.nombre, self.descripcion)
        ReportDlgClass.setTabOrder(self.descripcion, self.buttonBox)

    def retranslateUi(self, ReportDlgClass):
        ReportDlgClass.setWindowTitle(_translate("ReportDlgClass", "Datos de Informe", None))
        self.label_3.setText(_translate("ReportDlgClass", "Nombre", None))
        self.label.setText(_translate("ReportDlgClass", "Descripción", None))

from ts import DataDialog

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ReportDlgClass = QtGui.DataDialog()
    ui = Ui_ReportDlgClass()
    ui.setupUi(ReportDlgClass)
    ReportDlgClass.show()
    sys.exit(app.exec_())

