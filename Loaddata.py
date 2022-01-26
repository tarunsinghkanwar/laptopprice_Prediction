import pickle
import log

logger=log.get_log("loaddata")


def data():

     try:
         logger.info("Loading X_train and Y_train")
         X_train=pickle.load(open('X_train.pkl','rb'))
         Y_train=pickle.load(open('Y_train.pkl','rb'))
         return X_train,Y_train

     except Exception as e:
         logger.error("Failed to Load the data: {}".format(e))
