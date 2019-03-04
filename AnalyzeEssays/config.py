import cutie
import logging as log
# from inspect import getmembers

askYN = cutie.prompt_yes_or_no

if not hasattr(sys, 'real_prefix'):
	print("Venv")
	if askYN("WARN: Venv is not running. Cancel?"):
		exit()

logArgs = dict(filemode= 'w',
	filename='EssayAnalysis.log',
	level=log.DEBUG)
log.basicConfig(**logArgs)


class Config:
	ESSAYS_FOLDER = "../Scholastic Pull/Essays/2019-2-4"
	ANALYSIS_OUTPUT = "./EssayAnalysisResults/2019-2-4/EmpathAnalysis.csv"

