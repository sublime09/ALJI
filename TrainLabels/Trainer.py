import fileIO
import config
import os
# from inspect import signature, getmembers
# pprint(signature(pprint))
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm
from sklearn import preprocessing

# print(config.defaultLabels)

def main():
	print("Started Trainer main....")
	resultsFrame = fileIO.getResultFrame()
	print("Read", len(resultsFrame.index), "Participant results ...")
	empathFrame = fileIO.getEmpathFrame()
	print("Read", len(empathFrame.index), "Empath analysis results ...")
	empathCols = empathFrame.columns.values[2:]

	numAutoLabel = 5
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
		if not massFrame.empty:
			resultsFrame = pd.concat((resultsFrame, massFrame), sort=False)

	combFrame = resultsFrame.merge(empathFrame, on='jNum')
	# print(combFrame[['Username', 'jNum']]) # to see contributors

	empathColsIndex = combFrame.columns.get_loc("emotional")
	empathCols = combFrame.iloc[:, empathColsIndex:]
	trainers = empathCols

	scalar = preprocessing.MinMaxScaler(copy=False)
	scalar.fit(trainers)
	scalar.transform(trainers)

	target = combFrame['CGI-S'].astype('category')
	# print("Empath Columns:", *empathCols.columns.values)

	model = svm.LinearSVC(C=1)
	model.fit(trainers, target)
	print(model)
	# In problems where it is desired to give more importance to certain classes 
	# or certain individual samples keywords class_weight and sample_weight can be used.
	predicted = model.predict(trainers)
	# print("Trainers:", trainers)
	# print("Target:", target)
	# print("Predicted:", predict, '\n')

	parameters = dict()
	parameters['C'] = [pow(10, i) for i in range(0, 4)]
	parameters['alpha'] = [pow(10, i) for i in range(-3, 1)]
	# parameters['epsilon'] = [pow(10, i) for i in range(-2, 2)]
	# parameters['degree'] = range(2, 5)
	# parameters['gamma'] = [pow(5, i) for i in range(-3, 3)]
	usableParams = baseModel.get_params().keys()
	toRemove = [k for k in parameters if k not in usableParams]
	for badKey in toRemove:
		del parameters[badKey]
	evalFrame = pd.DataFrame()
	# evalFrame['jNum'] = combFrame.jNum
	evalFrame["jNum"] = combFrame.jNum
	evalFrame["target"] = target
	evalFrame["predicted"] = predicted
	numTries = len(evalFrame.index)
	incorrects = evalFrame.target.ne(evalFrame.predicted)
	incorrects = evalFrame[incorrects]
	numCorrects = numTries - len(incorrects.index)
	pctCorrect = (100.0 * numCorrects) / numTries
	print("Predictions: %d \t Pct Correct: %.2f%%" % (numTries, pctCorrect))
	if not incorrects.empty:
		print("Incorrect Predictions", incorrects, sep='\n')
		# TODO: color incorrect predictions?


	'''Plotting / Visualization:'''
	plotCols = ['medical_emergency', 'CGI-S']
	plotFrame = combFrame[plotCols]
	plotFrame['color'] = 'blue'
	autolabeled = combFrame.Username == 'AUTOLABELED'
	plotFrame.loc[autolabeled, "color"] = 'teal'
	plt.ion() #interactive mode to run in background
	scatterPlotFrame(plotFrame)
	plt.show()

	resp = input("Press Enter to close...")
	print("Done with main")

def scatterPlotFrame(plotFrame, trendline=True):
	plotCols = plotFrame.columns.values
	assert len(plotCols) >= 2
	xLabel, yLabel = plotCols[:2]
	# print("plotFrame = \n", plotFrame)
	plt.scatter(xLabel, yLabel, color=plotFrame.color, data=plotFrame)
	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	plt.title(xLabel + ' versus ' + yLabel)
	if trendline:
		x = plotFrame[xLabel]
		y = plotFrame[yLabel]
		trendline = np.poly1d(np.polyfit(x, y, 1))
		newX = np.arange(0, 1, 0.001)
		plt.autoscale(False)
		plt.plot(newX, trendline(newX), color="orange")


if __name__ == '__main__':
	main()
