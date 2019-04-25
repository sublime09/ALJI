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

if __name__ == '__main__':
	main()
