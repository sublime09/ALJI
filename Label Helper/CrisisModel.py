import os
import FileIO
from LabelJournal import LabelJournal

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

class CrisisModel():
	def __init__(self, groupNum=1):
		gIndex = groupNum - 1
		jNums = mostNegEmo[gIndex::numGroups]
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