from config import *
import os
import csv
import pandas as pd

dirNameHere = os.path.dirname(__file__)
labelResultsLoc = os.path.join(dirNameHere, "LabelResults")
empathDataLoc = "..?AnalyzeEssays?EssayAnalysisResults?2019-2-4?EmpathAnalysis.csv"
empathDataLoc = empathDataLoc.replace('?', os.path.sep)
# empathDataLoc = os.path.join(empathDataLoc.split('?'))
empathDataLoc = os.path.join(dirNameHere, empathDataLoc)

def getEmpathFrame():
	assert os.path.exists(empathDataLoc)
	empathFrame = pd.read_csv(empathDataLoc)
	filenames = empathFrame.Filename.values
	jNums = [f.split()[0].lstrip("Entry") for f in filenames]
	empathFrame.insert(0, "jNum", pd.Series(jNums))

	# get cols in preferred order
	cols = empathFrame.columns.tolist()
	def colOrder(colName):
		if colName in ["jNum", "Filename"]:
			return 0
		elif "emotion" in colName:
			return 1
		else: 
			return 2
	cols.sort(key=colOrder)
	empathFrame = empathFrame[cols]
	return empathFrame


def getResultFrame():
	csvFiles = list(walkFiles(labelResultsLoc, "csv"))
	lilFrames = [csvToFrame(f) for f in csvFiles]
	bigFrame = pd.concat(lilFrames)
	return bigFrame

def csvToFrame(csvPathAndName):
	csvPath, csvName = csvPathAndName
	# jNum = lrStrip(csvName, "ALJI j#", ".csv")
	jNum = csvName.lstrip("ALJI j#").rstrip(".csv")
	lilFrame = pd.read_csv(csvPath)
	numRows = len(lilFrame['Username'])
	jNumCol = pd.Series([jNum] * numRows)
	lilFrame.insert(0, "jNum", jNumCol.values)
	return lilFrame

def walkFiles(path, ext):
	'''Walks files on a path of a certain file extension'''
	ext = "." + ext.lower()
	for root, dirs, files in os.walk(path):
		for fName in files:
			if fName.lower().endswith(ext):
				fPath = os.path.join(root, fName)
				log.info("Found on walk: %s", fPath)
				yield fPath, fName

def testFileIO():
	print("FileIO Trainer test:")
	limit = 3
	for jNum, result in readResultsGen():
		print("result=", result)
		limit -= 1
		if limit <= 0:
			break

if __name__ == '__main__':
	testFileIO()
