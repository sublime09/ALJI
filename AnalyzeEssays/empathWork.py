from config import *
from empath import Empath
from Essay import Essay
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

empathScore = Empath().analyze
# Examples of adjusting the empathLexicon:
# empathLexicon.delete_category("ocean")
# print("Categories = ", empathLexicon.cats.keys())
lemmatize = WordNetLemmatizer().lemmatize

def scoreAndSummarize(text):
	'''Main textual analysis flow'''
	tokened = word_tokenize(text)
	lemmaed = ' '.join((lemmatize(w) for w in tokened))
	scores = empathScore(lemmaed, normalize=True)
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


def bigCatsSummation(scores):
	nonZero = {k: v for k, v in scores.items() if v > 0}
	sortScores = sorted(nonZero.items(), key=lambda kv: kv[1])
	rounded = {k: round(v, 6) for k, v in sortScores[:5]}
	return str(rounded)


if __name__ == '__main__':
	print("empathWork Test:")
	tests = """Today is a great day. 
		The seas are choppy today. 
		The sea is choppy today. 
		The pain is too much. """
	tests = [t.strip() for t in tests.split('\n')]
	for sent in tests:
		if sent in [None, ""]:
			continue
		print("   Scoring sentence:", repr(sent))
		scores, summ = scoreAndSummarize(sent)
		print(summ)
