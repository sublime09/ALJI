import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from IntroWidget import Ui_IntroWidget
from LabelingWidget import Ui_LabelingWidget
from DelCrisisDialog import Ui_DelCrisisDialog

def toWidget(wigObject):
	wig = QtWidgets.QWidget()
	wig.ui = wigObject
	wig.ui.setupUi(wig)
	return wig

class Controller:
	def __init__(self):
		self.app = QtWidgets.QApplication(sys.argv)

		# setup widgets and their uis
		self.intro = toWidget(Ui_IntroWidget())
		self.labeler = toWidget(Ui_LabelingWidget())
		self.delConfirm = toWidget(Ui_DelCrisisDialog())

		# do connections...
		self.connectIntroToTask()
		self.setupJournal()    # TODO
		self.setupJournalNav() # TODO
		self.setupFontChanges()
		self.addCustomCrisisFuncs()

		basicCrises = "Suicide Depression Anger".split()
		for cName in basicCrises:
			self.addCrisisLabel(cName)
		self.labeler.ui.crisisFrame.deleteLater() #was placeholder 


		# show first window...
		self.intro.show()
		sys.exit(self.app.exec_())


	def setupJournal(self):
		journalDisplay = self.labeler.ui.journalEntryText
		journalDisplay.setText("Hello world! \n\n does newLine work?")
		# TODO: set text from journals
		pass

	def setupJournalNav(self):
		# TODO: set nav across journals
		pass

	def addCrisisLabel(self, cName):
		# TODO: add crisis checked functionality
		parent = self.labeler.ui.crisisGroupBox
		parentLayout = self.labeler.ui.crisisGroupBoxLayout
		cFrame = QtWidgets.QFrame(parent)
		def doDelete():
			cFrame.deleteLater()
			self.delConfirm.close()
		def confirmDelete():
			self.delConfirm = toWidget(Ui_DelCrisisDialog())
			self.delConfirm.ui.buttonBox.accepted.connect(doDelete)
			self.delConfirm.ui.buttonBox.rejected.connect(self.delConfirm.close)
			self.delConfirm.show()

		cFrame.setFrameShape(QtWidgets.QFrame.Box)
		cFrame.setObjectName("crisisFrame_"+cName)
		hLayout = QtWidgets.QHBoxLayout(cFrame)
		hLayout.setObjectName("hLayout_"+cName)
		crisisCB = QtWidgets.QCheckBox(cFrame)
		crisisCB.setObjectName("crisisCB_"+cName)
		crisisCB.setText(cName)
		hLayout.addWidget(crisisCB)
		delCrisisButton = QtWidgets.QToolButton(cFrame)
		delIcon = QtGui.QIcon()
		delIcon.addPixmap(QtGui.QPixmap("images/times.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		delCrisisButton.setIcon(delIcon)
		delCrisisButton.setIconSize(QtCore.QSize(20, 20))
		delCrisisButton.setObjectName("deleteCrisis_"+cName)
		delCrisisButton.clicked.connect(confirmDelete)
		hLayout.addWidget(delCrisisButton)
		parentLayout.addWidget(cFrame)

	def addCustomCrisisFuncs(self):
		labelerUI = self.labeler.ui
		newCrisisLine = labelerUI.customCrisisLine
		def addNewCrisis():
			newCrisis = str(self.labeler.ui.customCrisisLine.text())
			newCrisis = newCrisis.strip()
			if (newCrisis is not ""):
				newCrisisLine.setText("")
				self.addCrisisLabel(newCrisis)
		addButton = labelerUI.addCustomButton.clicked.connect(addNewCrisis)


	def connectIntroToTask(self):
		def switchWindows():
			self.intro.hide()
			self.labeler.show()
		acceptCheck = self.intro.ui.AcceptCheckBox
		continueButton = self.intro.ui.ContinueButton
		acceptCheck.clicked.connect(continueButton.setEnabled)
		continueButton.clicked.connect(switchWindows)

	def setupFontChanges(self):
		labelerUI = self.labeler.ui
		def updateFont():
			font = labelerUI.fontComboBox.currentFont()
			size = labelerUI.pointSizeSpinBox.value()
			font.setPointSize(size)
			labelerUI.journalEntryText.setFont(font)
		# TODO: limit fonts to something reasonable
		# self.fontComboBox.setFontFilters(QtWidgets.QFontComboBox.ProportionalFonts)
		labelerUI.pointSizeSpinBox.valueChanged.connect(updateFont)
		labelerUI.fontComboBox.currentFontChanged.connect(updateFont)

if __name__ == '__main__':
	Controller()
