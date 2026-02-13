# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clasificaciondlg.ui'
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

class Ui_ClasificacionDialogClass(object):
    def setupUi(self, ClasificacionDialogClass):
        ClasificacionDialogClass.setObjectName(_fromUtf8("ClasificacionDialogClass"))
        ClasificacionDialogClass.resize(524, 450)
        self.verticalLayout = QtGui.QVBoxLayout(ClasificacionDialogClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(ClasificacionDialogClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(ClasificacionDialogClass)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(ClasificacionDialogClass)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(ClasificacionDialogClass)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(ClasificacionDialogClass)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(ClasificacionDialogClass)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(ClasificacionDialogClass)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(ClasificacionDialogClass)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(ClasificacionDialogClass)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.textEdit = QtGui.QTextEdit(ClasificacionDialogClass)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_5.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line = QtGui.QFrame(ClasificacionDialogClass)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        spacerItem = QtGui.QSpacerItem(20, 54, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(ClasificacionDialogClass)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ClasificacionDialogClass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ClasificacionDialogClass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ClasificacionDialogClass.reject)
        QtCore.QMetaObject.connectSlotsByName(ClasificacionDialogClass)

    def retranslateUi(self, ClasificacionDialogClass):
        ClasificacionDialogClass.setWindowTitle(_translate("ClasificacionDialogClass", "Datos de clasificación", None))
        self.label.setText(_translate("ClasificacionDialogClass", "Id", None))
        self.label_2.setText(_translate("ClasificacionDialogClass", "Idtipoclas", None))
        self.label_3.setText(_translate("ClasificacionDialogClass", "Idpadre", None))
        self.label_4.setText(_translate("ClasificacionDialogClass", "Código", None))
        self.label_5.setText(_translate("ClasificacionDialogClass", "Descripción", None))

from ts import DataDialog

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ClasificacionDialogClass = QtGui.DataDialog()
    ui = Ui_ClasificacionDialogClass()
    ui.setupUi(ClasificacionDialogClass)
    ClasificacionDialogClass.show()
    sys.exit(app.exec_())

