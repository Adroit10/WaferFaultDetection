import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils import collection_as_dataframe

@dataclass
class DataIngestionconfig():
    train_data_path:str=os.path.join("artifacts",'train.csv')
    test_data_path:str=os.path.join("artifacts",'test.csv')
    raw_data_path:str=os.path.jon("artifacts",'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Initiating the data ingestion process')

        try:
            df:pd.DataFrame= collection_as_dataframe(db_name=DBNAME,collection_name=COLLECTIONNAME)
            logging.info('Exported the collection as a DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            train_set,test_set=train_test_split(df,test_size=0.25,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of data from MongodB to {} is complete'.format(self.ingestion_config.raw_data_path))
            logging.info('Data ingestion process complete')

            return(self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path)


        except Exception as e:
            logging.info('Error occured while initiating data ingestion process')
            raise CustomException(e,sys)

