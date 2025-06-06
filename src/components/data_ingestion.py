# This file is for reading the data

import os,sys
from src.exception import Custom_exception
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# from data_transformation import DataTransformation

# from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

@dataclass # directly defining class variable without writing init
class DataIngestionConfig:
  train_data_path:str = os.path.join('artifact','train.csv')
  test_data_path:str = os.path.join('artifact','test.csv')
  data_path:str = os.path.join('artifact','original_data.csv')

class DataIngestion:
  def __init__(self):
    self.ingestion_config = DataIngestionConfig()
  def initiate_data_ingestion(self):
    logging.info('entered the data ingestion block')
    try:
      df = pd.read_csv("data/cleaned_all.csv") # we can read from any source here only
      logging.info('Exported the data as dataframe')
      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
      
      
      df.to_csv(self.ingestion_config.data_path,index=False,header=True)
      
      logging.info('Train test split initiated')
      train_set,test_set = train_test_split(df,test_size=.25,random_state=42)
      
      train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
      test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
      logging.info('ingestion of the data is completed')
      
      return(
        self.ingestion_config.train_data_path
        ,self.ingestion_config.test_data_path)
      
    except Exception as e:
      raise(Custom_exception(e,sys))
    
if __name__ == "__main__":
  obj = DataIngestion()
  train_data,test_data = obj.initiate_data_ingestion()
  
  # data_transformation = DataTransformation()
  # train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)
  # model_trainer = ModelTrainer()
  # print(model_trainer.inititate_model_trainer(train_arr,test_arr))
      