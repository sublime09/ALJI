from config import *


def genStoriesFromLinedTexts(linedTexts):
	currEntry = (Config.start-1) * PER_PAGE
	endEntry = Config.end * PER_PAGE
	for lText in linedTexts:
		lines = list(genStripLongBlanks(lText))
		story = '\n'.join(lines)
		numChars = len(story)
		numLines = len(lines)
		if numLines < 3:
			logging.warning("numLines < 3 !!!!")
		if numChars > 45000:
			logging.warning("numChars > 45000  !!!")
		if numChars < 2000:
			logging.warning("numChars < 2000  !!!")
		if len(set(lines)) * 3 < numLines:
			logging.warning("Many duplicate lines in this story!!!")

		fmtStr = "Story #%s is %s lines and %s characters"
		logging.info(fmtStr, currEntry, numLines, numChars)
		yield story
		currEntry += 1


def genStripLongBlanks(storyLines):
	blankLinesInARow = 0
	for line in storyLines:
		line = line.rstrip()
		if len(line) == 0:
			blankLinesInARow += 1
			if blankLinesInARow == 2:
				yield ""
		else:
			yield line
			blankLinesInARow = 0


def genDoRemovals(stories):
	def getSnippet(oneLongStory):
		return ' '.join(oneLongStory[:60].split())

	currEntry = (Config.start-1) * PER_PAGE
	endEntry = Config.end * PER_PAGE
	snippets = set()
	for story in stories:
		snip = getSnippet(story)
		if snip in snippets:
			logging.warning("Deleted DUP: #%s SNIPPET: %s", currEntry, snip)
		else:
			snippets.add(snip)
			yield story
