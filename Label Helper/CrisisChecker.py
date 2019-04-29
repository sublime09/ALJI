
from PyQt5 import QtCore, QtGui, QtWidgets

# QtWidgets.QCheckBox

class CrisisChecker(QWidget):
	''' Custom checkbox and tool for crisis labeling
	'''

	def __init__(self, parent=None, name):
        super(CrisisChecker, self).__init__(parent)
        self.name = name

        cb = QtGui.QCheckBox(self.name)

        delButton = QtWidgets.QToolButton(parent)

        hLayout = QtGui.QHBoxLayout(parent)





# self.CrisisPlaceholderCB = QtWidgets.QCheckBox(LabelingWidget)
# self.CrisisPlaceholderCB.setObjectName("CrisisPlaceholderCB")
# self.CrisisLayout.addWidget(self.CrisisPlaceholderCB)



# retranslate:
# self.CrisisPlaceholderCB.setText(_translate("LabelingWidget", "CheckBox"))


# end:
# QtCore.QMetaObject.connectSlotsByName(LabelingWidget)
