from config import *
from seleniumWork import genPageSourcesFromWeb
from soupWork import genSoupsFromPageSources, \
		genSplitBigSoups, genLinedTextFromSoups
from storyWork import genStoriesFromLinedTexts, genDoRemovals
from fileIO import jsonSave, jsonReadDict, txtSave

def main():
	if not askYN("Do everything using defaults?"):
		doManualConfig()
	webPages = None
	bigSoups = None
	lilSoups = None
	texts = None
	stories = None

	if askYN("Use Selenium to fetch page soups?"):
		webPages = genPageSourcesFromWeb()
	if askYN("Convert page sources into Big Soups?"):
		bigSoups = genSoupsFromPageSources(webPages)
	if askYN("Split pageSoups into storySoups?"):
		lilSoups = genSplitBigSoups(bigSoups)
	if askYN("Convert Soups to Text ?"):
		linedTexts = genLinedTextFromSoups(lilSoups)
	if askYN("Convert Texts to Stories?"):
		stories = genStoriesFromLinedTexts(linedTexts)
	if askYN("Remove any duplicate stories detected?"):
		uniques = list(genDoRemovals(stories))
		stories = uniques

	if askYN("Save Stories to folder as .txt files?"):
		txtSave(stories)
	return 0


if __name__ == '__main__':
	main()
