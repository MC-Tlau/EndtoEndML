import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exception import CustomException
from logger import logging
from data_transformation import DataTransformation

import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass 

@dataclass
class DataIngestionConfig:
    '''Defining the paths where to save'''
    train_data_path:str = os.path.join('artifact', 'train.csv')
    test_data_path:str = os.path.join('artifact', 'test.csv')
    raw_data_path:str = os.path.join ('artifact', 'data.csv')

class DataIngestion:
    '''Initiated a class object of dataingestion config that contains the path for the files to be saved
    Made a function that reads the dataset and save the files to their corresponding folders
    return training and testing path'''
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('C:/Users/Mercy/OneDrive/Desktop/ML Project/notebook/data/stud.csv')

            logging.info('Reading the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)
            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info("Ingestion of data completed")

            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path)
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
   