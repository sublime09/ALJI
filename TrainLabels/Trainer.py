print("Importing...", end='')
import fileIO, config
# from inspect import signature, getmembers
# pprint(signature(pprint))
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.svm import SVR, SVC
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import GridSearchCV
print(" done!")

# print(config.defaultLabels)

# TODO: DummyRegressor, Lasso, ElasticNet, SVR(kernel='rbf')
# TODO: EnsembleRegressors?  n_estimators=100
# TODO: Label Propagation

''' RUNNING OPTIONS FOR MODELS '''
visualizeCGI = False
labelSpreadingAlpha = None
numAutoLabel = 10 # worse than label spreading?
# scalar = MinMaxScaler(copy=False)
scalar = StandardScaler(copy=False)
# baseModel = DummyRegressor()        # r= -0.446
# baseModel = SVC(kernel='linear')    # 
# baseModel = SVR(kernel='linear')    # r= -0.103
# baseModel = Lasso()                 # r= -0.120 WARNINGS
baseModel = ElasticNet()              # r= -0.121 WARNINGS
# baseModel = Ridge()                 # r= -0.076
# baseModel = RandomForestRegressor() # r= -0.218 to -0.323 random
params = dict()
params['C'] = [pow(10, i) for i in range(-3, 4)]
params['alpha'] = [pow(10, i) for i in range(-3, 1)]
params['n_estimators'] = [pow(5, i) for i in range(1, 5)]
# params['epsilon'] = [pow(10, i) for i in range(-2, 2)]
# params['degree'] = range(2, 5)
# params['gamma'] = [pow(5, i) for i in range(-3, 3)]

def main():
	print("Started Trainer main....")
	resultsFrame = fileIO.getResultFrame()
	print("Read", len(resultsFrame.index), "Participant results ...")
	empathFrame = fileIO.getEmpathFrame()
	print("Read", len(empathFrame.index), "Empath analysis results ...")
	empathCols = empathFrame.columns.values[2:]
	assert len(empathCols) == 194
	resultsFrame['color'] = 'blue'

	if numAutoLabel > 0:
		cols = "negative_emotion medical_emergency pain anger shame torment".split()
		negSenti = empathFrame[cols].sum(axis=1).sort_values()
		negSenti = negSenti.head(numAutoLabel).index
		happyFrame = empathFrame.iloc[negSenti]

		massFrame = pd.DataFrame()
		massFrame['jNum'] = happyFrame.jNum.values
		massFrame['Timestamp'] = "9999/11/11 11:11:11 AM EST"
		massFrame['CGI-S'] = 1
		massFrame['Username'] = 'AUTOLABELED'
		massFrame['color'] = 'teal'
		if not massFrame.empty:
			resultsFrame = pd.concat((resultsFrame, massFrame), sort=False)

	# empathFrame['CGI-S'] = -1 # TODO on label spreading
	combFrame = resultsFrame.merge(empathFrame, on='jNum') # WORKs GOOD

	# print(combFrame[['jNum', 'CGI-S', 'Username']]) # to see contributors

	'''Plotting / Visualization:'''
	plotCols = ['medical_emergency', 'CGI-S', 'color']
	plotFrame = combFrame[plotCols].copy()
	plt.ion() #interactive mode to run in background
	if visualizeCGI:
		scatterPlot(plotFrame, 'medical_emergency', 'CGI-S')

	'''Select target and scale trainers'''
	target = combFrame['CGI-S'].astype('int')
	trainers = combFrame[empathCols]
	scalar.fit(trainers)
	scalar.transform(trainers)

	print("BaseModel =", str(baseModel)[:50], "...")

	# In problems where it is desired to give more importance to certain classes 
	# or certain individual samples keywords class_weight and sample_weight can be used.

	usableParams = baseModel.get_params().keys()
	toRemove = [k for k in params if k not in usableParams]
	for badKey in toRemove:
		del params[badKey]

	'''Train / cross validate:'''
	clf = GridSearchCV(baseModel, params, cv=6)
	print("Cross Validation using", clf.cv, "folds")
	print("Searching Params:", params)
	clf.fit(trainers, target)
	crossValFrame = pd.DataFrame(clf.cv_results_)
	printCols = 'rank_test_score mean_test_score std_test_score params'.split()
	print(crossValFrame[printCols])
	print("Chosen Model =", str(clf.best_estimator_)[:50], "...")
	predicted = clf.predict(trainers)

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
	print("Predictions: %d \t Pct Correct: %.2f%%" % (numTries, pctCorrect))
	if not incorrects.empty:
		pass
		# print("Some Incorrect Predictions: ", incorrects.tail(7), sep='\n')
		# print("Predicted CGI-S:", incorrects.predicted.describe())
		# TODO: color incorrect predictions?

	

def scatterPlot(plotFrame, xCol, yCol, trendline=True):
	x = plotFrame[xCol]
	y = plotFrame[yCol]
	colors = plotFrame.color
	plt.scatter(x=x, y=y, c=colors)
	plt.xlabel(xCol)
	plt.ylabel(yCol)
	plt.title(xCol + ' versus ' + yCol)
	if trendline is not None:
		trendline = np.poly1d(np.polyfit(x, y, 1))
		newX = np.arange(0, 1, 0.01)
		plt.autoscale(False)
		plt.plot(newX, trendline(newX), color="orange")
	plt.show()


if __name__ == '__main__':
	main()
	if visualizeCGI:
		resp = input("Press Enter to close...")
	plt.close()
	print("Done with main")
