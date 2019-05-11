from typing import Callable
from PyQt5 import QtCore, QtGui, QtWidgets
from .images import icons_rc

class LabelFrame(QtWidgets.QFrame):
	def __init__(self, parent: QtWidgets.QWidget):
		super(LabelFrame, self).__init__(parent)
		self.layout = QtWidgets.QHBoxLayout(self)
		self.crisisCB = QtWidgets.QCheckBox(self)
		self.crisisCB.setText("UNKNOWN_LABEL")
		self.deleteButton = QtWidgets.QToolButton(self)
		pixmap = QtGui.QPixmap(":/icon/times.svg")
		delIcon = QtGui.QIcon()
		delIcon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.deleteButton.setIcon(delIcon)
		self.deleteButton.setIconSize(QtCore.QSize(20, 20))
		self.layout.addWidget(self.crisisCB)
		self.layout.addWidget(self.deleteButton)

	def setState(self, name: str, checked: bool):
		self.crisisCB.setText(name)
		self.crisisCB.setChecked(checked)

	def setActions(self, checkAction: Callable, delAction: Callable):
		self.deleteButton.clicked.connect(delAction)
		self.crisisCB.clicked.connect(checkAction)


'''
self.crisisFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
sizePolicy.setHorizontalStretch(0)
sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.crisisFrame.sizePolicy().hasHeightForWidth())
self.crisisFrame.setSizePolicy(sizePolicy)
self.crisisFrame.setFrameShape(QtWidgets.QFrame.Box)
self.crisisFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
self.crisisFrame.setObjectName("crisisFrame")
self.hl3 = QtWidgets.QHBoxLayout(self.crisisFrame)
self.hl3.setContentsMargins(-1, 2, -1, 2)
self.hl3.setObjectName("hl3")
self.crisisCB = QtWidgets.QCheckBox(self.crisisFrame)
sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
sizePolicy.setHorizontalStretch(0)
sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.crisisCB.sizePolicy().hasHeightForWidth())
self.crisisCB.setSizePolicy(sizePolicy)
self.crisisCB.setChecked(False)
self.crisisCB.setObjectName("crisisCB")
self.hl3.addWidget(self.crisisCB)
self.deleteCrisis = QtWidgets.QToolButton(self.crisisFrame)
sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
sizePolicy.setHorizontalStretch(0)
sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.deleteCrisis.sizePolicy().hasHeightForWidth())
self.deleteCrisis.setSizePolicy(sizePolicy)
icon2 = QtGui.QIcon()
icon2.addPixmap(QtGui.QPixmap("images/times.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
self.deleteCrisis.setIcon(icon2)
self.deleteCrisis.setIconSize(QtCore.QSize(20, 20))
self.deleteCrisis.setObjectName("deleteCrisis")
self.hl3.addWidget(self.deleteCrisis)
self.verticalLayout.addWidget(self.crisisFrame)
'''