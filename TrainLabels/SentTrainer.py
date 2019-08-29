print("Importing Pandas...", end='', flush=True)
import pandas as pd
print("Sklearn...", end='', flush=True)
from sklearn import preprocessing, dummy, svm
from sklearn import linear_model, neighbors, ensemble
print("PyPlot...", end='', flush=True)
import matplotlib.pyplot as plt
print("ALJI code...", end='', flush=True)
from Framing import getFrame, getEmpathCols
from ModelComparer import ModelComparer
print("Done!")

''' RUNNING OPTIONS FOR MODELS '''
visualizeCGI = True
folds = 5
scaler = preprocessing.StandardScaler(copy=False)
# scaler = preprocessing.MinMaxScaler(copy=False)

regressors = [
	dummy.DummyRegressor(),
	svm.LinearSVR(tol=1),
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
	svm.LinearSVC(tol=1), 
	svm.SVC(kernel='rbf', gamma='scale'), 
	neighbors.KNeighborsClassifier(), 
	ensemble.RandomForestClassifier(), 
	ensemble.GradientBoostingClassifier(), 
	ensemble.AdaBoostClassifier()
]

params = dict()
params['C'] = [10**i for i in range(-4, 4)]
params['n_neighbors'] = [2**i for i in range(0, 5)]
params['n_estimators'] = [5**i for i in range(1, 5)]


def main():
	resultsFrame = getFrame("resultsFrame")
	sentFrame = getFrame("sentFrame")
	jNums = resultsFrame.jNum

	combFrame = resultsFrame.merge(sentFrame, on='jNum')
	# print(combFrame[['jNum', 'CGI-S', 'Concern Labels']]) # to see contributors
	
	empathCols = getEmpathCols()
	assert len(empathCols) == 194

	trainers = combFrame[empathCols]
	target = combFrame['CGI-S'].astype(float)

	# from sklearn.datasets import load_boston, load_diabetes
	# dataset = load_boston()
	# trainers = dataset.data
	# target = dataset.target

	scaler.fit(trainers)
	scaler.transform(trainers)
	nSamples, nFeatures = trainers.shape

	mc = tryTrainFor(trainers, target)
	bestModel = mc.getBestModel()
	cgiPredicted = bestModel.predict(trainers)

	'''Plotting / Visualization:'''
	if True:
		y = pd.Series(target, name='True boston')
		x = pd.Series(cgiPredicted, name='Predicted boston')
		# colors = combFrame['color']
		plt.grid(which='both')
		scatterPlot(x, y)
		title = "Sentence Segmented, N=%s, Best Model"
		title = title % (len(target))
		plt.title(title)

	print("Enter 'c' to continue or 'q' to quit")
	breakpoint()

	intervene = combFrame['CGI-S'] > 3 
	target = pd.Series(intervene.astype(int), name='intervene')
	mc = tryTrainFor(trainers, target)

	print("Enter 'c' to continue or 'q' to quit")
	breakpoint()

	if plt.get_fignums():
		plt.close()
	print("Done with main")


def tryTrainFor(trainers, target):
	doClass = 'float' not in str(target.dtype)
	models = classifiers if doClass else regressors
	scoring = 'balanced_accuracy' if doClass else 'r2'
	mc = ModelComparer(models, params)
	mc.fit(trainers, target, scoring=scoring, cv=folds)
	summary = mc.getModelScores()
	print(summary)
	bestModel = mc.getBestModel()
	print("Best Model for:", target.name, ':')
	print(bestModel)
	'''TODO: RETURN SCORE'''
	return mc

def scatterPlot(x, y, colors=None):
	plt.ion() #interactive mode to run in background
	plt.scatter(x=x, y=y, c=colors, s=33)
	plt.xlabel(x.name)
	plt.ylabel(y.name)
	plt.title(x.name + ' versus ' + y.name)
	plt.show()
	plt.pause(0.01)

def plotTrend(x, y):
	import numpy as np
	trendline = np.poly1d(np.polyfit(x, y, 1))
	newX = [min(x), max(x)]
	plt.plot(newX, trendline(newX), color="orange", lw=1.5)

if __name__ == '__main__':
	main()