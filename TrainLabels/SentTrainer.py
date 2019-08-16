print("Importing: NLTK...", flush=True, end='')
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
print("Empath...", flush=True, end='')
from empath import Empath
print("Numpy...", end='', flush=True)
import numpy as np
print("PyPlot...", end='', flush=True)
import matplotlib.pyplot as plt
print("Pandas...", end='', flush=True)
import pandas as pd
print("Sklearn...", end='', flush=True)
from sklearn import preprocessing, dummy, svm
from sklearn import linear_model, neighbors, ensemble
print("ALJI code...", end='', flush=True)
# import fileIO, config
from ModelComparer import ModelComparer
print("Done!")

getEmpathScore = Empath().analyze
lemmatize = WordNetLemmatizer().lemmatize

testStr = "Can it work with. multiple's sentences"
tokens = word_tokenize(testStr)
print(tokens)
print(lemmatize(tokens))
exit()


testStr = '''
The fifth death and the second death at age fifteen. 
This death occurred in the back of a minivan, parked outside a liquor store at midnight.
I was crying, and so was the ghost of my first death. 
A ghost, 4 years old, chubby arms and tear streaked cheeks. 
Her arms were pinned behind her back as she watched me, as she watched him grab my wrists the same way he grabbed hers. 
She watched me as I was overpowered , as she thought “Maybe love really is like this.” 
As she thought “I didn’t think it was supposed to happen like this, but this is how it’s happening, and it’s happening again, and it happened before, and here it is again. 
So maybe it’s supposed to be like this.”
'''

import re
sentRegex = r"\w[\w'’-]*\s+\w[\w'’-]*[^\.;]*"
sentRegex2 = r"(\w+([’'\-]\w+)?,?\s*)+"
matches = re.finditer(sentRegex, testStr)
categories = "negative_emotion violence".split()
for match in matches:
	sent = match.group()
	basic = getEmpathScore(sent, normalize=True)
	assert len(basic.keys()) == 194
	ana = getEmpathScore(sent, normalize=True, categories=categories)
	print(sent)
	print("ANA = ", ana)
    
exit()


def main():
	pass


def scoreAndSummarize(text):
	'''Main textual analysis flow'''
	tokened = word_tokenize(text)
	lemmaed = ' '.join((lemmatize(w) for w in tokened))
	scores = getEmpathScore(lemmaed, normalize=True)
	summation = bigCatsSummation(scores)
	return scores, summation


def genScoreEssays(essays):
	for ess in essays:
		log.debug("Scoring file: %s ...", ess.fileName)
		scores, summ = scoreAndSummarize(ess.text)
		ess.empath = scores
		ess.summation = summ
		print("Scored File:", ess.fileName)
		log.info("Scored file: %s", ess.fileName)
		yield ess

if __name__ == '__main__':
	main()