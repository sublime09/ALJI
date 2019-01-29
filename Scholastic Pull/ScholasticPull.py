from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import json
from math import ceil

FILE_OUTPUT = "Stories.json"
TOTAL_STORIES = 543
PER_PAGE = 15
LAST_PAGE = ceil(TOTAL_STORIES / PER_PAGE)
PAGE_START, PAGE_END = 1, 37


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
				if len(story) < 5000:
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
	baseProfile.set_preference("extensions.enabledScopes", 0)  # no addons
	baseProfile.set_preference("extensions.autoDisableScopes", 15)  # no addons
	driver = webdriver.Firefox(baseProfile)
	sleep(.5)  # give a bit of extra time to start up
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
	sleep(4)  # waits for page to load
	print("souping ... ", end='')
	bigSoup = BeautifulSoup(driver.page_source, 'lxml')
	smallSoups = bigSoup.select('ul.gallery-works div.writing')
	print("done!")
	for contentNum in range(len(smallSoups)):
		yield contentNum+1, smallSoups[contentNum]


def soupToStory(smallSoup):
	tags = smallSoup.select('h1,h2,h3,h4,h5,p,span,div')

	def iterTagsToLines(tags):
		emptySpace = 0
		for t in tags:
			line = t.text.strip()
			if line == '<br>' or line == '':
				emptySpace += 1
				if emptySpace == 2:
					yield ''
			else:
				yield line
				emptySpace = 0
	lines = iterTagsToLines(tags)
	story = '\n\t'.join(lines)
	return story


if __name__ == '__main__':
	main()
