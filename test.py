from sklearn.pipeline import  Pipeline
from feature_engine.encoding import RareLabelEncoder,OrdinalEncoder
from xgboost import XGBRegressor
import pickle
import Loaddata
import log
logger=log.get_log("Pipeline")
import Preprocessing

def best_param():
         param=    {'booster': 'gbtree',
             'gamma': 0.1,
             'learning_rate': 0.3,
             'max_depth': 6,
             'n_estimators': 50
            }

         return param

def Model():

    try:
            preprocessing = Pipeline([
                ('RareLabel_Encoder', RareLabelEncoder(tol=0.05, n_categories=5)),
                ('Ordnal_encoder', OrdinalEncoder(encoding_method='ordered')),
                ('XGB',XGBRegressor(**best_param()))
            ])

            return preprocessing
    except Exception as e:
        logger.error("Failed:",e)


pipe=Model()
X_train,Y_train=Loaddata.data()



