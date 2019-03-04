from config import *
# from itertools import islice
from fileIO import readEssaysGen, writeEssaysCSV
from Essay import Essay
from empathWork import genScoreEssays


def main():
	unscored = readEssaysGen()
	scored = genScoreEssays(unscored)
	# scored = islice(genScoreEssays(unscored), 20)
	writeEssaysCSV(scored)
	print("Analysis done!")


if __name__ == '__main__':
	main()
