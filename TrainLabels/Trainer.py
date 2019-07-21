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
	# print('resultsFrame = ', resultsFrame, sep='\n')
	empathFrame = fileIO.getEmpathFrame()

	numAutoLabel = min(50, len(resultsFrame.index)//5 + 1)
	# numAutoLabel = int(0.15 * len(empathFrame.index))
	happyFrame = empathFrame.copy()
	sentis = happyFrame.positive_emotion - happyFrame.negative_emotion
	happyFrame.insert(2, 'senti', sentis)
	happyFrame.sort_values(by='senti', ascending=False, inplace=True)
	happiestJnums = happyFrame.head(numAutoLabel).jNum.values

	massFrame = pd.DataFrame(columns=resultsFrame.columns)
	l = len(happiestJnums)
	now = datetime.now(tz=timezone.utc).strftime('%Y/%m/%d %I:%M:%S %p %Z') # + datetime.time
	massFrame.Timestamp = [now] * l
	massFrame['CGI-S'] = [1] * l
	massFrame['Concern Labels'] = [None] * l
	massFrame['Custom Concern Labels'] = [None] * l
	massFrame['Username'] = ['autoLabel@autoLabel.autoLabel'] * l
	massFrame.jNum = happiestJnums
	# print('massFrame = ', massFrame, sep='\n')

	if not massFrame.empty:
		resultsFrame = pd.concat((resultsFrame, massFrame))

	combFrame = resultsFrame.merge(empathFrame, on='jNum')

	empathColsIndex = combFrame.columns.get_loc("emotional")
	empathCols = combFrame.iloc[:, empathColsIndex:]
	trainers = empathCols

	scalar = preprocessing.MinMaxScaler(copy=False)
	scalar.fit(trainers)
	scalar.transform(trainers)
	# print("trainers=", trainers, "", sep='\n')

	target = combFrame['CGI-S'].astype('category')
	# print("Empath Columns:", empathCols.columns.values)

	model = svm.LinearSVC()
	model.fit(trainers, target)
	print(model)
	# In problems where it is desired to give more importance to certain classes 
	# or certain individual samples keywords class_weight and sample_weight can be used.
	predicted = model.predict(trainers)
	# print("Trainers:", trainers)
	# print("Target:", target)
	# print("Predicted:", predict, '\n')

	evalFrame = pd.DataFrame(trainers)
	evalFrame.insert(0, "jNum", combFrame.jNum)
	evalFrame.insert(0, "target", target)
	evalFrame.insert(0, "predicted", predicted)
	print('evalFrame:\n', evalFrame[['jNum', 'target', 'predicted']])

	plotCols = ['negative_emotion', 'CGI-S']
	plotFrame = combFrame[plotCols]
	scatterPlotFrame(plotFrame)
	plt.show()

	resp = input("Press enter to close")
	plt.cla()
	plt.exit()

	print("Done with main")

def scatterPlotFrame(plotFrame, trendline=True):
	print(plotFrame)
	plotCols = plotFrame.columns.values
	assert len(plotCols) >= 2
	xLabel, yLabel = plotCols[:2]
	plt.scatter(xLabel, yLabel, data=plotFrame)
	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	plt.title(xLabel + ' versus ' + yLabel)
	if trendline:
		x = plotFrame[xLabel]
		y = plotFrame[yLabel]
		z = np.poly1d(np.polyfit(x, y, 1))
		# print("Trendline:", z)
		newX = np.arange(0, 1, 0.001)
		plt.autoscale(False)
		plt.plot(newX, z(newX), color="yellow")


if __name__ == '__main__':
	main()
