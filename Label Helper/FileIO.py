import os

def readEssaysGen():
	for fPath, fName in walkEssayFiles():
		story = readFile(fPath)
		# yield Essay(fName, story)
		yield None

def walkJournalsGen(startPath):
	walkPath = os.path.join(startPath)
	# log.info("Walking Journals on path: %s", walkPath)
	for root, dirs, files in os.walk(walkPath):
		for fName in files:
			if not fName.startswith("Entry"):
				continue
			if not fName.endswith(".txt"):
				continue
			fPath = os.path.join(root, fName)
			yield fPath, fName


def readFile(filepath):
	fileText = None
	log.info("Reading File: %s", filepath)
	with open(filepath, 'r', encoding="UTF-8") as file:
		fileText = file.read()
	return fileText


def writeFile(filepath, content):
	log.info("Writing File: %s", filepath)
	print("Output file:", filepath)
	dirPath, fileName = os.path.split(filepath)
	os.makedirs(dirPath, exist_ok=True)
	with open(filepath, 'w', encoding="UTF-8") as file:
		file.write(content)

if __name__ == '__main__':
	print("FileIO Essays test:")
	from itertools import islice
	for fName, story in islice(genEssayFiles(), 3):
		print("Excerpt from:", fName)
		print("  ", story[:60].replace("\n", " "), "...")
