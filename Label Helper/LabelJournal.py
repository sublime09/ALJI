import FileIO 
from collections import defaultdict

class LabelJournal:
	def __init__(self, jNum):
		self.jNum = jNum
		fileInfo = FileIO.getJFileInfo(jNum)
		self.filePath = fileInfo[0]
		self.fileName = fileInfo[1]
		self.jText = FileIO.readFile(self.filePath)
		self.labels = defaultdict(set)

	def __repr__(self):
		args = ["LabelJournal #" + self.jNum]
		args.append("Labels="+repr(self.labels))
		return '\n'.join(args)
	
	def labelText(self, text, labelName):
		self.labels[labelName].add(text)

	# def unlabelText(self, text, labelName):
	# 	self.labels[labelName].remove(text)

	def delLabel(self, labelName):
		del self.labels[labelName]


