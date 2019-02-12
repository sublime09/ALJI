import lxml
from bs4 import BeautifulSoup

from config import *

def genSoupsFromPageSources(pageSources):
	currPage = Config.start
	endPage = Config.end
	print("Souping page", currPage,"to", endPage, " ... ")
	for pgSource in pageSources:
		logging.debug("Souping page# %s", currPage)
		bigSoup = BeautifulSoup(pgSource, 'lxml')
		logging.info("Souped page# %s", currPage)
		yield bigSoup
		currPage += 1


def genSplitBigSoups(bigSoups):
	cssSelector = 'ul.gallery-works div.writing'
	currEntry = (Config.start-1) * PER_PAGE
	endEntry = Config.end * PER_PAGE
	for bSoup in bigSoups:
		for soup in bSoup.select(cssSelector):
			logging.info("Split soup for entry# %s", currEntry)
			yield soup
			currEntry += 1


def genLinedTextFromSoups(lilSoups):
	currEntry = (Config.start-1) * PER_PAGE
	endEntry = Config.end * PER_PAGE
	for soup in lilSoups:
		if len(soup.text) < 30:
		    logging.warning("len(soup.text) < 30")
		soupLines = soup.findAll(text=True)
		soupLines = [t for t in soupLines if "Comment" not in str(type(t))]
		yield soupLines
		currEntry += 1

