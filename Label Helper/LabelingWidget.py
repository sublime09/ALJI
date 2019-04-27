# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LabelingWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LabelingWidget(object):
    def setupUi(self, LabelingWidget):
        LabelingWidget.setObjectName("LabelingWidget")
        LabelingWidget.resize(805, 707)
        self.horizontalLayout = QtWidgets.QHBoxLayout(LabelingWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.JournalEntryText = QtWidgets.QTextEdit(LabelingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JournalEntryText.sizePolicy().hasHeightForWidth())
        self.JournalEntryText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.JournalEntryText.setFont(font)
        self.JournalEntryText.setMouseTracking(True)
        self.JournalEntryText.setLineWidth(1)
        self.JournalEntryText.setDocumentTitle("")
        self.JournalEntryText.setReadOnly(True)
        self.JournalEntryText.setAcceptRichText(False)
        self.JournalEntryText.setObjectName("JournalEntryText")
        self.horizontalLayout.addWidget(self.JournalEntryText)
        self.LabelingLayout = QtWidgets.QVBoxLayout()
        self.LabelingLayout.setObjectName("LabelingLayout")
        self.CrisisTitleLabel = QtWidgets.QLabel(LabelingWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.CrisisTitleLabel.setFont(font)
        self.CrisisTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CrisisTitleLabel.setObjectName("CrisisTitleLabel")
        self.LabelingLayout.addWidget(self.CrisisTitleLabel)
        self.CrisisListWidget = QtWidgets.QListWidget(LabelingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CrisisListWidget.sizePolicy().hasHeightForWidth())
        self.CrisisListWidget.setSizePolicy(sizePolicy)
        self.CrisisListWidget.setMouseTracking(True)
        self.CrisisListWidget.setObjectName("CrisisListWidget")
        self.LabelingLayout.addWidget(self.CrisisListWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.LabelingLayout.addItem(spacerItem)
        self.NavLayout = QtWidgets.QHBoxLayout()
        self.NavLayout.setObjectName("NavLayout")
        self.BackButton = QtWidgets.QToolButton(LabelingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackButton.sizePolicy().hasHeightForWidth())
        self.BackButton.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon)
        self.BackButton.setIconSize(QtCore.QSize(20, 20))
        self.BackButton.setObjectName("BackButton")
        self.NavLayout.addWidget(self.BackButton)
        self.TaskNumberLabel = QtWidgets.QLabel(LabelingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TaskNumberLabel.sizePolicy().hasHeightForWidth())
        self.TaskNumberLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TaskNumberLabel.setFont(font)
        self.TaskNumberLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TaskNumberLabel.setObjectName("TaskNumberLabel")
        self.NavLayout.addWidget(self.TaskNumberLabel)
        self.ForwardButton = QtWidgets.QToolButton(LabelingWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ForwardButton.setIcon(icon1)
        self.ForwardButton.setIconSize(QtCore.QSize(20, 20))
        self.ForwardButton.setObjectName("ForwardButton")
        self.NavLayout.addWidget(self.ForwardButton)
        self.LabelingLayout.addLayout(self.NavLayout)
        self.FontLayout = QtWidgets.QHBoxLayout()
        self.FontLayout.setObjectName("FontLayout")
        self.fontComboBox = QtWidgets.QFontComboBox(LabelingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)
        self.fontComboBox.setFontFilters(QtWidgets.QFontComboBox.ProportionalFonts)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.fontComboBox.setCurrentFont(font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.FontLayout.addWidget(self.fontComboBox)
        self.PointSizeSpinBox = QtWidgets.QSpinBox(LabelingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointSizeSpinBox.sizePolicy().hasHeightForWidth())
        self.PointSizeSpinBox.setSizePolicy(sizePolicy)
        self.PointSizeSpinBox.setMinimum(5)
        self.PointSizeSpinBox.setMaximum(30)
        self.PointSizeSpinBox.setProperty("value", 11)
        self.PointSizeSpinBox.setObjectName("PointSizeSpinBox")
        self.FontLayout.addWidget(self.PointSizeSpinBox)
        self.LabelingLayout.addLayout(self.FontLayout)
        self.horizontalLayout.addLayout(self.LabelingLayout)

        self.retranslateUi(LabelingWidget)
        self.fontComboBox.currentFontChanged['QFont'].connect(self.JournalEntryText.setCurrentFont)
        self.PointSizeSpinBox.valueChanged['int'].connect(self.JournalEntryText.setFontWeight)
        QtCore.QMetaObject.connectSlotsByName(LabelingWidget)

    def retranslateUi(self, LabelingWidget):
        _translate = QtCore.QCoreApplication.translate
        LabelingWidget.setWindowTitle(_translate("LabelingWidget", "ALJI Label Helper Task"))
        self.JournalEntryText.setHtml(_translate("LabelingWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I walked into the dust filled room and admired the old perfume smells mixing with the gritty air. The sun filtered into the space creating strange shadows in the corners while the off-kilter light protruded straight onto the table in the middle of the room. It took a second for my senses to adjust to the ancient aroma; too many articles of clothing, books, and jewels were spilling about in and out like an Egyptian tomb. It felt somber, as if every item had already lived three lives before nearing old age on the yellowed table cloth in the antique store. The midnight blue beret rested there––alone––near the shadowy corner. It whispered to me even though girls my age should have been drawn to Barbies more than berets. I’ve always been captivated by different ideas of beauty. Knowing this, Mom graciously presented it to me, since all Saturday afternoons are occasions for celebratory gifts.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If I imagine carefully enough, I can almost smell the vague scent of perfume that wafted everywhere the blue beret went. I know lavender was the previous owner’s favorite scent. It was strong, yet womanly, as every great writer should be. I imagine she had a passion for life, something I would acquire as I wore that accessory. She was interested in politics, and most likely traveled from the edges of California to the cobbled streets of Rome in search of adventure, or parties filled with paper lanterns just so she would have an occasion to pop on the perfect hat. I felt the same way every Wednesday as I had tea with the fairies and my mom in our best dresses. Magical.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I know she was the kind of woman to attend wild safaris but still enjoy Sunday brunches cramped in hotel lobbies. She walked fearlessly, ready to conquer the rainy forests of Washington or the musky alleys of New York City as a lady of courage and power, the kind that didn’t just sit behind a desk and wait for change. She implemented it. If she had ideas then the whole world would know them. I imagine her as an editor, a great romanticist, and somewhat of a messy eater. I’m pretty sure there were still crumby memories of lemon bars hidden in the velvet.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I wore that beret with the same confidence, as if it gave every owner a mysterious new persona. I wore it proudly, and a bit awkwardly, as young girls do. I wore it to my first wedding and my first funeral. From antique shops to the tallest buildings, to the streets of Paris, to the smoky taverns of New Orleans, I imagine the midnight blue beret as a traveler itself: full of secrets regarding everything it would ever see. I know this history is true, because nothing can stop a woman wearing a midnight blue beret.</p></body></html>"))
        self.JournalEntryText.setPlaceholderText(_translate("LabelingWidget", "PLACEHOLDER TEXT"))
        self.CrisisTitleLabel.setText(_translate("LabelingWidget", "Crisis Labels"))
        self.BackButton.setText(_translate("LabelingWidget", "Back"))
        self.BackButton.setShortcut(_translate("LabelingWidget", "Ctrl+Left"))
        self.TaskNumberLabel.setText(_translate("LabelingWidget", "Journal Entry ??/??"))
        self.ForwardButton.setText(_translate("LabelingWidget", "Forward"))
        self.ForwardButton.setShortcut(_translate("LabelingWidget", "Ctrl+Right"))
        self.PointSizeSpinBox.setSuffix(_translate("LabelingWidget", " pt."))

