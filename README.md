# Credit Card Default Prediction and Model Deployment Project

## Introduction

In the realm of financial analysis, the ability to predict credit defaults has emerged as a pivotal factor in maintaining the stability and sustainability of commercial banks. This project embarks on a comprehensive journey, beginning with Exploratory Data Analysis (EDA) and culminating in the deployment of an advanced machine learning model through a Flask-based web application. Our aim is to provide a holistic solution that not only enhances credit risk assessment but also empowers real-time decision-making.

## Data Source 

In our dataset we have 25 columns which reflects various attribute of the customer. The target columns is default.payment.next.month, Which reflects whether the customers defaulte or not. Our aim is to predict the probability od default given he payment history os the custmers. I have built my model using a public dataset available on kaggle.        
<a href="https://www.kaggle.com/uciml/default-of-credit-card-clients-dataset">https://www.kaggle.com/uciml/default-of-credit-card-clients-dataset<a>        

### OUTPUT: 
1. default.payment.next.month: Default payment (1=yes, 0=no)

### INPUTS:
1. ID: ID of each client 
2. LIMIT_BAL: Amount of given credit in NT (New Taiwan) dollars 
3. SEX: Gender (1=male, 2=female)
4. EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
5. MARRIAGE: Marital status (1=married, 2=single, 3=others)
6. AGE: Age in years
7. PAY_0: Repayment status in Sep, 2005 (-1=pay duly, 
 1=payment delay for one month, 2=payment delay for two months, ... 8=payment delay for eight months, 9=payment delay for nine months and above)
8. PAY_2: Repayment status in August, 2005 (scale same as above)
9. PAY_3: Repayment status in July, 2005 (scale same as above)
10. PAY_4: Repayment status in June, 2005 (scale same as above)
11. PAY_5: Repayment status in May, 2005 (scale same as above)
12. PAY_6: Repayment status in April, 2005 (scale same as above)
13. BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
14. BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
15. BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
16. BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
17. BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
18. BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
19. PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
20. PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
21. PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
22. PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
23. PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
24. PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar




## Exploratory Data Analysis (EDA)

The initial phase of the project involves delving into the dataset to extract meaningful insights and trends. Through rigorous data exploration and visualization techniques, we seek to unravel key patterns that may influence credit default probabilities. By meticulously examining the distribution of features, identifying outliers, and uncovering potential correlations, our EDA process serves as the foundational stepping stone towards informed feature engineering.

## Feature Engineering: Unveiling Hidden Insights

Armed with the insights garnered from EDA, the project transitions to the feature engineering stage. Here, we unleash the full potential of the dataset by crafting new features, transforming existing ones, and selecting the most relevant attributes. Our goal is to enhance the predictive capacity of the subsequent machine learning models by uncovering latent relationships and capturing intricate nuances within the data.

## Machine Learning Model Selection

The heart of our project lies in the application of a diverse array of machine learning models. We meticulously evaluate the performance of several algorithms, including Logistic Regression, K-Nearest Neighbors (KNN), Naive Bayes, Random Forest Regression, and XGBoost. Through rigorous testing and cross-validation, we identify the model that best aligns with our prediction objectives and dataset characteristics.

## Model Deployment: Empowering Real-time Decisions

Upon selecting the most potent machine learning model, we transition from experimentation to deployment. Leveraging Flask, a powerful Python web framework, we create an intuitive and user-friendly web application. This platform empowers end-users, ranging from financial analysts to decision-makers within commercial banks, to seamlessly input relevant information and obtain real-time credit default predictions. The deployment phase embodies the culmination of our efforts, transforming complex algorithms into a tangible tool for actionable insights.

## Conclusion: Navigating the Financial Landscape

In a world where financial stability is paramount, the fusion of Exploratory Data Analysis, Feature Engineering, Machine Learning, and Model Deployment represents a pioneering approach to credit risk assessment. By traversing this multifaceted journey, we equip stakeholders with the means to anticipate credit defaults and make informed decisions. As the financial landscape continues to evolve, our project stands as a beacon of innovation, guiding the industry towards heightened security, resilience, and prosperity.



# Project Structure and Workflow

## File Structure

- **data_integration.py**: Module for data ingestion tasks.
- **data_transformation.py**: Module for data transformation tasks.
- **model_trainer.py**: Module for model training tasks.
- **Prediction_pipeline.py**: Module for making predictions using a trained model.
- **utils.py**: Utility module containing helper functions for loading objects and logging.
- **logger.py**: Module for logging purposes.
- **exception.py**: Module containing custom exception classes.
- **app.py**: Flask application for deploying the prediction model as a web service.

## Workflow

1. **Data Ingestion**:
   - The `data_integration.py` module handles data ingestion tasks, importing raw data and saving it to artifacts folder.
   - Raw data is imported from the specified file path and saved as raw_data.csv.

2. **Data Transformation**:
   - The `data_transformation.py` module preprocesses and transforms the raw data for model training.
   - It performs tasks such as handling missing values, encoding categorical features, and scaling numerical features.
   - Preprocessed data is saved as train_data.csv and test_data.csv in the artifacts folder.

3. **Model Training**:
   - The `model_trainer.py` module trains machine learning models using preprocessed data.
   - It loads the preprocessed data, trains multiple models, evaluates their performance, selects the best model, and saves it for future use.
   - The trained model is saved as model.pkl in the artifacts folder.

4. **Prediction**:
   - The `Prediction_pipeline.py` module makes predictions on new data using the trained model.
   - It loads the preprocessor, output encoder, and trained model, preprocesses input features, and makes predictions.
   - Predictions are returned as output.

5. **Deployment**:
   - The `app.py` file contains a Flask application for deploying the prediction model as a web service.
   - It provides endpoints for users to interact with the model, including a homepage, prediction form, and result page.

## Dependencies

- pandas
- numpy
- scikit-learn
- Flask

## Usage

1. **Data Ingestion**:
   - Modify the file path in `data_integration.py` to point to your raw data file.
   - Run `data_integration.py` to ingest and save the raw data.

2. **Data Transformation**:
   - Run `data_transformation.py` after data ingestion to preprocess and transform the data.
   - Ensure the data paths are correctly set in `data_transformation.py`.

3. **Model Training**:
   - Run `model_trainer.py` after data transformation to train machine learning models.
   - Adjust the model parameters and evaluation metrics as needed in `model_trainer.py`.

4. **Prediction**:
   - Use the `Prediction_pipeline.py` module to make predictions on new data.
   - Ensure the input features are correctly formatted and provide them to the `predict` function.

5. **Deployment**:
   - Run `app.py` to start the Flask application.
   - Access the web service at http://localhost:8080/ to interact with the prediction model.


