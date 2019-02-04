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

if __name__ == '__main__':
	main()