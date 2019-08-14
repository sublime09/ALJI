print("Importing Numpy...", end='', flush=True)
import numpy as np
print("PyPlot...", end='', flush=True)
import matplotlib.pyplot as plt
print("Pandas...", end='', flush=True)
import pandas as pd
print("Sklearn...", end='', flush=True)
from sklearn import preprocessing, model_selection
from sklearn import dummy, svm, linear_model, neighbors, ensemble
print("ALJI code...", end='', flush=True)
import fileIO, config
from ModelComparer import ModelComparer
print("done!")

# TODO: sample weights: 'class_weight' and 'sample_weight' can be used

''' RUNNING OPTIONS FOR MODELS '''
visualizeCGI = True
numAutoLabel = 0 # worse than label spreading?
folds = 5
# scaler = preprocessing.PowerTransformer(copy=False)
scaler = preprocessing.StandardScaler(copy=False)
# scaler = preprocessing.MinMaxScaler(copy=False)

regressors = [
	dummy.DummyRegressor(),
	svm.LinearSVR(),
	svm.SVR(kernel='rbf', gamma='scale'),
	linear_model.Ridge(),
	linear_model.Lasso(),
	linear_model.ElasticNet(),
	ensemble.RandomForestRegressor(), 
	ensemble.GradientBoostingRegressor(), 
	ensemble.AdaBoostRegressor()
]

classifiers = [
	dummy.DummyClassifier(), 
	svm.LinearSVC(), 
	svm.SVC(kernel='rbf', gamma='scale'), 
	neighbors.KNeighborsClassifier(), 
	ensemble.RandomForestClassifier(), 
	ensemble.GradientBoostingClassifier(), 
	ensemble.AdaBoostClassifier()
]

params = dict()
params['C'] = [10**i for i in range(-4, 4)]
params['n_neighbors'] = [2**i for i in range(0, 5)]
params['n_estimators'] = [5**i for i in range(1, 4)]
# params['alpha'] = [i/10.0 for i in range(1, 10)]
# params['epsilon'] = [10**i for i in range(-2, 2)]
# params['degree'] = range(2, 5)
# params['gamma'] = [2**i for i in range(-8, 3)]

def main():
	print("Started Trainer main....")
	resultsFrame = fileIO.getResultFrame()
	print("Read", len(resultsFrame), "Participant results ...")
	empathFrame = fileIO.getEmpathFrame()
	print("Read", len(empathFrame), "Empath analysis results ...")
	empathCols = empathFrame.columns.values[2:]
	assert len(empathCols) == 194
	resultsFrame['color'] = 'blue'

	massFrame = getAutolabels(empathFrame, numAutoLabel)
	if not massFrame.empty:
		resultsFrame = pd.concat((resultsFrame, massFrame), sort=False)

	combFrame = resultsFrame.merge(empathFrame, on='jNum')
	# print(combFrame[['jNum', 'CGI-S', 'Concern Labels']]) # to see contributors

	'''Select target and scale trainers'''
	trainers = combFrame[empathCols]
	scaler.fit(trainers)
	scaler.transform(trainers)
	nSamples, nFeatures = trainers.shape
	target = combFrame['CGI-S'].astype(float)

	mc = tryTrainFor(trainers, target)
	bestModel = mc.getBestModel()
	cgiPredicted = bestModel.predict(trainers)

	'''Plotting / Visualization:'''
	if visualizeCGI:
		y = pd.Series(target, name='True CGI-S')
		x = pd.Series(cgiPredicted, name='Predicted CGI-S')
		colors = combFrame['color']
		plt.grid(which='both')
		scatterPlot(x, y, colors)
		plt.title("N=24, Best model for predicting CGI-S")
		plotTrend(x, y)
	evaulate(combFrame.jNum, target, cgiPredicted)

	resp = input("<Enter> to now target intervene...")

	intervene = combFrame['CGI-S'] > 3 
	target = pd.Series(intervene.astype(int), name='intervene')
	mc = tryTrainFor(trainers, target)

	resp = input("<Enter> to continue to concerns classifiers...")

	concernSents = combFrame['Concern Labels']
	concernFrame = getConcernFrame(concernSents).astype(int)

	for concern in concernFrame.columns:
		target = concernFrame[concern].astype('category')
		if len(set(target.values)) < 2:
			print("Skipped", concern, "due to <2 classes...")
			continue
		mc = tryTrainFor(trainers, target)

	if plt.get_fignums():
		resp = input("Press Enter to close...")
		plt.close()
	print("Done with main")


