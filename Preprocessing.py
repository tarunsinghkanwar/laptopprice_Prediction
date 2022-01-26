import feature_engine.encoding as enc
import log
from sklearn.pipeline import Pipeline

logger=log.get_log('Preprocessor')

class Preprocessor:


    def __init__(self):

          try:

               self.preprocessing=Pipeline([
                       ('RareLabel_Encoder',enc.RareLabelEncoder(tol=0.05,n_categories=5)),
                       ('Ordnal_encoder',enc.OrdinalEncoder(encoding_method='ordered'))
                         ])

          except Exception as e:
              print("Failed to initialise: ",e)




    def Encoding(self,X,Y):
        """

        :param X: Independent features
        :param Y: dependent feature

        """
        try:
              logger.info('Encoding the Independent variables has started: ')
              self.preprocessing.fit(X,Y)
        except Exception as e:
             logger.error("Encoding failed :",e)



    def transform(self,X):
        """

        :param X: Independent features
        :return: Transformed features after encoding
        """
        try:
                logger.info("Transforming the Features: ")

                return self.preprocessing.transform(X)
        except Exception as e:
            logger.error("Transformation failed: ",e)


