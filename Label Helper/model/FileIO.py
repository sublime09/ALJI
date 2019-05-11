import os

dirname = os.path.dirname(__file__)
journalsFilepath = os.path.join(dirname, "..", "Journals")
resultsFilespath = os.path.join(dirname, "..", "LabelResults")
dateStr = " 2019-02-04"

def writeJournalGroup(groupNum, contents):
	fName = "Group%sLabels.json" % (groupNum)
	fPath = os.path.join(resultsFilespath, fName)
	writeFile(fPath, contents)

def readJournalGroup(groupNum):
	fName = "Group%sLabels.json" % (groupNum)
	fPath = os.path.join(resultsFilespath, fName)
	if os.path.isfile(fPath):
		return readFile(fPath)
	return None

def readJTextForJNum(jNum):
	entryStr = "Entry" + str(jNum).zfill(3)
	fName = entryStr + dateStr + ".txt"
	fPath = os.path.join(journalsFilepath, fName)
	return readFile(fPath)

def walkJournalsGen():
	walkPath = os.path.join(journalsFilepath)
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
	with open(filepath, 'r', encoding="UTF-8") as file:
		fileText = file.read()
	return fileText


def writeFile(filepath, content):
	print("Writing file:", filepath)
	dirPath, fName = os.path.split(filepath)
	os.makedirs(dirPath, exist_ok=True)
	with open(filepath, 'w', encoding="UTF-8") as file:
		file.write(content)
