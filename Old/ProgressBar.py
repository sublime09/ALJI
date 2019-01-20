# author Patrick Sullivan
# shows a progress bar in the console for long processes
import sys
from time import time, sleep

def millis():
	return round(time() * 1000)

class ProgressBar:
	pctTemplate = '{:.0%}'
	decimals = 1
	barLength = 30
	tickMS = 2000

	def __init__(self, iterable, name=None):
		self.name = '' if name==None else name+': '
		self.i = 0
		self.iterator = iterable
		self.end = len(iterable)
		self.lastTick = 0

	def __iter__(self):
		return self

	def __next__(self):
		self.i += 1
		if self.lastTick + self.tickMS < millis():
			self.printBar()
		if self.i - 1 < self.end:
			return self.iterator[self.i - 1]
		else:
			raise StopIteration

	def printBar(self, *args):
		done = float(self.i - 1)
		pct = done / (self.end - 1)
		pctStr = self.pctTemplate.format(pct)
		fill = int(pct * self.barLength) * '█'
		empty = (self.barLength - len(fill)) * '-'
		outputs = (self.name, fill, empty, pctStr, *args)
		outTemplate = '\r%s|%s%s| %s' + ' %s'*len(args)
		print(outTemplate % (outputs))
		self.lastTick = millis()
		sys.stdout.flush()

if __name__ == '__main__':
	print("Testing ProgressBar...")
	begin, end = 3, 16
	name = "Test %s-%s"%(begin, end)
	p = ProgressBar(range(begin, end+1), name=name)
	for i in p:
		p.printBar("Test Count=",i)
		sleep(0.1)
	print("Done!")
	