import sys

from PyQt5 import QtWidgets
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
	setupConnections(introWidget, labelWidget)
	addLabelingFuncs(labelWidget)

	# show first window...
	introWidget.show()
	sys.exit(app.exec_())


def setupConnections(introWidget, labelWidget):
	acceptCheck = introWidget.ui.AcceptCheckBox
	continueButton = introWidget.ui.ContinueButton
	acceptCheck.clicked.connect(continueButton.setEnabled)

	def switchWindows():
		introWidget.hide()
		labelWidget.show()

	continueButton.clicked.connect(switchWindows)


def addLabelingFuncs(labelWidget):
	def updateFont():
		font = labelWidget.ui.fontComboBox.currentFont()
		size = labelWidget.ui.PointSizeSpinBox.value()
		font.setPointSize(size)
		labelWidget.ui.JournalEntryText.setFont(font)

	# TODO: limit fonts to something reasonable
	# self.fontComboBox.setFontFilters(QtWidgets.QFontComboBox.ProportionalFonts)
	labelWidget.ui.PointSizeSpinBox.valueChanged.connect(updateFont)
	labelWidget.ui.fontComboBox.currentFontChanged.connect(updateFont)

	# TODO: set text from journals
	labelWidget.ui.JournalEntryText.setText("Hello world! \n\n does newLine work?")


if __name__ == '__main__':
	main()
