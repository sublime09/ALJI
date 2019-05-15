# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/IntroWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IntroWidget(object):
    def setupUi(self, IntroWidget):
        IntroWidget.setObjectName("IntroWidget")
        IntroWidget.resize(900, 600)
        IntroWidget.setMinimumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        IntroWidget.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(IntroWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WelcomeLabel = QtWidgets.QLabel(IntroWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.WelcomeLabel.setScaledContents(False)
        self.WelcomeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.WelcomeLabel.setWordWrap(True)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.verticalLayout.addWidget(self.WelcomeLabel)
        self.InstructionsLabel = QtWidgets.QLabel(IntroWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InstructionsLabel.sizePolicy().hasHeightForWidth())
        self.InstructionsLabel.setSizePolicy(sizePolicy)
        self.InstructionsLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.InstructionsLabel.setTextFormat(QtCore.Qt.AutoText)
        self.InstructionsLabel.setScaledContents(False)
        self.InstructionsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.InstructionsLabel.setWordWrap(True)
        self.InstructionsLabel.setOpenExternalLinks(True)
        self.InstructionsLabel.setObjectName("InstructionsLabel")
        self.verticalLayout.addWidget(self.InstructionsLabel)
        self.AcceptCheckBox = QtWidgets.QCheckBox(IntroWidget)
        self.AcceptCheckBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AcceptCheckBox.sizePolicy().hasHeightForWidth())
        self.AcceptCheckBox.setSizePolicy(sizePolicy)
        self.AcceptCheckBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.AcceptCheckBox.setAcceptDrops(False)
        self.AcceptCheckBox.setAutoFillBackground(True)
        self.AcceptCheckBox.setIconSize(QtCore.QSize(15, 15))
        self.AcceptCheckBox.setCheckable(True)
        self.AcceptCheckBox.setChecked(False)
        self.AcceptCheckBox.setTristate(False)
        self.AcceptCheckBox.setObjectName("AcceptCheckBox")
        self.verticalLayout.addWidget(self.AcceptCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupNumSpinBox = QtWidgets.QSpinBox(IntroWidget)
        self.groupNumSpinBox.setSuffix("")
        self.groupNumSpinBox.setMinimum(1)
        self.groupNumSpinBox.setMaximum(16)
        self.groupNumSpinBox.setObjectName("groupNumSpinBox")
        self.horizontalLayout.addWidget(self.groupNumSpinBox)
        self.ContinueButton = QtWidgets.QPushButton(IntroWidget)
        self.ContinueButton.setEnabled(False)
        self.ContinueButton.setCheckable(False)
        self.ContinueButton.setChecked(False)
        self.ContinueButton.setAutoRepeat(False)
        self.ContinueButton.setAutoExclusive(False)
        self.ContinueButton.setAutoDefault(False)
        self.ContinueButton.setDefault(False)
        self.ContinueButton.setFlat(False)
        self.ContinueButton.setObjectName("ContinueButton")
        self.horizontalLayout.addWidget(self.ContinueButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ContactMeLabel = QtWidgets.QLabel(IntroWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContactMeLabel.sizePolicy().hasHeightForWidth())
        self.ContactMeLabel.setSizePolicy(sizePolicy)
        self.ContactMeLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ContactMeLabel.setTextFormat(QtCore.Qt.AutoText)
        self.ContactMeLabel.setScaledContents(False)
        self.ContactMeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ContactMeLabel.setWordWrap(True)
        self.ContactMeLabel.setOpenExternalLinks(True)
        self.ContactMeLabel.setObjectName("ContactMeLabel")
        self.verticalLayout.addWidget(self.ContactMeLabel)

        self.retranslateUi(IntroWidget)
        self.AcceptCheckBox.clicked['bool'].connect(self.ContinueButton.toggle)
        self.ContinueButton.clicked.connect(IntroWidget.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(IntroWidget)

    def retranslateUi(self, IntroWidget):
        _translate = QtCore.QCoreApplication.translate
        IntroWidget.setWindowTitle(_translate("IntroWidget", "ALJI Label Helper Introduction"))
        self.WelcomeLabel.setText(_translate("IntroWidget", "Welcome"))
        self.InstructionsLabel.setText(_translate("IntroWidget", "<html><head/><body><p><a name=\"docs-internal-guid-267460d2-7fff-ab05-71db-b4f90adb88b5\"/><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">T</span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">hank you for contributing to the </span><span style=\" font-family:\'Arial\'; font-weight:696; color:#000000; background-color:transparent;\">A</span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">ctive </span><span style=\" font-family:\'Arial\'; font-weight:696; color:#000000; background-color:transparent;\">L</span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">istening </span><span style=\" font-family:\'Arial\'; font-weight:696; color:#000000; background-color:transparent;\">J</span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">ournal </span><span style=\" font-family:\'Arial\'; font-weight:696; color:#000000; background-color:transparent;\">I</span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">nteraction (</span><span style=\" font-family:\'Arial\'; font-weight:696; color:#000000; background-color:transparent;\">ALJI</span><span style=\" font-family:\'Arial\'; color:#000000; background-color:transparent;\">) project. ALJI is a program designed to support the counseling of college students with depression or other illnesses by privately responding to their expressive writing or personal journal entries. </span></p><p>See the online instructions for your task description and an overview of the ALJI project before continuing. It is important you follow those instructions to remain consistent with other contributors. </p><p>Those with either a professional or academic background in recognizing mental health indicators are uniquely qualified to the task of labeling the following personal journals.  </p></body></html>"))
        self.AcceptCheckBox.setText(_translate("IntroWidget", "I Agree that I am qualified for this task"))
        self.groupNumSpinBox.setPrefix(_translate("IntroWidget", "Group #"))
        self.ContinueButton.setText(_translate("IntroWidget", "Continue to Tasks"))
        self.ContactMeLabel.setText(_translate("IntroWidget", "<html><head/><body><p>Email the primary researcher, Patrick Sullivan (<a href=\"mailto:sublime@vt.edu?subject=ALJI Label Helper question\"><span style=\" text-decoration: underline; color:#0000ff;\">sublime@vt.edu</span></a>) for any questions you have on the ALJI project or your task. </p></body></html>"))

