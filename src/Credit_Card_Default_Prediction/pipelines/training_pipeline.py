from src.Credit_Card_Default_Prediction.components.data_integration import DataIngestion
import os
import sys
from src.Credit_Card_Default_Prediction.logger import logging
from src.Credit_Card_Default_Prediction.exception import CustomException
import pandas as pd

obj = DataIngestion()
obj.initiate_data_ingestion()