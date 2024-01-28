import pandas as pd
import numpy as np
import os
import sys
from pathlib import Path
from dataclasses import dataclass

from src.Credit_Card_Default_Prediction.logger import logging
from src.Credit_Card_Default_Prediction.exception import CustomException
from src.Credit_Card_Default_Prediction.utils.utils import save_object

# Import libraries for tools
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder,OneHotEncoder,LabelEncoder
from sklearn.preprocessing import PowerTransformer

# pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# configuration for preproccing obj
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    
    def initiate_data_transformation(self,train_data,test_data):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Imported train and test dataset for data transformation')
            logging.info(f"Train DataFrame Head :\n{train_df.head().to_string()}")
            logging.info(f"Test DataFrame Head :\n{test_df.head().to_string()}") 

            preprocessor_obj = self.get_data_transformation()
            target_column = 'default.payment.next.month'
            drop_columns = [target_column,'ID']

            input_feature_train_df = train_df.drop(columns=drop_columns,axis =1)
            input_feature_test_df = test_df.drop(columns=drop_columns,axis =1)
            target_feature_train_df = train_df[target_column]
            target_feature_test_df = test_df[target_column]

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)
            logging.info("Applying preproccesing object on training abd testing datasets.")


            output = LabelEncoder()
            target_feature_train_df =output.fit_transform(target_feature_train_df)
            target_feature_test_df = output.transform(target_feature_test_df)
            looging.info('target column also get transformed')
            
            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_object(
                        file_path=self.data_transformation_config.preprocessor_obj_file_path,
                        obj={'preprocessor': preprocessor_obj, 'output': output}
                        )

            
            logging.info("Preproccessing picklefile saved")
            return(
                train_arr,
                test_arr
            )

        except Exception as e:
            logging.info("Exception occured in the intiate_data_transformation")
            raise CustomException(e,sys) 

    def get_data_transformation(self):
        try: 
            logging.info("Data transformation initiated")
            #imputation transformer
            trf1 = ColumnTransformer(
                [
                    ('impute_numerical_columns1',SimpleImputer(strategy='median'),[0]),
                    ('impute_categorical_columns1',SimpleImputer(strategy='most_frequent'),[1,2,3]),
                    ('impute_numerical_columns2',SimpleImputer(strategy='median'),[4]),
                    ('impute_categorical_columns2',SimpleImputer(strategy='most_frequent'),[5,6,7,8,9,10]),
                    ('impute_numerical_columns3',SimpleImputer(strategy='median'),[11,12,13,14,15,16,17,18,19,20,21,22])
                ]
                         ,remainder='passthrough')
                
            trf2 = ColumnTransformer(
                [
                    ('yao_jhonson_transformation1',PowerTransformer(),[0,4,11,12,13,14,15,16,17,18,19,20,21,22])
                ],remainder="passthrough")
            
            trf3 = ColumnTransformer(
                [
                    ('one_hot_encoding1',OneHotEncoder(sparse_output=False,handle_unknown='ignore'),[14,15,16,17,18,19,20,21,22])
                ],remainder='passthrough')

            preprocessor = Pipeline(
                [
                    ('trf1',trf1),
                    ('trf2',trf2),
                    ('trf3',trf3)
                ]
                            )



            return preprocessor

        except Exception as e:
            logging.info('Exception occured in Data transformation step get_data_transformation')
            raise CustomException(e,sys) 
        