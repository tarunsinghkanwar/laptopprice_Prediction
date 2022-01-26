from Preprocessing import Preprocessor
import Loaddata
import pickle
import log

logger=log.get_log('LoadPreprocessor')

def Dump_Preprocessor():
    try:
            logger.info("Dumping Preprocessor class into a pickle file: ")
            h=Preprocessor()
            X_train,Y_train=Loaddata.data()
            h.Encoding(X_train,Y_train)
            pickle.dump(h,open("Preprocessing.pkl",'wb'))
    except Exception as e:

            logger.error("Failed to dump Preprocessor class: ",e)


