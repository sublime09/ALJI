import os
import FileIO

journalsFilepath = ".\\Journals"

class CrisisModel():

	def __init__(self):
		self.jFiles = list()



		for root, d, files in os.walk(journalsFilepath):
			for fname in files:
				path = os.path.join(root, fname)
				self.jFiles.append(path)

				print("Reading from:", path)

				with open(path, 'r', encoding="UTF-8") as f:
					out = f.read()
					print(out)

				break

	def getEssay(num):
		return "THIS SHOULD BE ESSAY#" + num




if __name__ == '__main__':
	c = CrisisModel()