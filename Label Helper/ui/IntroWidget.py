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
        IntroWidget.resize(784, 608)
        IntroWidget.setMinimumSize(QtCore.QSize(676, 542))
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
        self.textEdit = QtWidgets.QTextEdit(IntroWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.BottomHoriLayout = QtWidgets.QHBoxLayout()
        self.BottomHoriLayout.setObjectName("BottomHoriLayout")
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
        self.BottomHoriLayout.addWidget(self.AcceptCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.BottomHoriLayout.addItem(spacerItem)
        self.groupNumSpinBox = QtWidgets.QSpinBox(IntroWidget)
        self.groupNumSpinBox.setSuffix("")
        self.groupNumSpinBox.setMinimum(1)
        self.groupNumSpinBox.setMaximum(16)
        self.groupNumSpinBox.setObjectName("groupNumSpinBox")
        self.BottomHoriLayout.addWidget(self.groupNumSpinBox)
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
        self.BottomHoriLayout.addWidget(self.ContinueButton)
        self.verticalLayout.addLayout(self.BottomHoriLayout)
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
        self.textEdit.setHtml(_translate("IntroWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thank you for contributing to the <span style=\" font-weight:600;\">A</span>ctive <span style=\" font-weight:600;\">L</span>istening <span style=\" font-weight:600;\">J</span>ournal <span style=\" font-weight:600;\">I</span>nteraction (<span style=\" font-weight:600;\">ALJI</span>) project. ALJI is a program designed to support the counseling of college students with depression by privately responding to their expressive writing or personal journal entries. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program is used to label the dataset that will be used in the training and testing of ALJI. The ALJI program can learn how to detect when an author is going through a mental health crisis based off of their expressive language and the labels you assign to certain language. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You are given about 6 journal entries to read and label, which will take roughly 30 minutes to complete. Which entries you are labeling is determined by your assigned Group#.  </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It is important you follow this guide when labeling journal entries:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Read the entire passage as if it is an entry in someone\'s personal journal or diary</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Consider the mental wellness of the author (assume the author is a high school senior in the USA, age 18)</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Take note of any sentences that are alarming or concerning (if any). If you beleive the author of this journal may need professional mental health support / couseling, do the following:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• Clarify the reason of your concern by applying a \'Crisis Label\' to the journal entry (\'checking\' the checkbox). Some default labels are provided, and you may create custom labels as you see fit. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">• When you have completed the labeling task for each entry in the group, follow the online instructions for reporting the labeling results to the researcher.  </p></body></html>"))
        self.AcceptCheckBox.setText(_translate("IntroWidget", "I Agree that I am qualified for this task"))
        self.groupNumSpinBox.setPrefix(_translate("IntroWidget", "Group #"))
        self.ContinueButton.setText(_translate("IntroWidget", "Continue to Tasks"))
        self.ContactMeLabel.setText(_translate("IntroWidget", "<html><head/><body><p>Email Patrick Sullivan\n"
"(<a href=\"mailto:sublime@vt.edu?subject=ALJI Label Helper question\"><span style=\" text-decoration: underline; color:#0000ff;\">sublime@vt.edu</span></a>)\n"
"\n"
"for any questions you have on the project. \n"
"\n"
"</p></body></html>"))

