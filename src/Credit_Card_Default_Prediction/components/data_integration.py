import pandas as pd
import numpy as np
import os
import sys
from pathlib import Path
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.Credit_Card_Default_Prediction.logger import logging
from src.Credit_Card_Default_Prediction.exception import CustomException



class DataIngestionConfig:
    raw_data:str = os.path.join('artifacts','raw_data.csv')
    train_data:str = os.path.join('artifacts','train_data.csv')
    test_data:str = os.path.join('artifacts','test_data.csv')




class DataIngestion:
    def __init__(self):
        ''' Creating object of DataIngestionConfig class to provide path to save all artifacts at artifacts folder'''
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data ingestion started.')

        try:
            # Importing data from data folder
            df = pd.read_csv(Path(os.path.join('notebooks/data','UCI_Credit_Card_updated.csv')))
            logging.info('Data has been imported from drive')

            # Saving raw data at artifacts folder as row data
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data)),exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data,index = False)
            logging.info('I have saved the raw dataset in artifact folder')

            # Performing train test split
            train_data,test_data = train_test_split(df,test_size = 0.15, random_state = 42)
            logging.info('Performed train test split and completed')
            # Saving train_data and test data at artifacts folder
            train_data.to_csv(self.ingestion_config.train_data,index = False)
            test_data.to_csv(self.ingestion_config.test_data,index = False)
            logging.info('Train data and Test data is saved at artifacts folder')

            logging.info('Data Ingestion work is completed')

            return (
                self.ingestion_config.train_data,
                self.ingestion_config.test_data
            )






        except Exception as e:
            logging.info('Exception occured during data ingestion stage.')
            raise CustomException(e,sys) 
