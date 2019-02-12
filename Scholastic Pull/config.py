from math import ceil
from datetime import date
import cutie
import logging

logArgs = dict(filemode= 'w',
	filename='pulling.log',
	level=logging.DEBUG)
logging.basicConfig(**logArgs)


# FOLDER_OUT = "Stories"
# FILE_OUTPUT = "Stories.json"
TOTAL_STORIES, PER_PAGE = 543, 15
TOTAL_PAGES = ceil(TOTAL_STORIES / PER_PAGE)
FIRST_PAGE, LAST_PAGE = 1, TOTAL_PAGES
# PAGE_START, PAGE_END = 1, LAST_PAGE
# SLEEP_START = 1
# SLEEP_PER_PAGE = 3.5
inputNum = cutie.get_number

class Config:
	skipYNPrompts = True
	start, end = FIRST_PAGE+3, 2+3
	pagePauseTime = 3.5
	mainFolderOut = "Stories"
	batchFolderOut = str(date.today())
	jsonOnTheGo = False
	hiddenBrowser = True

def askYN(*args, **kwargs):
	if Config.skipYNPrompts:
		print(*args, "Yes")
		return True
	else:
		return cutie.prompt_yes_or_no(*args, **kwargs)

def doManualConfig():
	args = dict(min_value=1, max_value=TOTAL_PAGES)
	start = inputNum("Page Start?", **args)
	end = inputNum("Page End?", **args)
	Config.start = int(min(start, end))
	Config.end = int(max(start, end))
	Config.pagePauseTime = inputNum("Pause time per page?", min_value=0)
	Config.mainFolderOut = input("Main Folder Name?")
	Config.batchFolderOut = input("Batch Folder Name?")
	Config.jsonOnTheGo = askYN("JSON save intermediate files?")
	Config.hiddenBrowser = askYN("Hide the browser in the background?")
	logging.debug("Manual Configuration Done")
	print("Configuration Complete")
	print("The rest of the program may take a while to run...")
	Config.skipYNPrompts = askYN("Answer Yes to all future prompts?")
