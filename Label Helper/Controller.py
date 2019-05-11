import sys
from threading import Timer
from model.JournalGroup import JournalGroup

from PyQt5 import QtWidgets, QtGui, QtCore
from ui.IntroWidget import Ui_IntroWidget
from ui.LabelingWidget import Ui_LabelingWidget
from ui.LabelFrame import LabelFrame


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
		self.model = None 
		self.autoSaver = Timer(10, self.startAutoSave)
		self.connectIntroToTask()
		self.intro.show()

		result = self.app.exec_()
		if self.model is not None:
			self.model.save()
		self.autoSaver.cancel()
		sys.exit(result)

	def showLabelTask(self, groupNum):
		self.model = JournalGroup(groupNum)
		self.setupJournalNav()
		self.setupFontChanges()
		self.addCustomCrisisFuncs()
		self.updateView()
		# self.setupJournalLabeling() # TOOO HARD
		# self.labeler.ui.crisisFrame.deleteLater() #was placeholder 
		self.labeler.showMaximized()
		self.autoSaver.start()

	def startAutoSave(self):
		if self.model is not None:
			self.model.save()
			self.autoSaver = Timer(10, self.startAutoSave)
			self.autoSaver.start()

	def updateView(self):
		m = self.model
		ui = self.labeler.ui
		# NAV LABEL
		newText = "Journal Label Task %s/%s" % (m.taskNum, m.taskTotal)
		ui.taskNumberLabel.setText(newText)
		print("Viewing Group{} Task{}".format(m.groupNum, m.taskNum))
		# JOURNAL TEXT
		ui.journalEntryText.setText(m.getCurrentText())
		#CRISIS LABELS
		for child in ui.labelScrollAreaWidgetContents.children():
			if not isinstance(child, QtWidgets.QVBoxLayout):
				child.deleteLater()
		for cName, checked in m.currentMark.labels.items():
			self.addCrisisLabel(cName, checked)

		# CGI
		cgiVal = m.currentMark.cgi
		ui.cgiSpinBox.setValue(cgiVal)
		def cgiChanged():
			newVal = ui.cgiSpinBox.value()
			m.currentMark.setCGI(newVal)
		ui.cgiSpinBox.valueChanged.connect(cgiChanged)


	def setupJournalNav(self):
		def goNext():
			self.model.nextJ()
			self.updateView()
		def goBack():
			self.model.prevJ()
			self.updateView()
		self.labeler.ui.backButton.clicked.connect(goBack)
		self.labeler.ui.forwardButton.clicked.connect(goNext)

	def addCrisisLabel(self, cName, checked=False):
		def doCheck():
			self.model.currentMark.toggleLabel(cName)
		def doDelete():
			self.model.currentMark.delLabel(cName)
			lFrame.deleteLater()
		lFrame = LabelFrame()
		lFrame.setState(cName, checked)
		lFrame.setActions(doCheck, doDelete)
		self.labeler.ui.labelScrollAreaLayout.addWidget(lFrame)

	def addCustomCrisisFuncs(self):
		labelerUI = self.labeler.ui
		newCrisisLine = labelerUI.customCrisisLine
		def addNewCrisis():
			newCrisis = str(self.labeler.ui.customCrisisLine.text())
			newCrisis = newCrisis.strip()
			if (newCrisis is not ""):
				newCrisisLine.setText("")
				self.addCrisisLabel(newCrisis)
				self.model.currentMark.newLabel(newCrisis)
		labelerUI.addCustomButton.clicked.connect(addNewCrisis)
		newCrisisLine.returnPressed.connect(addNewCrisis)

	def connectIntroToTask(self):
		def switchWindows():
			groupNum = self.intro.ui.groupNumSpinBox.value()
			self.intro.hide()
			self.showLabelTask(groupNum)
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
