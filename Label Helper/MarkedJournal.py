import FileIO 
import json

defaultCrises = "Depression Self-Harm Grief".split()

# @dataclass
# class Label:
# 	name: str 
# 	# text: str = "" # may add later
# 	checked: bool = False

# 	def toggle(self):
# 		self.checked = not self.checked

# @dataclass
class MarkedJournal:
	def __init__(self, jNum: int, jText: str, labels=None):
		self.jNum = jNum
		self.jText = jText
		if labels is None:
			labels = {n:False for n in defaultCrises}
		self.labels = labels

	@staticmethod
	def fromJSON(jsonObj):
		if isinstance(jsonObj, str):
			jsonObj = json.loads(jsonObj)
		return MarkedJournal(**jsonObj)

	@staticmethod
	def fromJNum(jNum):
		text = FileIO.readJTextForJNum(jNum)
		return MarkedJournal(jNum, text)

	def newLabel(self, name, checked=False):
		self.labels[name] = checked
	def toggleLabel(self, name):
		self.labels[name] = not self.labels[name]
		print(name, "is now", self.labels[name])
	def delLabel(self, name):
		del self.labels[name]

	def toJSON(self, indent=None):
		return json.dumps(self.__dict__, indent=indent)

	def __repr__(self):
		qName = self.__class__.__qualname__
		reprDict = {k:d for k,d in self.__dict__.items() if k != "jText"}
		return "%s(%r)" % (qName, reprDict)

if __name__ == '__main__':
	mj = MarkedJournal(1, "test jText")
	mj.toggleLabel("Depression")
	print(mj)
	jsonStr = mj.toJSON()
	print(jsonStr)
	jsonObj = json.loads(jsonStr)
	print(jsonObj)
	oj = MarkedJournal.fromJSON(jsonStr)
	print(oj)
