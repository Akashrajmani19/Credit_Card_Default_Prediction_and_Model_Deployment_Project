from src.Credit_Card_Default_Prediction.components.data_integration import DataIngestion
from src.Credit_Card_Default_Prediction.components.data_transformation import DataTransformation
from src.Credit_Card_Default_Prediction.components.model_trainer import ModelTrainer
import os
import sys
from src.Credit_Card_Default_Prediction.logger import logging
from src.Credit_Card_Default_Prediction.exception import CustomException
import pandas as pd

obj = DataIngestion()

train_data_path,test_data_path=obj.initiate_data_ingestion()

data_transformation=DataTransformation()

X_train,Y_train,X_test,Y_test=data_transformation.initiate_data_transformation(train_data_path,test_data_path)


model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(X_train,Y_train,X_test,Y_test)

# model_eval_obj = ModelEvaluation()
# model_eval_obj.initiate_model_evaluation(train_arr,test_arr)