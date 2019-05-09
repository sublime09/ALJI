import sys
from threading import Timer
from JournalGroup import JournalGroup

from PyQt5 import QtWidgets, QtGui, QtCore
from IntroWidget import Ui_IntroWidget
from LabelingWidget import Ui_LabelingWidget



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

		self.showIntro() # show first window...

		result = self.app.exec_()
		if self.model is not None:
			self.model.save()
		self.autoSaver.cancel()
		sys.exit(result)

	def showIntro(self):
		self.connectIntroToTask()
		self.intro.show()

	def showLabelTask(self, groupNum):
		self.model = JournalGroup(groupNum)
		self.setupJournalNav()
		self.updateJournalAndLabels()
		self.setupFontChanges()
		self.addCustomCrisisFuncs()
		self.labeler.ui.crisisFrame.deleteLater() #was placeholder 
		self.labeler.show()
		self.autoSaver.start()

	def startAutoSave(self):
		if self.model is not None:
			self.model.save()
			self.autoSaver = Timer(10, self.startAutoSave)
			self.autoSaver.start()


	def setupJournalLabeling(self):
		# journalDisplay = self.labeler.ui.journalEntryText
		# journalDisplay.setText(self.model.currentText())
		pass

	def updateJournalAndLabels(self):
		# JOURNAL TEXT
		jText = self.model.getCurrentText()
		self.labeler.ui.journalEntryText.setText(jText)
		num = self.model.taskNum
		total = self.model.taskTotal
		newText = "Journal Label Task %s/%s" % (num, total)
		self.labeler.ui.taskNumberLabel.setText(newText)
		#CRISIS LABELS
		parent = self.labeler.ui.crisisGroupBox
		parentLayout = self.labeler.ui.crisisGroupBoxLayout
		for child in parent.children():
			if isinstance(child, QtWidgets.QFrame):
				child.deleteLater()
		print("currentMark=", self.model.currentMark)
		for cName, checked in self.model.currentMark.labels.items():
			self.addCrisisLabel(cName, checked)


	def setupJournalNav(self):
		def goNext():
			self.model.nextJ()
			self.updateJournalAndLabels()
		def goBack():
			self.model.prevJ()
			self.updateJournalAndLabels()
		self.labeler.ui.backButton.clicked.connect(goBack)
		self.labeler.ui.forwardButton.clicked.connect(goNext)


	def addCrisisLabel(self, cName, checked=False):
		parent = self.labeler.ui.crisisGroupBox
		parentLayout = self.labeler.ui.crisisGroupBoxLayout
		cFrame = QtWidgets.QFrame(parent)
		self.model.currentMark.newLabel(cName, checked)

		def doCheck():
			self.model.currentMark.toggleLabel(cName)
		def doDelete():
			self.model.currentMark.delLabel(cName)
			cFrame.deleteLater()
		def confirmDelete():
			return doDelete() # NOTE may change if confirmation needed!

		cFrame.setFrameShape(QtWidgets.QFrame.Box)
		cFrame.setObjectName("crisisFrame_"+cName)
		hLayout = QtWidgets.QHBoxLayout(cFrame)
		hLayout.setObjectName("hLayout_"+cName)
		crisisCB = QtWidgets.QCheckBox(cFrame)
		crisisCB.setObjectName("crisisCB_"+cName)
		crisisCB.setText(cName)
		crisisCB.setChecked(checked)
		crisisCB.clicked.connect(doCheck)
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