def tryTrainFor(trainers, target):
	models = classifiers
	scoring = 'balanced_accuracy'
	if 'float' in str(target.dtype):
		models = regressors
		scoring = 'r2'
	mc = ModelComparer(models, params)
	mc.fit(trainers, target, scoring=scoring, cv=folds)
	summary = mc.getModelScores()
	print(summary)
	bestModel = mc.getBestModel()
	print("Best Model for:", target.name, ':')
	print(bestModel)
	score = '''TODO: RETURN SCORE'''
	return mc


def getConcernFrame(concernSents):
	sentColName = concernSents.name
	concernCols = set()
	for sentence in concernSents.values.flatten():
		concernCols.update(sentence.split(';'))
	concernCols.remove('nan')

	concernFrame = pd.DataFrame(concernSents)
	for col in concernCols:
		concernFrame[col] = False

	def intoBooleans(row):
		for label in row[sentColName].split(';'):
			if label in concernCols:
				row[label] = True
		return row
	concernFrame = concernFrame.apply(intoBooleans, axis=1)
	concernFrame = concernFrame.drop(columns=sentColName)
	return concernFrame


def evaulate(jNums, target, predicted):
	evalFrame = pd.DataFrame()
	evalFrame["jNum"] = jNums
	evalFrame["target"] = target
	evalFrame["predicted"] = predicted
	evalFrame["rounded"] = predicted.round().astype(target.dtype)
	numTries = len(evalFrame)
	incorrects = evalFrame.target.ne(evalFrame.rounded)
	incorrects = evalFrame[incorrects]
	numCorrects = numTries - len(incorrects)
	pctCorrect = (100.0 * numCorrects) / numTries
	if not incorrects.empty:
		print("Predictions: %d \t Pct Correct: %.2f%%" % (numTries, pctCorrect))
		print("Some Incorrect Predictions: ", incorrects.tail(7), sep='\n')

	
def getAutolabels(empathFrame, numAutoLabel):
	if numAutoLabel == 0:
		return pd.DataFrame()
	assert numAutoLabel > 0
	cols = "negative_emotion medical_emergency pain anger shame torment".split()
	negSenti = empathFrame[cols].sum(axis=1).sort_values()
	negSenti = negSenti.head(numAutoLabel).index
	happyFrame = empathFrame.iloc[negSenti]

	massFrame = pd.DataFrame()
	massFrame['jNum'] = happyFrame.jNum.values
	massFrame['CGI-S'] = 1
	massFrame['color'] = 'teal'
	return massFrame


def scatterPlot(x, y, colors=None):
	plt.ion() #interactive mode to run in background
	plt.scatter(x=x, y=y, c=colors, s=33)
	plt.xlabel(x.name)
	plt.ylabel(y.name)
	plt.title(x.name + ' versus ' + y.name)
	plt.show()
	plt.pause(0.01)


def plotTrend(x, y):
	trendline = np.poly1d(np.polyfit(x, y, 1))
	newX = [min(x), max(x)]
	plt.plot(newX, trendline(newX), color="orange", lw=1.5)

''' UNUSED '''
def findOutliers(combFrame):
	print("Possible outliers:")
	lowballs = (combFrame['medical_emergency'] / combFrame['CGI-S']) < (0.001/1.3)
	highballs = (combFrame['CGI-S'] / combFrame['medical_emergency']) > (6/0.0025)
	outliers = lowballs | highballs
	print(combFrame[outliers][['jNum', 'Username', 'CGI-S', 'medical_emergency']])

def reduceWithPCA(frame, n_components):
	from sklearn import decomposition
	pca = decomposition.PCA(n_components=n_components)
	pca.fit(frame)
	return pca.transform(trainers)

def printKBestFeatures(trainers, target, k=None):
	from sklearn.feature_selection import SelectKBest
	if k is None:
		k = sqrt(len(trainers.columns))
	selector = SelectKBest(k=k)
	newTrain = selector.fit_transform(trainers, target)
	print("Best features in trainers:")
	print(trainers.columns[selector.get_support()].values)

if __name__ == '__main__':
	main()
