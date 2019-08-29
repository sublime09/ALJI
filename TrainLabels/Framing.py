print("Importing: Pandas...", end='', flush=True)
import pandas as pd
print("Empath...", end='', flush=True)
from empath import Empath
print("TextBlob...", end='', flush=True)
from textblob import TextBlob
print("ALJI code...", end='', flush=True)
import fileIO
from ProgBar import ProgBar
print("Done!")

def getFrame(frameName):
	filename = "Frames/" + frameName + ".pickle"
	return pd.read_pickle(filename)

def getEmpathCols():
	return list(Empath().analyze("").keys())

def main():
	print("Framing resultsFrame...")
	resultsFrame = getResultFrame()
	resultsFrame.to_pickle("Frames/journalFrame.pickle")
	jNums = resultsFrame.jNum

	print("Framing journalFrame...")
	journalFrame = getJournalFrame(jNums)
	journalFrame.to_pickle("Frames/journalFrame.pickle")

	print("Framing sentFrame...")
	sentFrame = getSentenceFrame(jNums)
	sentFrame.to_pickle("Frames/sentFrame.pickle")


def getJournalFrame(jNums):
	data = dict(jNum=jNums)
	jTexts = [fileIO.getJText(j) for j in jNums]
	data['jText'] = jTexts
	frame = pd.DataFrame(data=data)
	frame = appendEmpath(frame, targetCol='jText')
	return frame

# TODO: flatCGI, slantCGI, rampCGI ?
def getSentenceFrame(jNums):
	sentColName = 'sent'
	jTexts = [fileIO.getJText(j) for j in jNums]
	data = dict(jNum=[], sNum=[], numWords=[], sent=[])
	for jNum, jText in ProgBar(zip(jNums, jTexts)):
		jText = jText.replace("\\n", '\n')
		jText = jText.replace("\\t", '\t')
		jText = jText.replace('."', '. "')
		jText = jText.replace('.”', '. ”')
		jText = jText.replace('.`', '. `')
		jText = jText.replace('\xa0', ' ')
		jText = jText.replace("\n", " ")
		for sNum, sent in enumerate(TextBlob(jText).sentences):
			numWords = len(sent.words)
			if numWords > 100:
				print("WARNING: long sentence:", sent, sep='\n')
				breakpoint()
			data['jNum'].append(jNum)
			data['sNum'].append(sNum)
			data['numWords'].append(numWords)
			data[sentColName].append(str(sent))
	sFrame = pd.DataFrame(data=data)
	sFrame = appendEmpath(sFrame, targetCol='sent')
	return sFrame


def appendEmpath(frame, targetCol):
	assert targetCol in frame.columns
	empathScore = Empath().analyze
	tagDict = dict(J='a', N='n', V='v', R='r')

	pBar = ProgBar(range(len(frame) + 1))
	def scoreRow(row):
		pBar.makeProg()
		tb = TextBlob(row[targetCol])
		# USING POS_TAG + LEMMATIZE
		words_and_tags = [(w, tagDict.get(pos[0], 'n')) for w, pos in tb.tags]
		lemmatized_list = [word.lemmatize(tag) for word, tag in words_and_tags]
		lemmaSent = " ".join(lemmatized_list)
		scored = empathScore(lemmaSent, normalize=True)
		row = row.append(pd.Series(data=scored))
		return row
	# APPEND EMPATHS COLUMNS TO FRAME
	print("Doing empath on", len(frame), "rows...")
	frame = frame.apply(scoreRow, axis='columns')
	return frame	

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
	lilFrame = pd.read_csv(csvPath)
	numRows = len(lilFrame.index)
	jNumCol = pd.Series([jNum] * numRows)
	lilFrame.insert(0, "jNum", jNumCol.values)
	return lilFrame

def test():
	print('doing Framing test()...')
	js = [522, 64]
	frame = getJournalFrame(js)
	print("Journal Frame:")
	print(frame)
	resp = input("Continue to sentence frame?")
	frame = getSentenceFrame(js)
	print("Sentence Frame:")
	print(frame)

if __name__ == '__main__':
	main()
	# test()
