import os
import sys
import pandas as pd
from flask import Flask, request, render_template,jsonify
from src.Credit_Card_Default_Prediction.pipelines.prediction_pipeline import CustomData,PredictPipeline

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict", methods = ["GET","POST"])
def predict_datapoint():
    if request.method == 'GET':
        return render_template("form.html")

    else:
        data=CustomData(
        LIMIT_BAL =  float(request.form['LIMIT_BAL']),
        SEX = request.form['SEX'],
        EDUCATION = request.form['EDUCATION'],
        MARRIAGE = request.form['MARRIAGE'],
        AGE = int(request.form['AGE']),
        PAY_0 = int(request.form['REPAYMENT_STATUS_SEPT']),
        PAY_2 = int(request.form['REPAYMENT_STATUS_AUGUST']),
        PAY_3 = int(request.form['REPAYMENT_STATUS_JULY']),
        PAY_4 = int(request.form['REPAYMENT_STATUS_JUNE']),
        PAY_5 = int(request.form['REPAYMENT_STATUS_MAY']),
        PAY_6 = int(request.form['REPAYMENT_STATUS_APRIL']),
        BILL_AMT1 =float(request.form['BILL_AMT_SEPT']),
        BILL_AMT2 =float(request.form['BILL_AMT_AUGUST']),
        BILL_AMT3 =float(request.form['BILL_AMT_JULY']),
        BILL_AMT4 =float(request.form['BILL_AMT_JUNE']),
        BILL_AMT5 =float(request.form['BILL_AMT_MAY']),
        BILL_AMT6 =float(request.form['BILL_AMT_APRIL']),
        PAY_AMT1 = float(request.form['PAY_AMT_SEPT']),
        PAY_AMT2 = float(request.form['PAY_AMT_AUGUST']),
        PAY_AMT3 = float(request.form['PAY_AMT_JULY']),
        PAY_AMT4 = float(request.form['PAY_AMT_JUNE']),
        PAY_AMT5 = float(request.form['PAY_AMT_MAY']),
        PAY_AMT6 = float(request.form['PAY_AMT_APRIL'])
        )
        final_data = data.get_data_as_dataframe()
        Predict_Pipeline = PredictPipeline()
        pred = Predict_Pipeline.predict(final_data)
        if pred == 0:
            result = "Customer will not get default"
        else:
            result = "Customer will get default"
        return render_template("result.html",final_result = result)
    
if __name__ == "__main__":
    app.run(host ="0.0.0.0",port=8080)
