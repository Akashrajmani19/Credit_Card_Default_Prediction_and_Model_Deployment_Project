import os
import sys
import pickle
import numpy as np
import pandas as pd
import mlflow
from src.Credit_Card_Default_Prediction.logger import logging
from src.Credit_Card_Default_Prediction.exception import CustomException
import mlflow.sklearn
from sklearn.metrics import f1_score,recall_score, precision_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        mlflow.set_registry_uri("https://dagshub.com/Akashrajmani19/Credit_Card_Default_Prediction_and_Model_Deployment_Project.mlflow")
        tracking_url_type_store = urlparse(mlflow.get_registry_uri()).scheme
        print(tracking_url_type_store) 
        with mlflow.start_run():
            for i in range(len(models)):
                model = list(models.values())[i]
                model.fit(X_train,y_train)
                model_name = model.__class__.__name__
                # mlflow.log_model(f"Model_{i}_name", model_name)
                mlflow.sklearn.log_model(model, model_name)
                # Train model
                model.fit(X_train,y_train)



                # Predict Testing data
                y_test_pred =model.predict(X_test)

                # Get R2 scores for train and test data
                f1_score_ = f1_score(y_test,y_test_pred)
                recal_score = recall_score(y_test,y_test_pred, average='weighted')
                Precision_score = precision_score(y_test,y_test_pred , average='weighted')
                mlflow.log_metric('f1_score', f1_score_)
                mlflow.log_metric('recall_score', recal_score)
                mlflow.log_metric('Precision_score', Precision_score)


                report[list(models.keys())[i]] =  recal_score

            return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)