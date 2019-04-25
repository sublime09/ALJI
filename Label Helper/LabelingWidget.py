# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\LabelingWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LabelingWidget(object):
    def setupUi(self, LabelingWidget):
        LabelingWidget.setObjectName("LabelingWidget")
        LabelingWidget.resize(640, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(LabelingWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(LabelingWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(LabelingWidget)
        self.pushButton.clicked.connect(LabelingWidget.close)
        QtCore.QMetaObject.connectSlotsByName(LabelingWidget)

    def retranslateUi(self, LabelingWidget):
        _translate = QtCore.QCoreApplication.translate
        LabelingWidget.setWindowTitle(_translate("LabelingWidget", "ALJI Label Helper Task"))
        self.pushButton.setText(_translate("LabelingWidget", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelingWidget = QtWidgets.QWidget()
    ui = Ui_LabelingWidget()
    ui.setupUi(LabelingWidget)
    LabelingWidget.show()
    sys.exit(app.exec_())

