from xgboost import XGBRegressor
import log
from Model_Tuner import find_best_param

logger=log.get_log("Model")
import pickle

class Model:

    def __init__(self):
                try:

                    self.prep = None
                    self.param = {'booster': 'gbtree',
             'gamma': 0.1,
             'learning_rate': 0.3,
             'max_depth': 6,
             'n_estimators': 50
            }
                    self.XGB = None
                    self.M=find_best_param()
                except Exception as e:
                    logger.error("Failed to call Preprocessor :",e)





    def XGBFit(self,X,Y):
        try:

                logger.info("Fiting the Model")
                self.prep=pickle.load(open("Preprocessing.pkl", 'rb'))


                X=self.prep.transform(X)

                #self.param = self.M.Hyperparamters(X, Y)
                self.XGB = XGBRegressor(**self.param)
                self.XGB.fit(X,Y)

        except Exception as e:
            logger.error("Failed to Fit the model: {}".format(e))

    def XGBPredict(self,X):
        try:
            logger.info('Predicting the Laptop Price')

            return self.XGB.predict(X)

        except Exception as e:
            logger.error("Failed to Predict{}".format(e))

