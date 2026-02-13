# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reportlist.ui'
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

class Ui_ReportListClass(object):
    def setupUi(self, ReportListClass):
        ReportListClass.setObjectName(_fromUtf8("ReportListClass"))
        ReportListClass.resize(614, 457)
        self.verticalLayout = QtGui.QVBoxLayout(ReportListClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(ReportListClass)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.informeAc = QtGui.QLineEdit(ReportListClass)
        self.informeAc.setEnabled(False)
        self.informeAc.setObjectName(_fromUtf8("informeAc"))
        self.horizontalLayout_2.addWidget(self.informeAc)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabla = QtGui.QTableWidget(ReportListClass)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.verticalLayout.addWidget(self.tabla)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.crear = QtGui.QPushButton(ReportListClass)
        self.crear.setObjectName(_fromUtf8("crear"))
        self.horizontalLayout.addWidget(self.crear)
        self.activar = QtGui.QPushButton(ReportListClass)
        self.activar.setObjectName(_fromUtf8("activar"))
        self.horizontalLayout.addWidget(self.activar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.elimina = QtGui.QPushButton(ReportListClass)
        self.elimina.setObjectName(_fromUtf8("elimina"))
        self.horizontalLayout.addWidget(self.elimina)
        self.edita = QtGui.QPushButton(ReportListClass)
        self.edita.setObjectName(_fromUtf8("edita"))
        self.horizontalLayout.addWidget(self.edita)
        self.anade = QtGui.QPushButton(ReportListClass)
        self.anade.setObjectName(_fromUtf8("anade"))
        self.horizontalLayout.addWidget(self.anade)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.insertFromClipboard = QtGui.QAction(ReportListClass)
        self.insertFromClipboard.setObjectName(_fromUtf8("insertFromClipboard"))

        self.retranslateUi(ReportListClass)
        QtCore.QObject.connect(self.insertFromClipboard, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), ReportListClass.dataFromClipboard)
        QtCore.QMetaObject.connectSlotsByName(ReportListClass)
        ReportListClass.setTabOrder(self.elimina, self.edita)
        ReportListClass.setTabOrder(self.edita, self.anade)

    def retranslateUi(self, ReportListClass):
        ReportListClass.setWindowTitle(_translate("ReportListClass", "Lista de informes", None))
        self.label.setText(_translate("ReportListClass", "Informe Activo:", None))
        self.crear.setText(_translate("ReportListClass", "Crear", None))
        self.activar.setText(_translate("ReportListClass", "Activar", None))
        self.elimina.setText(_translate("ReportListClass", "Eliminar", None))
        self.edita.setText(_translate("ReportListClass", "Editar", None))
        self.anade.setText(_translate("ReportListClass", "Añadir", None))
        self.insertFromClipboard.setText(_translate("ReportListClass", "Insertar desde portapapeles", None))

from widgets.datalist import DataList

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ReportListClass = QtGui.DataList()
    ui = Ui_ReportListClass()
    ui.setupUi(ReportListClass)
    ReportListClass.show()
    sys.exit(app.exec_())

