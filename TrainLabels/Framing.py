import pandas as pd
from textblob import TextBlob
import fileIO

def main():
	js = [522, 64]
	getJournalsFrame(js)
	frame = getSentenceFrame(js)
	for sent in frame.sent:
		print(sent)

def getEmpathFrame():
	emapthLoc = fileIO.getEmpathLoc()
	empathFrame = pd.read_csv(empathLoc)
	filenames = empathFrame.Filename.values
	jNums = [f.split()[0].lstrip("Entry") for f in filenames]
	empathFrame.insert(1, "jNum", pd.Series(jNums))
	# get cols in preferred order
	cols = empathFrame.columns.tolist()
	def colOrder(colName):
		if colName in ["jNum", "Filename"]:
			return 0
		else: 
			return 2
	cols.sort(key=colOrder)
	empathFrame = empathFrame[cols]
	return empathFrame


def getJournalsFrame(jNums):
	data = dict(jNum=jNums)
	data['jTexts'] = [fileIO.getJText(j) for j in jNums]
	frame = pd.DataFrame(data=data)
	return frame
	# insert flatCGI, slantCGI, rampCGI ?

def getSentenceFrame(jNums):
	jTexts = [fileIO.getJText(j) for j in jNums]
	data = dict(jNum=[], sNum=[], sent=[])
	for jNum, jText in zip(jNums, jTexts):
		jText.replace(".\"", ". \"")
		jText.replace("\n", " ")
		numWords = len(sent.words)
		if numWords > 100:
			print("long sentence:", sent, sep='\n')
			resp = input("continue?")
		for sNum, sent in enumerate(TextBlob(jText).sentences):
			data['jNum'].append(jNum)
			data['sNum'].append(sNum)
			data['numWords'].append(numWords)
			data['sent'].append(str(sent))
	return pd.DataFrame(data=data)

def getResultFrame():
	csvFiles = fileIO.getResultLocs()
	lilFrames = (csvToFrame(f) for f in csvFiles)
	lilFrames = (f for f in lilFrames if not f.empty)
	bigFrame = pd.concat(lilFrames)
	for colName in ['Concern Labels', 'Custom Concern Labels']:
		bigFrame[colName] = bigFrame[colName].astype(str)
	return bigFrame

def csvToFrame(csvPathAndName):
	csvPath, csvName = csvPathAndName
	jNum = csvName.lstrip("ALJI j#").rstrip(".csv")
	# print("Reading:", csvPath)
	lilFrame = pd.read_csv(csvPath)
	numRows = len(lilFrame.index)
	jNumCol = pd.Series([jNum] * numRows)
	lilFrame.insert(0, "jNum", jNumCol.values)
	return lilFrame

if __name__ == '__main__':
	main()