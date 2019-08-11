import pandas as pd
import numpy as np

from sklearn.model_selection import GridSearchCV

class ModelComparer:

    def __init__(self, models: list, params: dict):
        self.models = models
        self.params = params
        self.grids = {}
        self.bestOf = {}
        self.bigFrame = None
        self.lilFrame = None

    def fit(self, X, y, cv=5, scoring='r2', iid=True, **kwargs):
        for model in self.models:
            possParams = set(model.get_params().keys())
            chosenParams = set(self.params.keys())
            jointParams = possParams.intersection(chosenParams)
            params = {k:self.params[k] for k in jointParams}
            modelName = type(model).__name__
            print("Running GridSearchCV for %s..." % modelName)
            gs = GridSearchCV(model, params, cv=cv, scoring=scoring, iid=iid)
            gs.fit(X, y)
            self.grids[modelName] = pd.DataFrame(gs.cv_results_)
            self.bestOf[modelName] = gs.best_estimator_

    def getBigFrame(self):
        if self.bigFrame is not None:
            return self.bigFrame
        bigFrame = pd.DataFrame()
        for modelName, grid in self.grids.items():
            grid['estimator'] = modelName
            bigFrame = pd.concat((bigFrame, grid), sort=False, ignore_index=True)
        self.bigFrame = bigFrame
        return self.bigFrame

    def getLilFrame(self):
        bigFrame = self.getBigFrame()
        rankOnes = bigFrame['rank_test_score'] == 1
        return bigFrame[rankOnes]

    def getModelScores(self):
        bigFrame = self.getLilFrame()
        goodCols = 'mean_test_score estimator params'.split()
        bigFrame = bigFrame.sort_values(['mean_test_score'])
        return bigFrame[goodCols]

    def getBestModel(self):
        bigFrame = self.getModelScores()
        bestModelName = bigFrame['estimator'].iloc[-1]
        bestModel = self.bestOf[bestModelName]
        return bestModelName, bestModel
