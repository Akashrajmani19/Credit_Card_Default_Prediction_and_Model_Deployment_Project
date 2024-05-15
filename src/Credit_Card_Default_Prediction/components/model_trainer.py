import pandas as pd
import numpy as np
import os
import sys
from pathlib import Path
from dataclasses import dataclass

from src.Credit_Card_Default_Prediction.logger import logging
from src.Credit_Card_Default_Prediction.exception import CustomException
from src.Credit_Card_Default_Prediction.utils.utils import save_object
from src.Credit_Card_Default_Prediction.utils.utils import evaluate_model

from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
import mlflow

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')
    
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initate_model_training(self,X_train,Y_train,X_test,Y_test):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                 X_train,
                Y_train,
                X_test,
                Y_test,
            )

            models={
            #'XGBClassifier':XGBClassifier(colsample_bytree = 0.8,gamma= 5,max_depth= 4,min_child_weight= 5,subsample= 1.0,n_jobs = -1),
            'XGBClassifier':XGBClassifier(objective ='binary:logistic', base_score= None, booster= None, callbacks= None, 
            colsample_bylevel= None, colsample_bynode= None, colsample_bytree= 0.5487455924565161, device= None, 
            early_stopping_rounds= None, enable_categorical= False, eval_metric= None, feature_types= None, gamma= None
            , importance_type= None, interaction_constraints= None, learning_rate=0.08581386246280566,max_bin= None,
             max_cat_threshold = None, max_cat_to_onehot= None, max_delta_step= None, max_depth = 3, max_leaves =  None,
              min_child_weight =  3, monotone_constraints=None, multi_strategy=None, n_estimators=136,
               n_jobs=-1, num_parallel_tree=None, random_state=None, reg_alpha= None, reg_lambda=None, sampling_method=None, 
               scale_pos_weight= None, subsample= 0.715231665064311, tree_method= None, validate_parameters= None, verbosity= None),
            #'RandomForestClassifier':RandomForestClassifier(n_estimators=300,min_samples_leaf=15,max_depth= None,criterion= 'gini',n_jobs=-1)
            'RandomForestClassifier':RandomForestClassifier(max_depth=9, max_features=0.29499734960645674,
                       min_samples_leaf=6, min_samples_split=16,
                       n_estimators=121, n_jobs=-1)
            
            }
# ---------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------            
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , recall Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , recall Score : {best_model_score}')

            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )
          

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e,sys)