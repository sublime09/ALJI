import os

journalsFilepath = ".\\Journals"

def getJFileInfo(jNum):
	fileStart = "Entry" + str(jNum).zfill(3)
	for fPath, fName in walkJournalsGen():
		if fName.startswith(fileStart):
			return fPath, fName
	throw("can't find journal starting with: "+fileStart)


def walkJournalsGen():
	walkPath = os.path.join(journalsFilepath)
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
	# log.info("Reading File: %s", filepath)
	with open(filepath, 'r', encoding="UTF-8") as file:
		fileText = file.read()
	return fileText


def writeFile(filepath, content):
	# log.info("Writing File: %s", filepath)
	print("Output file:", filepath)
	dirPath, fileName = os.path.split(filepath)
	os.makedirs(dirPath, exist_ok=True)
	with open(filepath, 'w', encoding="UTF-8") as file:
		file.write(content)
