# json stories to txt files
# segmented by newlines
# filename format: ####.txt
	# #### is the submission number from data source

import os
import json
import zipfile


# from ScholasticPull import FILE_OUTPUT as FILE_INPUT
FILE_INPUT = "Stories.json"
FILE_OUTPUT = "Stories.zip"
FOLDER_OUT = "Stories/"

def main():
	print("reading JSON...")
	with open(FILE_INPUT, 'r') as jsonFileObj:
		storiesDict = json.load(jsonFileObj)
		
		if not os.path.exists(FOLDER_OUT):
			print("Making", FOLDER_OUT, "directory...")
			os.makedirs(FOLDER_OUT)

		for subNum, story in storiesDict.items():
			if int(subNum) == 1:
				continue
			filename = subNum.zfill(3) + ".txt"
			with open(FOLDER_OUT + filename, 'w') as txtFileObj:
				print("Type=", type(story))
				txtFileObj.write(story)
				print("Wrote a story!")
				exit()


		# # print(storiesDict["1"])
		# print("Making zip archive...")
		# with Zipfile(FILE_OUTPUT, 'w') as zipOut:
		# 	for subNum, story in storiesDict.items():


def jsonSave(obj):
	print("Saving to", FILE_OUTPUT, "...", end='')
	with open(FILE_OUTPUT, 'w') as fp:
		json.dump(obj, fp, indent=1)
	print("Done!")


def jsonLoad(filepath):
	print("reading json....", end='')
	result = None
	with open(filepath, 'r') as fileObj:
		result = json.load(fileObj)
	if result is None:
		print("Can't read JSON from:", filepath)
	else:
		print("done!")
	return result



def OLDtxtSave(entryNum, story):
	if not os.path.exists(FOLDER_OUT):
		print("Making", FOLDER_OUT, "directory...")
		os.makedirs(FOLDER_OUT)

	entryStr = "Entry" + str(entryNum).zfill(3)
	todayStr = str(date.today())
	filename = entryStr + " " + todayStr + ".txt"
	filepath = FOLDER_OUT + os.path.sep + filename
	print("Saving", filepath, "...", end='')
	with open(filepath, 'w', encoding="utf-8") as fileObj:
		fileObj.write(story)
	print("done")


def OLDiterUrls():
	start = max(PAGE_START, 1)
	end = min(PAGE_END, LAST_PAGE)
	for pageNum in range(start, end+1):
		print("Page #"+str(pageNum), "going to", end)
		fullUrl = urlBegin + str(pageNum) + urlEnd
		yield pageNum, fullUrl

def OLDdriverUrlToSoups(driver, url):
	print("Getting page ... ", end='')
	driver.get(url)
	sleep(SLEEP_PER_PAGE)  # waits for page to load
	print("souping ... ", end='')
	bigSoup = BeautifulSoup(driver.page_source, 'lxml')
	smallSoups = bigSoup.select('ul.gallery-works div.writing')
	print("done!")
	for contentNum in range(len(smallSoups)):
		yield contentNum+1, smallSoups[contentNum]

def OLDmain():	
	soups = {}
	stories = {}
	with getSeleniumDriver() as driver:
		for pageNum, url in iterUrls():
			for contentNum, soup in driverUrlToSoups(driver, url):
				storyNum = (pageNum-1) * PER_PAGE + contentNum
				soups[storyNum] = soup
				story = soupToStory(soup)
				stories[storyNum] = story
				print("Story #"+str(storyNum), end='\t')
				print("has", story.count('\n'), "lines", end='\t')
				print("and is length", len(story))
	print("Selenium Done!")
	stories = doRemovals(stories)
	for num, story in stories.items():
		txtSave(num, story)
	# jsonSave(stories)
	print("ScholasticPull is done!")


if __name__ == '__main__':
	main()