# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferenciasdlg.ui'
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

class Ui_PreferenciasDlgClass(object):
    def setupUi(self, PreferenciasDlgClass):
        PreferenciasDlgClass.setObjectName(_fromUtf8("PreferenciasDlgClass"))
        PreferenciasDlgClass.resize(390, 275)
        self.verticalLayout = QtGui.QVBoxLayout(PreferenciasDlgClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(PreferenciasDlgClass)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayout = QtGui.QFormLayout(self.tab)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.servidor = QtGui.QLineEdit(self.tab)
        self.servidor.setObjectName(_fromUtf8("servidor"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.servidor)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.basedatos = QtGui.QLineEdit(self.tab)
        self.basedatos.setObjectName(_fromUtf8("basedatos"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.basedatos)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.password = QtGui.QLineEdit(self.tab)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.password)
        self.probar = QtGui.QPushButton(self.tab)
        self.probar.setObjectName(_fromUtf8("probar"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.probar)
        self.usuario = QtGui.QLineEdit(self.tab)
        self.usuario.setObjectName(_fromUtf8("usuario"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.usuario)
        self.puerto = QtGui.QLineEdit(self.tab)
        self.puerto.setObjectName(_fromUtf8("puerto"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.puerto)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkScriptStackable = QtGui.QCheckBox(self.tab_2)
        self.checkScriptStackable.setObjectName(_fromUtf8("checkScriptStackable"))
        self.verticalLayout_2.addWidget(self.checkScriptStackable)
        self.beautifier = QtGui.QCheckBox(self.tab_2)
        self.beautifier.setObjectName(_fromUtf8("beautifier"))
        self.verticalLayout_2.addWidget(self.beautifier)
        spacerItem = QtGui.QSpacerItem(20, 129, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.botones = QtGui.QDialogButtonBox(PreferenciasDlgClass)
        self.botones.setOrientation(QtCore.Qt.Horizontal)
        self.botones.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.botones.setObjectName(_fromUtf8("botones"))
        self.verticalLayout.addWidget(self.botones)
        self.label.setBuddy(self.servidor)
        self.label_2.setBuddy(self.basedatos)
        self.label_3.setBuddy(self.usuario)
        self.label_4.setBuddy(self.password)
        self.label_5.setBuddy(self.puerto)

        self.retranslateUi(PreferenciasDlgClass)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.botones, QtCore.SIGNAL(_fromUtf8("accepted()")), PreferenciasDlgClass.accept)
        QtCore.QObject.connect(self.botones, QtCore.SIGNAL(_fromUtf8("rejected()")), PreferenciasDlgClass.reject)
        QtCore.QMetaObject.connectSlotsByName(PreferenciasDlgClass)
        PreferenciasDlgClass.setTabOrder(self.servidor, self.puerto)
        PreferenciasDlgClass.setTabOrder(self.puerto, self.basedatos)
        PreferenciasDlgClass.setTabOrder(self.basedatos, self.usuario)
        PreferenciasDlgClass.setTabOrder(self.usuario, self.password)
        PreferenciasDlgClass.setTabOrder(self.password, self.probar)
        PreferenciasDlgClass.setTabOrder(self.probar, self.tabWidget)
        PreferenciasDlgClass.setTabOrder(self.tabWidget, self.botones)

    def retranslateUi(self, PreferenciasDlgClass):
        PreferenciasDlgClass.setWindowTitle(_translate("PreferenciasDlgClass", "Preferencias", None))
        self.label.setText(_translate("PreferenciasDlgClass", "Servidor", None))
        self.label_2.setText(_translate("PreferenciasDlgClass", "Base de datos", None))
        self.label_3.setText(_translate("PreferenciasDlgClass", "Usuario", None))
        self.label_4.setText(_translate("PreferenciasDlgClass", "Contraseña", None))
        self.probar.setText(_translate("PreferenciasDlgClass", "Probar...", None))
        self.label_5.setText(_translate("PreferenciasDlgClass", "Puerto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PreferenciasDlgClass", "Base de datos", None))
        self.checkScriptStackable.setText(_translate("PreferenciasDlgClass", "Emular contextos apilables", None))
        self.beautifier.setText(_translate("PreferenciasDlgClass", "Embellecer fórmulas en informe de cálculo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PreferenciasDlgClass", "Script", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PreferenciasDlgClass = QtGui.QDialog()
    ui = Ui_PreferenciasDlgClass()
    ui.setupUi(PreferenciasDlgClass)
    PreferenciasDlgClass.show()
    sys.exit(app.exec_())

