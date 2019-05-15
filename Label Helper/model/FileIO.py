import sys
import os

cwd = os.getcwd()
realFile = os.path.realpath(__file__)
dir_path = os.path.dirname(realFile)
dir_fake_path = os.path.dirname(__file__)
basePaths = [cwd, dir_path, dir_fake_path]
upPaths = [os.path.dirname(p) for p in basePaths]
upUpPaths = [os.path.dirname(p) for p in upPaths]

maybePaths = basePaths + upPaths + upUpPaths

journalsFolder = "Journals"
resultsFilespath = os.path.join(cwd, "LabelResults")
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
	fName = os.path.join(journalsFolder, fName)

	for onePath in maybePaths:
		fPath = os.path.join(onePath, fName)
		if os.path.isfile(fPath):
			print("FILE FOUND: " + str(fPath), file=sys.stderr)
			return readFile(fPath)
		else:
			print("Could not find file: " + str(fPath), file=sys.stderr)
	raise FileNotFoundError(fName)

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
