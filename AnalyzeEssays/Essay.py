from config import *

class Essay:
	def __init__(self, fileName, text):
		self.fileName = fileName
		self.text = text
		self.empath = None
		self.summation = None

	def __repr__(self):
		args = ["File: " + self.fileName]
		args.append("Excerpt: "+ self.text[:30])
		args.append("Categories: " + str(self.summation))
		return '\n'.join(args)

	def genColNames(self):
		yield "Filename"
		for cat, score in self.empath.items():
			yield str(cat)

	def genRowValues(self):
		yield self.fileName
		for cat, score in self.empath.items():
			yield str(score)
		