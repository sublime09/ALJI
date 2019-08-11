print("Importing Numpy...", end='', flush=True)
import numpy as np
print("PyPlot...", end='', flush=True)
import matplotlib.pyplot as plt
print("Pandas...", end='', flush=True)
import pandas as pd
print("Sklearn...", end='', flush=True)
from sklearn import preprocessing, model_selection
from sklearn import dummy, svm, linear_model, ensemble
print("ALJI code...", end='', flush=True)
import fileIO, config
from ModelComparer import ModelComparer
print("done!")

# TODO: Label Propagation NAH
# TODO: sample weights: 'class_weight' and 'sample_weight' can be used

# baseModel = svm.LinearSVC()    # NEEDED?

''' RUNNING OPTIONS FOR MODELS '''
visualizeCGI = False
labelSpreadingAlpha = None
numAutoLabel = 0 # worse than label spreading?
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
	ensemble.GradientBoostingRegressor()
]

params = dict()
params['C'] = [10**i for i in range(-4, 4)]
# params['alpha'] = [i/10.0 for i in range(1, 10)]
params['n_estimators'] = [5**i for i in range(1, 5)]
# params['epsilon'] = [10**i for i in range(-2, 2)]
# params['degree'] = range(2, 5)
# params['gamma'] = [2**i for i in range(-8, 3)]


def main():
	print("Started Trainer main....")
	resultsFrame = fileIO.getResultFrame()
	print("Read", len(resultsFrame.index), "Participant results ...")
	empathFrame = fileIO.getEmpathFrame()
	print("Read", len(empathFrame.index), "Empath analysis results ...")
	empathCols = empathFrame.columns.values[2:]
	assert len(empathCols) == 194
	resultsFrame['color'] = 'blue'

	massFrame = getAutolabels(empathFrame, numAutoLabel)
	if massFrame is not None and not massFrame.empty:
		print("concating ")
		resultsFrame = pd.concat((resultsFrame, massFrame), sort=False)

	combFrame = resultsFrame.merge(empathFrame, on='jNum') # WORKs GOOD
	combFrame['intervene'] = combFrame['CGI-S'] > 3

	# print(combFrame[['jNum', 'CGI-S', 'Concern Labels']]) # to see contributors

	concernCols = set()
	for sentence in combFrame['Concern Labels'].values.flatten().astype(str):
		concernCols.update(sentence.split(';'))
	concernCols.remove('nan')
	# print(concernCols)
	for col in concernCols:
		pass ''' TODO: binary classifiers for concern labels'''
		

	'''Plotting / Visualization:'''
	if visualizeCGI:
		x = combFrame['medical_emergency']
		y = combFrame['CGI-S']
		colors = combFrame['color']
		plt.ion() #interactive mode to run in background
		scatterPlot(x, y, colors)
		plotTrend(x, y)
		return

	'''Select target and scale trainers'''
	target = combFrame['CGI-S'].astype('int')
	trainers = combFrame[empathCols]
	scaler.fit(trainers)
	scaler.transform(trainers)

	mc = ModelComparer(regressors, params)
	mc.fit(trainers, target, cv=5, scoring='r2')
	summary = mc.getModelScores()
	print(summary)
	name, bestModel = mc.getBestModel()
	print("Best Model:", bestModel, sep='\n')

	predicted = bestModel.predict(trainers)

	'''Evaluate: '''
	evalFrame = pd.DataFrame()
	evalFrame["jNum"] = combFrame.jNum
	evalFrame["target"] = target
	evalFrame["predicted"] = predicted
	evalFrame["rounded"] = predicted.round().astype(target.dtype)
	numTries = len(evalFrame.index)
	incorrects = evalFrame.target.ne(evalFrame.rounded)
	incorrects = evalFrame[incorrects]
	numCorrects = numTries - len(incorrects.index)
	pctCorrect = (100.0 * numCorrects) / numTries
	if not incorrects.empty:
		print("Predictions: %d \t Pct Correct: %.2f%%" % (numTries, pctCorrect))
		print("Some Incorrect Predictions: ", incorrects.tail(7), sep='\n')

	
def getAutolabels(empathFrame, numAutoLabel):
	if numAutoLabel == 0:
		return None
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
	plt.scatter(x=x, y=y, c=colors, s=8)
	plt.xlabel(x.name)
	plt.ylabel(y.name)
	plt.title(x.name + ' versus ' + y.name)
	plt.show()

def plotTrend(x, y):
	trendline = np.poly1d(np.polyfit(x, y, 1))
	newX = np.linspace(min(x), max(x), num=100)
	plt.autoscale(False)
	plt.plot(newX, trendline(newX), color="orange", lw=1.5)

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


if __name__ == '__main__':
	main()
	if plt.get_fignums():
		resp = input("Press Enter to close...")
		plt.close()
	print("Done with main")
