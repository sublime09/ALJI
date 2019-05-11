from typing import Callable
from PyQt5 import QtCore, QtGui, QtWidgets
from .images import icons_rc

class LabelFrame(QtWidgets.QFrame):
	def __init__(self):
		super().__init__()
		self.layout = QtWidgets.QHBoxLayout(self)
		self.checkBox = QtWidgets.QCheckBox(self)
		self.checkBox.setText("UNKNOWN_LABEL")
		self.deleteButton = QtWidgets.QToolButton(self)
		pixmap = QtGui.QPixmap(":/icon/times.svg")
		delIcon = QtGui.QIcon()
		delIcon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.deleteButton.setIcon(delIcon)
		self.deleteButton.setIconSize(QtCore.QSize(20, 20))
		self.layout.addWidget(self.checkBox)
		self.layout.addWidget(self.deleteButton)

	def setState(self, name: str, checked: bool):
		self.checkBox.setText(name)
		self.checkBox.setChecked(checked)

	def setActions(self, checkAction: Callable, delAction: Callable):
		self.deleteButton.clicked.connect(delAction)
		self.checkBox.clicked.connect(checkAction)
