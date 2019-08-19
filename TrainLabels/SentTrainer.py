print("Importing: NLTK...", end='', flush=True)
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
print("Empath...", end='', flush=True)
from empath import Empath
print("Numpy...", end='', flush=True)
# import numpy as np
print("PyPlot...", end='', flush=True)
# import matplotlib.pyplot as plt
print("Pandas...", end='', flush=True)
import pandas as pd
print("Sklearn...", end='', flush=True)
# from sklearn import preprocessing, dummy, svm
# from sklearn import linear_model, neighbors, ensemble
print("ALJI code...", end='', flush=True)
# import fileIO, config
from ModelComparer import ModelComparer
print("Done!")

getEmpathScore = Empath().analyze
lemmatize = WordNetLemmatizer().lemmatize

testStr = "Can it work with. multiple's sentences"
# tokens = word_tokenize(testStr)
# print(tokens)
# print(lemmatize(tokens))

testStr = ''' --- The Fifth Death ---
5. The fifth death and the second death at age fifteen. 
This death occurred in the back of a minivan, parked outside a liquor store at midnight.
I was crying, and so was the ghost of my first death. 
A ghost, 4 years old, chubby arms and tear streaked cheeks. 
Her arms were pinned behind her back as she watched me, as she watched him grab my wrists the same way he grabbed hers. 
She watched me as I was overpowered , as she thought “Maybe love really is like this”. 
As she thought “I didn’t think it was supposed to happen like this, but this is how it’s happening, and it’s happening again, and it happened before, and here it is again. 
So maybe it’s supposed to be like this.” '''
jText = testStr

from textblob import TextBlob

from empath import Empath
emapthScore = Empath().analyze


def main():
	categories = "negative_emotion violence sexual".split()
	# kwargs = {'categories':categories}

	print("\n Using Regex ::::::::")
	sents = toSentences(jText)
	for sent in sents:
		lemmaSent = tokenAndLemma(sent)
		print(sent)
		printEmapths(lemmaSent)

	print("\nUsing Textblob:::::")
	sents = TextBlob(jText).sentences
	for sent in sents:
		if len(sent.words) < 3:
			continue
		lemmaSent = lemmatize_with_postag(sent)
		print(sent)
		printEmapths(lemmaSent)


	return
	


	for sent in toSentences(jText):
		basic = getEmpathScore(sent, normalize=True)
		assert len(basic.keys()) == 194
		ana = getEmpathScore(sent, normalize=True, categories=categories)
		print(sent)
		print("ANA = ", ana)



def printEmapths(text, **kwargs):
	scores = emapthScore(text, normalize=True, **kwargs)
	d = {k:str(int(v*100))+"%" for k,v in scores.items() if v>0}
	dStr = ', '.join([k+":"+v for k,v in d.items()])
	print(dStr)


def lemmatize_with_postag(sent):
	if isinstance(sent, str):
		sent = TextBlob(sent)
	tagDict = dict(J='a', N='n', V='v', R='r')
	words_and_tags = [(w, tagDict.get(pos[0], 'n')) for w, pos in sent.tags]
	lemmatized_list = [word.lemmatize(tag) for word, tag in words_and_tags]
	return " ".join(lemmatized_list)


def toSentences(jText: str):
	import re
	# sentRegex = r"\w[\w'’-]*\s+\w[\w'’-]*[^\.;]*"
	# sentRegex = r"(\w+([’'\-]\w+)?,?\s*)+"
	sentRegex = r"\w[\w'’-]*[\s,]+\w[\w'’-]*[^\.]*"
	matches = re.finditer(sentRegex, jText)
	return [match.group() for match in matches]


def tokenAndLemma(sent: str):
	tokened = word_tokenize(sent)
	lemmaed = ' '.join((lemmatize(w) for w in tokened))
	return lemmaed


def scoreAndSummarize(text):
	'''Main textual analysis flow'''
	scores = getEmpathScore(lemmaed, normalize=True)
	# summation = bigCatsSummation(scores)
	return scores #, summation



if __name__ == '__main__':
	main()