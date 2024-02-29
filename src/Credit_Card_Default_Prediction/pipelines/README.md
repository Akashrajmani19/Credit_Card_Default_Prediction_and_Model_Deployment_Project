# Training Pipeline Module - training_pipeline.py

The `training_pipeline.py` module orchestrates the entire training pipeline for a credit card default prediction project. It integrates data ingestion, data transformation, and model training components to prepare the data and train machine learning models.

## Purpose
This module aims to automate the end-to-end process of data ingestion, data transformation, and model training. It provides a streamlined approach to load data, preprocess it, train machine learning models, and evaluate their performance.

## File Structure
- **training_pipeline.py**: Main module for orchestrating the training pipeline.
- **logger.py**: Module for logging purposes.
- **exception.py**: Module containing custom exception classes.
- **components/data_integration.py**: Module for data ingestion tasks.
- **components/data_transformation.py**: Module for data transformation tasks.
- **components/model_trainer.py**: Module for model training tasks.

## Dependencies
- pandas
- src.Credit_Card_Default_Prediction (custom modules)

## Workflow
1. **Data Ingestion**:
    - Raw data is ingested using the DataIngestion component.
    - Training and testing data paths are obtained.

2. **Data Transformation**:
    - Data transformation tasks are initiated using the DataTransformation component.
    - Data is preprocessed and transformed into a suitable format for model training.

3. **Model Training**:
    - Model training tasks are initiated using the ModelTrainer component.
    - Machine learning models are trained on the preprocessed data.

4. **Model Evaluation (Optional)**:
    - Model evaluation tasks can be performed to assess the performance of trained models (not implemented in the provided code snippet).

## Usage
To utilize the functionalities provided by `training_pipeline.py`, follow these steps:

1. Import the necessary modules and classes:
    ```python
    from src.Credit_Card_Default_Prediction.components.data_integration import DataIngestion
    from src.Credit_Card_Default_Prediction.components.data_transformation import DataTransformation
    from src.Credit_Card_Default_Prediction.components.model_trainer import ModelTrainer
    ```

2. Create an instance of the `DataIngestion` class to initiate data ingestion:
    ```python
    data_ingestion = DataIngestion()
    ```

3. Perform data ingestion to obtain training and testing data paths:
    ```python
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
    ```

4. Create an instance of the `DataTransformation` class to initiate data transformation:
    ```python
    data_transformation = DataTransformation()
    ```

5. Perform data transformation to preprocess the data:
    ```python
    X_train, Y_train, X_test, Y_test = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
    ```

6. Create an instance of the `ModelTrainer` class to initiate model training:
    ```python
    model_trainer = ModelTrainer()
    ```

7. Train machine learning models using the preprocessed data:
    ```python
    model_trainer.initiate_model_training(X_train, Y_train, X_test, Y_test)
    ```

8. (Optional) Perform model evaluation to assess model performance:
    ```python
    # model_eval_obj = ModelEvaluation()
    # model_eval_obj.initiate_model_evaluation(train_arr,test_arr)
    ```

# Prediction Pipeline Module - Prediction_pipeline.py

The `Prediction_pipeline.py` module is responsible for making predictions using a trained machine learning model. It provides functionalities to load the preprocessor, output encoder, and trained model, preprocess input features, and make predictions.

## Purpose
This module aims to streamline the process of making predictions on new data using a trained machine learning model. It provides a convenient interface to preprocess input features and obtain predictions for credit card default prediction.

## File Structure
- **Prediction_pipeline.py**: Main module for making predictions using a trained model.
- **logger.py**: Module for logging purposes.
- **exception.py**: Module containing custom exception classes.
- **utils/utils.py**: Utility functions for loading objects and logging.

## Dependencies
- pandas
- src.Credit_Card_Default_Prediction.utils (custom modules)

## Classes and Functions

### PredictPipeline
- **Methods**:
    - `__init__()`: Initializes the PredictPipeline object.
    - `predict(feature)`: Performs prediction on input features using a trained machine learning model.

### CustomData
- **Methods**:
    - `__init__()`: Initializes the CustomData object with input features.
    - `get_data_as_dataframe()`: Converts input features into a pandas DataFrame.

## Workflow
1. **Loading Objects**:
    - Preprocessor, output encoder, and trained model objects are loaded from pickle files.

2. **Data Preprocessing**:
    - Input features are preprocessed using the preprocessor object.

3. **Prediction**:
    - Preprocessed features are passed to the trained model for prediction.

4. **Result**:
    - Predicted labels are returned as output.

## Usage
To utilize the functionalities provided by `Prediction_pipeline.py`, follow these steps:

1. Import the necessary modules and classes:
    ```python
    from src.Credit_Card_Default_Prediction.Prediction_pipeline import PredictPipeline, CustomData
    ```

2. Create an instance of the `PredictPipeline` class:
    ```python
    predict_pipeline = PredictPipeline()
    ```

3. Load input features and convert them into a pandas DataFrame using the `CustomData` class:
    ```python
    custom_data = CustomData(LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6, BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6)
    input_df = custom_data.get_data_as_dataframe()
    ```

4. Perform prediction using the `predict(feature)` method:
    ```python
    prediction = predict_pipeline.predict(input_df)
    ```

