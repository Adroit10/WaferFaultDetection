import os
import sys
from src.components.data_ingestion import DataIngestion
from src.logger import logging
from src.exception import CustomException

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestion()

    def num_pipeline(self):
        try:
            train_path,test_path=self.data_ingestion_config.initiate_data_ingestion()

        except Exception as e:
            logging.info('Error occured in the num_pipeline in the training_pipeline.py file')
            raise CustomException(e,sys)