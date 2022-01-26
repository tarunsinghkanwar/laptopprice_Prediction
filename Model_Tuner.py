import log
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor
logger=log.get_log("Model_Tuner")

class find_best_param:

    def __init__(self):

        try:

            self.param= {
                                  'n_estimators':[10,20,30,40,50,60,70],
                                  'max_depth':[1,2,3,4,5,6],
                                  'learning_rate':[0.1,0.2,0.3,0.4,0.5],
                                  'booster': ['gbtree', 'dart']

                                  }
            self.XGB=XGBRegressor()
            self.gsv = GridSearchCV(estimator=self.XGB,param_grid=self.param,cv=3,scoring='r2')
        except Exception as e:
            logger.error("Failed to Initialise Model Tuner {}".format(e))


    def Hyperparamters(self,X,Y):

            try:
                logger.info("Hperparamter Tuning has started: ")
                self.gsv.fit(X,Y)
                logger.info("best_param for XGBModel are : ",self.gsv.best_params_)
                return self.gsv.best_params_


            except Exception as e:

                logger.error("Failed to Tunned the model: ",e)
