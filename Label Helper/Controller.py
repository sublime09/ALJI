import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from IntroWidget import Ui_IntroWidget
from LabelingWidget import Ui_LabelingWidget


def main():
	app = QtWidgets.QApplication(sys.argv)

	# setup widgets and their uis
	introWidget = QtWidgets.QWidget()
	introWidget.ui = Ui_IntroWidget()
	introWidget.ui.setupUi(introWidget)

	labelWidget = QtWidgets.QWidget()
	labelWidget.ui = Ui_LabelingWidget()
	labelWidget.ui.setupUi(labelWidget)

	# do connections...
	connectIntroToTask(introWidget, labelWidget)
	addLabelingFuncs(labelWidget)

	# show first window...
	introWidget.show()
	sys.exit(app.exec_())


def addLabelingFuncs(labelWidget):
	# TODO: set text from journals
	labelWidget.ui.journalEntryText.setText("Hello world! \n\n does newLine work?")
	basicCrises = "Suicide Depression Anger".split()
	for cName in basicCrises:
		addCrisisLabel(labelWidget, cName)
	addCustomCrisisFuncs(labelWidget)
	addFontFunctions(labelWidget)


def addCrisisLabel(labelWidget, cName):
	# TODO: make delete functionality
	# TODO: add crisis checked functionality
	# self.deleteCrisis.clicked.connect(self.crisisFrame.deleteLater)
	pass
	ui = labelWidget.ui
	cFrame = QtWidgets.QFrame(ui.crisisGroupBox)
	cFrame.setFrameShape(QtWidgets.QFrame.Box)
	cFrame.setObjectName("crisisFrame_"+cName)
	hLayout = QtWidgets.QHBoxLayout(cFrame)
	hLayout.setObjectName("hLayout_"+cName)
	crisisCB = QtWidgets.QCheckBox(cFrame)
	crisisCB.setObjectName("crisisCB+"+cName)
	crisisCB.setText(cName)
	hLayout.addWidget(crisisCB)
	delCrisisButton = QtWidgets.QToolButton(cFrame)
	delIcon = QtGui.QIcon()
	delIcon.addPixmap(QtGui.QPixmap("images/times.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	delCrisisButton.setIcon(delIcon)
	delCrisisButton.setIconSize(QtCore.QSize(20, 20))
	delCrisisButton.setObjectName("deleteCrisis_"+cName)
	hLayout.addWidget(delCrisisButton)
	ui.crisisGroupBoxLayout.addWidget(cFrame)




def addCustomCrisisFuncs(LabelingWidget):
	pass
	# TODO: custom crisis labels functionality
	# self.customCrisisFrame = QtWidgets.QFrame(self.crisisGroupBox)
	# self.customCrisisFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
	# self.customCrisisFrame.setFrameShadow(QtWidgets.QFrame.Raised)
	# self.customCrisisFrame.setObjectName("customCrisisFrame")
	# self._4 = QtWidgets.QHBoxLayout(self.customCrisisFrame)
	# self._4.setObjectName("_4")
	# self.customCrisisTextBox = QtWidgets.QPlainTextEdit(self.customCrisisFrame)
	# sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
	# sizePolicy.setHorizontalStretch(0)
	# sizePolicy.setVerticalStretch(0)
	# sizePolicy.setHeightForWidth(self.customCrisisTextBox.sizePolicy().hasHeightForWidth())
	# self.customCrisisTextBox.setSizePolicy(sizePolicy)
	# self.customCrisisTextBox.setMinimumSize(QtCore.QSize(0, 35))
	# self.customCrisisTextBox.setObjectName("customCrisisTextBox")
	# self._4.addWidget(self.customCrisisTextBox)
	# self.addCustomButton = QtWidgets.QToolButton(self.customCrisisFrame)
	# icon3 = QtGui.QIcon()
	# icon3.addPixmap(QtGui.QPixmap("images/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	# self.addCustomButton.setIcon(icon3)
	# self.addCustomButton.setIconSize(QtCore.QSize(20, 20))
	# self.addCustomButton.setObjectName("addCustomButton")
	# self._4.addWidget(self.addCustomButton)
	# self.vl2.addWidget(self.customCrisisFrame)


def connectIntroToTask(introWidget, labelWidget):
	acceptCheck = introWidget.ui.AcceptCheckBox
	continueButton = introWidget.ui.ContinueButton
	acceptCheck.clicked.connect(continueButton.setEnabled)
	def switchWindows():
		introWidget.hide()
		labelWidget.show()
	continueButton.clicked.connect(switchWindows)

def addFontFunctions(labelWidget):
	def updateFont():
		font = labelWidget.ui.fontComboBox.currentFont()
		size = labelWidget.ui.pointSizeSpinBox.value()
		font.setPointSize(size)
		labelWidget.ui.journalEntryText.setFont(font)
	# TODO: limit fonts to something reasonable
	# self.fontComboBox.setFontFilters(QtWidgets.QFontComboBox.ProportionalFonts)
	labelWidget.ui.pointSizeSpinBox.valueChanged.connect(updateFont)
	labelWidget.ui.fontComboBox.currentFontChanged.connect(updateFont)

if __name__ == '__main__':
	main()
