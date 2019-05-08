import os
import json
import FileIO
from MarkedJournal import MarkedJournal

mostNegEmo = '''437 341 068 278 510 041 366 472 238 188 
270 309 294 408 357 426 381 299 156 010 522 473 345 
213 150 543 125 069 053 031 456 239 542 502 453 428 
480 245 088 527 460 215 124 404 248 040 535 395 283 
081 176 287 149 233 135 499 143 103 429 011 402 250 
180 524 298 360 219 541 383 120 412 377 501 359 094 
027 446 371 386 073 138 264 115 521 225 005 517 450 
486 368 070 423 530 485 332 243 285 493 018 021 '''
mostNegEmo = [int(s) for s in mostNegEmo.split()]
numGroups = 16

class JournalGroup():
	@staticmethod
	def fromJSON(jsonObj):
		if isinstance(jsonObj, str):
			jsonObj = json.loads(jsonObj)
		groupNum = jsonObj['group'] + 1
		marksJSON = jsonObj['marks']
		marks = [MarkedJournal.fromJSON(j) for j in marksJSON]
		return JournalGroup(groupNum, marks)

	def __init__(self, groupNum, marks=None):
		self.group = groupNum - 1
		self.marks = marks
		self.task = 0
		if self.marks is None:
			oldSave = FileIO.readJournalGroup(groupNum)
			if oldSave is not None:
				jsonObj = json.loads(oldSave)
				assert self.group == jsonObj['group']
				marksJSON = jsonObj['marks']
				self.marks = [MarkedJournal.fromJSON(j) for j in marksJSON]
		if self.marks is None:
			jNums = mostNegEmo[self.group::numGroups]
			self.marks = [MarkedJournal.fromJNum(j) for j in jNums]
		# self.startAutoSave()

	# def startAutoSave(self):
	# 	self.save()
	# 	Timer(10, self.startAutoSave).start()

	@property
	def groupNum(self):
		return self.group + 1

	@property
	def taskNum(self):
		return self.task + 1

	@property
	def taskTotal(self):
		return len(self.marks)
	
	def changeJ(self, amt):
		self.task = (self.task + amt) % len(self.marks)

	def nextJ(self):
		self.changeJ(1)
	def prevJ(self):
		self.changeJ(-1)

	@property
	def currentMark(self):
		return self.marks[self.task]

	def getCurrentText(self):
		return self.currentMark.jText

	def toJSON(self, indent=None):
		d = lambda o: o.__dict__
		return json.dumps(self, indent=indent, default=d)

	def save(self):
		jsonStr = self.toJSON()
		FileIO.writeJournalGroup(self.groupNum, jsonStr)

	def __str__(self):
		return 'CrisisModel group#' + str(self.groupNum)

	def __repr__(self):
		return "%s(%r)" % (self.__class__.__qualname__, self.__dict__)

if __name__ == '__main__':
	c = JournalGroup(1)
	print("Using:", repr(c))
	print("Snippet: ", c.getCurrentText()[:60])
	c.currentMark.newLabel("dispair")
	jsonStr = c.toJSON(indent=None)
	# print("\nJSON Printed:", jsonStr[:100])
	c.save()
	d = JournalGroup.fromJSON(jsonStr)
	assert d.group == 0
	