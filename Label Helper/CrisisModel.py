import os
import FileIO
from LabelJournal import LabelJournal


class CrisisModel():
	def __init__(self, groupNum=1):
		# TODO manage group numbers
		jNums = [1, 2, 3]
		self.ljs = [LabelJournal(j) for j in jNums]
		self.taskTotal = len(self.ljs)
		self.taskIndex = 0

	@property
	def taskNum(self):
		return self.taskIndex + 1

	def changeJ(self, amt=1):
		self.taskIndex += amt
		self.taskIndex = self.taskIndex % self.taskTotal

	def nextJ(self):
		self.changeJ(1)
	def prevJ(self):
		self.changeJ(-1)

	def currentText(self):
		i = self.taskIndex
		return self.ljs[i].jText

if __name__ == '__main__':
	c = CrisisModel(1)