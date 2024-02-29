# Data Integration Module - data_integration.py

The `data_integration.py` module is responsible for handling data ingestion tasks, such as importing raw data, performing train-test splitting, and saving the processed data.

## Purpose
This module aims to streamline the process of ingesting raw data for a credit card default prediction project. It provides functionalities to import raw data, split it into training and testing sets, and save the processed data for further analysis and modeling.

## File Structure
- **data_integration.py**: Main module for data ingestion tasks.
- **logger.py**: Module for logging purposes.
- **exception.py**: Module containing custom exception classes.

## Dependencies
- pandas
- numpy
- sklearn

## Classes and Functions

### DataIngestionConfig
- **Attributes**:
    - `raw_data`: Path to store the raw data file.
    - `train_data`: Path to store the training data file.
    - `test_data`: Path to store the testing data file.

### DataIngestion
- **Methods**:
    - `__init__()`: Initializes the DataIngestion object and sets up the ingestion configuration.
    - `initiate_data_ingestion()`: Performs data ingestion tasks, including importing raw data, splitting it into training and testing sets, and saving the processed data.

## Workflow
1. **Importing Raw Data**:
    - Raw data is imported from the specified file path.

2. **Saving Raw Data**:
    - The imported raw data is saved to the specified file path.

3. **Train-Test Splitting**:
    - The raw data is split into training and testing sets using the `train_test_split` function from sklearn.

4. **Saving Train and Test Data**:
    - The training and testing sets are saved to the specified file paths.

## Usage
To utilize the functionalities provided by `data_integration.py`, follow these steps:

1. Import the necessary modules and classes:
    ```python
    from data_integration import DataIngestion
    ```

2. Create an instance of the `DataIngestion` class:
    ```python
    data_ingestion = DataIngestion()
    ```

3. Perform data ingestion by calling the `initiate_data_ingestion()` method:
    ```python
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
    ```

# Data Transformation Module - data_transformation.py

The `data_transformation.py` module handles data transformation tasks, including preprocessing and feature engineering, for a credit card default prediction project.

## Purpose
This module aims to preprocess and transform raw data to prepare it for model training. It provides functionalities to handle missing values, encode categorical features, and scale numerical features.

## File Structure
- **data_transformation.py**: Main module for data transformation tasks.
- **logger.py**: Module for logging purposes.
- **exception.py**: Module containing custom exception classes.
- **utils/utils.py**: Utility functions for saving objects.

## Dependencies
- pandas
- numpy
- sklearn

## Classes and Functions

### DataTransformationConfig
- **Attributes**:
    - `preprocessor_obj_file_path`: Path to store the preprocessor object file.
    - `output_obj_file_path`: Path to store the output object file.

### DataTransformation
- **Methods**:
    - `__init__()`: Initializes the DataTransformation object and sets up the transformation configuration.
    - `initiate_data_transformation(train_path, test_path)`: Performs data transformation tasks, including importing data, preprocessing, and saving preprocessed data.
    - `get_data_transformation()`: Returns the preprocessor object for data transformation.

## Workflow
1. **Importing Data**:
    - Training and testing data are imported from the specified file paths.

2. **Data Preprocessing**:
    - Missing values are handled using SimpleImputer.
    - Numerical features are transformed using PowerTransformer.
    - Categorical features are encoded using OneHotEncoder.

3. **Feature Engineering**:
    - Preprocessed data is split into input features and target labels.
    - Target labels are encoded using LabelEncoder.

4. **Saving Preprocessor Object**:
    - The preprocessor object and output object (for target labels) are saved as pickle files.

5. **Completion**:
    - Preprocessing and transformation tasks are completed.
    - Transformed input features and target labels are returned.

## Usage
To utilize the functionalities provided by `data_transformation.py`, follow these steps:

1. Import the necessary modules and classes:
    ```python
    from data_transformation import DataTransformation
    ```

2. Create an instance of the `DataTransformation` class:
    ```python
    data_transformation = DataTransformation()
    ```

3. Perform data transformation by calling the `initiate_data_transformation(train_path, test_path)` method:
    ```python
    X_train, Y_train, X_test, Y_test = data_transformation.initiate_data_transformation(train_path, test_path)
    ```

# Model Trainer Module - model_trainer.py

The `model_trainer.py` module is responsible for training machine learning models for a credit card default prediction project.

## Purpose
This module aims to streamline the process of training machine learning models on preprocessed data. It provides functionalities to train and evaluate models, select the best performing model, and save the trained model for future use.

## File Structure
- **model_trainer.py**: Main module for model training tasks.
- **logger.py**: Module for logging purposes.
- **exception.py**: Module containing custom exception classes.
- **utils/utils.py**: Utility functions for saving objects and evaluating model performance.

## Dependencies
- pandas
- numpy
- sklearn

## Classes and Functions

### ModelTrainerConfig
- **Attributes**:
    - `model_file_path`: Path to store the trained model file.

### ModelTrainer
- **Methods**:
    - `__init__()`: Initializes the ModelTrainer object and sets up the training configuration.
    - `train_model(X_train, Y_train)`: Trains machine learning models on the provided training data.
    - `evaluate_model(model, X_test, Y_test)`: Evaluates the performance of the trained model on the provided test data.
    - `select_best_model(models, X_train, Y_train, X_test, Y_test)`: Selects the best performing model from a list of models based on evaluation metrics.
    - `save_model(model)`: Saves the trained model as a pickle file.

## Workflow
1. **Training Model**:
    - Machine learning models are trained on the provided training data (features and labels).

2. **Model Evaluation**:
    - The performance of each trained model is evaluated using evaluation metrics such as accuracy, precision, recall, and F1-score.

3. **Model Selection**:
    - The best performing model is selected based on evaluation metrics.

4. **Saving Trained Model**:
    - The selected model is saved as a pickle file for future use.

5. **Completion**:
    - Model training and selection tasks are completed.
    - The trained model is ready for deployment and inference.

## Usage
To utilize the functionalities provided by `model_trainer.py`, follow these steps:

1. Import the necessary modules and classes:
    ```python
    from model_trainer import ModelTrainer
    ```

2. Create an instance of the `ModelTrainer` class:
    ```python
    model_trainer = ModelTrainer()
    ```

3. Train machine learning models by calling the `train_model(X_train, Y_train)` method:
    ```python
    model_trainer.train_model(X_train, Y_train)
    ```

4. Evaluate the trained model by calling the `evaluate_model(model, X_test, Y_test)` method:
    ```python
    model_trainer.evaluate_model(model, X_test, Y_test)
    ```

5. Select the best performing model by calling the `select_best_model(models, X_train, Y_train, X_test, Y_test)` method:
    ```python
    best_model = model_trainer.select_best_model(models, X_train, Y_train, X_test, Y_test)
    ```

6. Save the trained model by calling the `save_model(model)` method:
    ```python
    model_trainer.save_model(best_model)
    ```

