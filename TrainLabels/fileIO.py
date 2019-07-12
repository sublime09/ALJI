from config import *
import os
import json

labelResultsFolder = "LabelResults"

def readResultsGen():
	for fPath, fName in walkResultLabelFiles():
		oneResults = readJSON(fPath)
		oneResults['filename'] = fName
		fPath = fPath.replace('/', os.path.sep)
		pathSplit = fPath.split(os.path.sep)
		oneResults['labeler'] = pathSplit[1]
		gStr = pathSplit[2].replace("Labels.json", "")
		gNum = int(gStr.replace("Group", ""))
		oneResults['group'] = gNum
		yield oneResults

def readJSON(filepath):
	log.info("Reading JSON: %s", filepath)
	with open(filepath, 'r', encoding="UTF-8") as fp:
		return json.load(fp) #, indent=2)

def walkResultLabelFiles():
	walkPath = os.path.join(labelResultsFolder)
	log.info("Walking JSONs on path: %s", walkPath)
	for root, dirs, files in os.walk(walkPath):
		for fName in files:
			if not fName.endswith(".json"):
				continue
			fPath = os.path.join(root, fName)
			yield fPath, fName

def readEssaysGen():
	for fPath, fName in walkEssayFiles():
		story = readFile(fPath)
		yield Essay(fName, story)

def writeEssaysCSV(essays):
	csvLines = []
	for ess in essays:
		if len(csvLines) == 0:
			csvLines.append(','.join(ess.genColNames()))
		csvLines.append(','.join(ess.genRowValues()))
	csvLines = '\n'.join(csvLines)
	writeFile(Config.ANALYSIS_OUTPUT, csvLines)


def walkEssayFiles():
	walkPath = os.path.join(Config.ESSAYS_FOLDER)
	log.info("Walking Essays on path: %s", walkPath)
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
	print("FileIO Trainer test:")
	limit = 3
	for resultD in readResultsGen():
		piece = str(resultD)[:80]
		print("Piece = ", piece)
		limit -= 1
		if limit <= 0:
			break
