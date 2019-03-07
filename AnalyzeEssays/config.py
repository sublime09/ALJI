import sys
if not hasattr(sys, 'real_prefix'):
	print("WARNING: Not using a virtualenv...")
	prompt = "Continue without activating virtual environment? "
	resp = input(prompt).strip().lower()
	if resp not in "yes y".split():
		print("Exiting...")
		exit()

import cutie
import logging as log
# from inspect import getmembers

askYN = cutie.prompt_yes_or_no

logArgs = dict(filemode= 'w',
	filename='EssayAnalysis.log',
	level=log.DEBUG)
log.basicConfig(**logArgs)


class Config:
	ESSAYS_FOLDER = "../Scholastic Pull/Essays/2019-2-4"
	ANALYSIS_OUTPUT = "./EssayAnalysisResults/2019-2-4/EmpathAnalysis.csv"

