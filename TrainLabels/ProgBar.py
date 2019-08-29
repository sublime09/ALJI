''' Shows a progress bar in console'''
''' Author: Patrick Sullivan '''
class ProgBar():
	def __init__(self, it, width=60):
		self.it = list(it)
		self.len = len(self.it)
		self.width = width
		self.progLen = float(width) / self.len
		self.i = 0

	def __iter__(self):
		self.i = 0
		self.show()
		return self

	def __next__(self):
		self.i += 1
		self.show()
		if self.i < self.len:
			return self.it[self.i]
		else: 
			raise StopIteration

	def makeProg(self):
		try:
			return self.__next__()
		except StopIteration as e:
			return 

	def show(self):
		x = int(self.progLen * self.i)
		bar = "#" * x
		empty = "-" * (self.width - x)
		s = "[%s%s] %i/%i\r" % (bar, empty, self.i, self.len)
		end = '' if self.i < self.len else '\n'
		print(s, end=end, flush=True)


if __name__ == '__main__':
	from time import sleep
	print("testing progBar:")
	for i in ProgBar(range(5)):
		sleep(1)
	print("Done!")