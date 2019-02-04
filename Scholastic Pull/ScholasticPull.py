from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import json
from math import ceil


FILE_OUTPUT = "Stories.json"
TOTAL_STORIES = 543
PER_PAGE = 15
LAST_PAGE = ceil(TOTAL_STORIES / PER_PAGE)
PAGE_START, PAGE_END = 1, LAST_PAGE
# PAGE_ITER = range(0+1, LAST_PAGE+1)
SLEEP_START = 1
SLEEP_PER_PAGE = 6


def main():
	soups = {}
	stories = {}
	with getSeleniumDriver() as driver:
		for pageNum, url in iterUrls():
			for contentNum, soup in driverUrlToSoups(driver, url):
				storyNum = (pageNum-1) * PER_PAGE + contentNum
				soups[storyNum] = soup
				story = soupToStory(soup)
				stories[storyNum] = story
				print("Story #"+str(storyNum), "is length", len(story))
				if len(story) < 500:
					input("CAUTION Press enter to continue....")
	print("Selenium Done!")
	stories = doRemovals(stories)
	jsonSave(stories)
	print("ScholasticPull is done!")


def doRemovals(stories):
	# removes too small stories
	stories = {k: v for k, v in stories.items() if len(v.strip()) > 500}

	def getSnippet(story):
		return ' '.join(story[:60].split())

	snippets = set()
	uniqueStories = {}
	for num, story in stories.items():
		snip = getSnippet(story)
		if snip not in snippets:
			snippets.add(snip)
			uniqueStories[num] = story

	for num in stories:
		if num not in uniqueStories:
			print("Deleted DUP:", num, ":", getSnippet(stories[num]))
	return uniqueStories


def jsonSave(obj):
	print("Saving to", FILE_OUTPUT, "...", end='')
	with open(FILE_OUTPUT, 'w') as fp:
		json.dump(obj, fp, indent=1)
	print("Done!")


def getSeleniumDriver():
	print("Starting Selenium...", end='')
	baseProfile = webdriver.FirefoxProfile()
	# no addons
	baseProfile.set_preference("extensions.enabledScopes", 0)
	baseProfile.set_preference("extensions.autoDisableScopes", 15)
	driver = webdriver.Firefox(baseProfile)
	sleep(SLEEP_START)  # give a bit of extra time to start up
	print("done!")
	return driver


def iterUrls():
	urlBegin = "https://www.artandwriting.org/explore/online-galleries/#subset="
	urlEnd = "&writing=Personal+Essay%2FMemoir&art_portfolio=false&writing_portfolio=false&year=0&state=All&awards=All&grade=12"
	start = max(PAGE_START, 1)
	end = min(PAGE_END, LAST_PAGE)
	for pageNum in range(start, end+1):
		print("Page #"+str(pageNum), "going to", end)
		fullUrl = urlBegin + str(pageNum) + urlEnd
		yield pageNum, fullUrl


def driverUrlToSoups(driver, url):
	print("Getting page ... ", end='')
	driver.get(url)
	sleep(SLEEP_PER_PAGE)  # waits for page to load
	print("souping ... ", end='')
	bigSoup = BeautifulSoup(driver.page_source, 'lxml')
	smallSoups = bigSoup.select('ul.gallery-works div.writing')
	print("done!")
	for contentNum in range(len(smallSoups)):
		yield contentNum+1, smallSoups[contentNum]


def soupToStory(smallSoup):
	soupLines = smallSoup.findAll(text=True)
	storyLines = [a for a in soupLines if a not in ['', '\n']]
	storyText = '\n'.join(storyLines)

	noSoup = len(smallSoup.text) < 30
	fewLines = len(storyLines) < 3
	longStory = len(storyText) > 50000
	
	if noSoup or fewLines or longStory:
		print("Bad story!!!! noSoup, fewLines, longStory =", noSoup, fewLines, longStory)
		import pdb; pdb.set_trace()

	duplicates = len(storyLines) == len(set(storyLines))
	if duplicates:
		print("Duplicate lines found!!!!")
		import pdb; pdb.set_trace()

	return storyText


if __name__ == '__main__':
	main()
