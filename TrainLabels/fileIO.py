''' Basic IO using python's os and config
walking files, reading files, finding files
'''
from config import *
import os

dirNameHere = os.path.dirname(__file__)
labelResultsLoc = os.path.join(dirNameHere, "LabelResults")

def getEmpathLoc():
	empathDataLoc = "..?AnalyzeEssays?EssayAnalysisResults?2019-2-4?EmpathAnalysis.csv"
	empathDataLoc = empathDataLoc.replace('?', os.path.sep)
	# empathDataLoc = os.path.join(empathDataLoc.split('?'))
	empathDataLoc = os.path.join(dirNameHere, empathDataLoc)
	assert os.path.exists(empathDataLoc)
	return empathDataLoc

def getResultLocs():
	return list(walkFiles(labelResultsLoc, "csv"))

def getJText(jNum):
	dateStr = " 2019-2-4"
	journalsFolder = "../Scholastic Pull/Essays/2019-2-4"
	fileBeginning = "Entry"+ str(jNum).zfill(3)
	fileEnd = "txt"
	for fPath, fName in walkFiles(journalsFolder, fileEnd):
		if fName.startswith(fileBeginning):
			return readFile(fPath)
	raise FileNotFoundError("No Journal entry for jNum="+str(jNum))

def walkFiles(path, ext):
	'''Walks files on a path of a certain file extension'''
	ext = ext.lower()
	if '.' not in ext:
		ext = '.' + ext
	for root, dirs, files in os.walk(path):
		for fName in files:
			if fName.lower().endswith(ext):
				fPath = os.path.join(root, fName)
				# log.info("Found on walk: %s", fPath)
				yield fPath, fName

def readFile(filepath):
	assert os.path.exists(filepath)
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

if __name__ == '__main__':
	testFileIO()
