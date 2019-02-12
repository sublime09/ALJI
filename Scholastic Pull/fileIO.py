import os
import json
from config import *

def txtSave(stories):
	outPath = os.path.join(Config.mainFolderOut, Config.batchFolderOut)
	if not os.path.exists(outPath):
		print("Making", outPath, "directory...")
		os.makedirs(outPath)
	print("Saving stories ...", end='')

	currEntry = (Config.start-1) * PER_PAGE
	for story in stories:
		entryStr = "Entry" + str(currEntry).zfill(3)
		filename = entryStr+ ".txt"
		filepath = os.path.join(outPath, filename)
		with open(filepath, 'w', encoding="utf-8") as fileObj:
			fileObj.write(story)
		logging.info("File written: %s", filepath)
		currEntry += 1

	print("Done!")


def jsonReadDict(filePath = None):
	while filePath in (None, ""):
		resp = input("Read what JSON file?:").strip()
		if resp in (None, ""):
			if askYN("Cancel JSON read?"):
				return dict()
		else:
			filePath = resp
	d = None
	print("Reading...", end='')
	with open(filePath, 'r') as fp:
		d = json.load(fp, indent=1)
	print("Done!")
	return d


def jsonSave(obj, filePath=None):
	while filePath in (None, ""):
		resp = input("Save JSON file as?").strip()
		if resp in (None, ""):
			if askYN("Cancel JSON save?"):
				return
		else:
			filePath = resp

	print("Saving", filePath, "...", end='')
	with open(filePath, 'w') as fp:
		json.dump(obj, fp, indent=1)
	print("Done!")
