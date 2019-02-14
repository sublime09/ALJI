from math import ceil
from datetime import date
import cutie
import logging as log

logArgs = dict(filemode= 'w',
	filename='pulling.log',
	level=log.DEBUG)
log.basicConfig(**logArgs)


TOTAL_STORIES, PER_PAGE = 543, 15
TOTAL_PAGES = ceil(TOTAL_STORIES / PER_PAGE)
FIRST_PAGE, LAST_PAGE = 1, TOTAL_PAGES
inputNum = cutie.get_number

class Config:
	skipYNPrompts = True
	start, end = FIRST_PAGE, LAST_PAGE
	pagePauseTime = 3.5
	mainFolderOut = "Stories"
	batchFolderOut = str(date.today())
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
	Config.hiddenBrowser = askYN("Hide the browser in the background?")
	log.debug("Manual Configuration Done")
	print("Configuration Complete")
	print("The rest of the program may take a while to run...")
	Config.skipYNPrompts = askYN("Answer Yes to all future prompts?")
