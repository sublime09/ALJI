# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DelCrisisDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DelCrisisDialog(object):
    def setupUi(self, DelCrisisDialog):
        DelCrisisDialog.setObjectName("DelCrisisDialog")
        DelCrisisDialog.resize(329, 172)
        DelCrisisDialog.setMinimumSize(QtCore.QSize(329, 172))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        DelCrisisDialog.setFont(font)
        self.vboxlayout = QtWidgets.QVBoxLayout(DelCrisisDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label = QtWidgets.QLabel(DelCrisisDialog)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(DelCrisisDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(DelCrisisDialog)
        QtCore.QMetaObject.connectSlotsByName(DelCrisisDialog)

    def retranslateUi(self, DelCrisisDialog):
        _translate = QtCore.QCoreApplication.translate
        DelCrisisDialog.setWindowTitle(_translate("DelCrisisDialog", "Delete Crisis Label?"))
        self.label.setText(_translate("DelCrisisDialog", "<html><head/><body><p>Deleting this Crisis Label will delete <span style=\" font-weight:600;\">all </span>instances you applied this label to text! </p><p>Delete this Crisis Label?</p></body></html>"))

