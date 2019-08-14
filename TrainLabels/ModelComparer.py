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

    def fit(self, X, y, scoring, cv=5, iid=False, **kwargs):
        print("Grid Searching on models:", end='', flush=True)
        for model in self.models:
            possParams = set(model.get_params().keys())
            chosenParams = set(self.params.keys())
            jointParams = possParams.intersection(chosenParams)
            params = {k:self.params[k] for k in jointParams}
            modelName = type(model).__name__
            print(modelName+"...", end='', flush=True)
            gs = GridSearchCV(model, params, cv=cv, scoring=scoring, iid=iid)
            try:
                gs.fit(X, y)
            except ValueError as e:
                print(e)
                print("Skipping", modelName, "for above error in fitting^^")
                continue
            self.grids[modelName] = pd.DataFrame(gs.cv_results_)
            self.bestOf[modelName] = gs.best_estimator_
        print("done!")

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
        uniques = bigFrame[rankOnes].drop_duplicates(subset='estimator')
        return uniques

    def getModelScores(self):
        bigFrame = self.getLilFrame()
        goodCols = 'mean_test_score estimator params'.split()
        bigFrame = bigFrame.sort_values(['mean_test_score'])
        return bigFrame[goodCols]

    def getBestModel(self):
        bigFrame = self.getModelScores()
        bestModelName = bigFrame['estimator'].iloc[-1]
        bestModel = self.bestOf[bestModelName]
        return bestModel

    def __str__(self):
        return str(self.getModelScores())
