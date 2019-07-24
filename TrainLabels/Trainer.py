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
from datetime import datetime, timezone

# print(config.defaultLabels)

def main():
	print("Started Trainer main....")
	resultsFrame = fileIO.getResultFrame()
	empathFrame = fileIO.getEmpathFrame()
	resultsFrame['color'] = ['blue'] * len(resultsFrame.index)

	# numAutoLabel = min(50, len(resultsFrame.index)//5 + 1)
	numAutoLabel = 5
	if numAutoLabel > 0:
		happyFrame = empathFrame.copy()
		sentis = happyFrame.positive_emotion - happyFrame.negative_emotion
		happyFrame.insert(2, 'senti', sentis)
		happyFrame.sort_values(by='senti', ascending=False, inplace=True)
		happiestJnums = happyFrame.head(numAutoLabel).jNum.values

		massFrame = pd.DataFrame(columns=resultsFrame.columns)
		l = len(happiestJnums)
		now = datetime.now(tz=timezone.utc).strftime('%Y/%m/%d %I:%M:%S %p %Z')
		massFrame.Timestamp = [now] * l
		massFrame['CGI-S'] = [1] * l
		massFrame['Concern Labels'] = [None] * l
		massFrame['Custom Concern Labels'] = [None] * l
		massFrame['Username'] = ['autoLabel@autoLabel.autoLabel'] * l
		massFrame['color'] = ['teal'] * l
		massFrame.jNum = happiestJnums

		if not massFrame.empty:
			resultsFrame = pd.concat((resultsFrame, massFrame))

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

	plotCols = ['pain', 'CGI-S', 'color']
	plotFrame = combFrame[plotCols]
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
