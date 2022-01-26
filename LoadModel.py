import Model_building
import log
import Loaddata
import pickle
logger=log.get_log("LoadModel")

def loading_model():
      try:

           X_train,Y_train=Loaddata.data()



           model=Model_building.Model()

           model.XGBFit(X_train,Y_train)
           logger.info("Dumping the fitted model : ")
           pickle.dump(model,open('model.pkl','wb'))

      except Exception as e:
             logger.error("Failed to Dump the Model: ",e)



