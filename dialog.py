# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog, text_only = False, default_text = None):
        self.text_only = text_only
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.branch_name = QtWidgets.QLineEdit(Dialog)
        self.branch_name.setGeometry(QtCore.QRect(70, 60, 231, 21))
        self.branch_name.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 60, 16))
        self.label.setObjectName("label")

        if default_text != None:
            self.branch_name.setText(default_text)

        if text_only == False:
            self.weight = QtWidgets.QLineEdit(Dialog)
            self.weight.setGeometry(QtCore.QRect(70, 140, 231, 21))
            self.weight.setObjectName("textEdit")
            self.label_2 = QtWidgets.QLabel(Dialog)
            self.label_2.setGeometry(QtCore.QRect(70, 110, 60, 16))
            self.label_2.setObjectName("label_2")
            self.normalize = QtWidgets.QCheckBox("Keep weight and normalize to 1",Dialog)
            self.normalize.setGeometry(QtCore.QRect(70, 180, 280, 16))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name"))
        if self.text_only == False:
            self.label_2.setText(_translate("Dialog", "Weight"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
