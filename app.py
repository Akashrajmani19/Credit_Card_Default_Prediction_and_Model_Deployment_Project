import os
import sys
import pandas as pd
from flask import Flask, request, render_template,jsonify
from src.Credit_Card_Default_Prediction.pipelines.prediction_pipeline import CustomData,PredictPipeline




app = Flask(__name__,template_folder='Template')



# In[ ]:


@app.route('/',methods=['GET'])


# In[ ]:


def Home():
    return render_template('index.html')


# In[ ]:


@app.route("/predict", methods=['POST'])


# In[ ]:


def predict():
    
    if request.method == 'POST':
        
        
        logging.info('Active User Found')
        
        data=CustomData(
        LIMIT_BAL =  float(request.form['LIMIT_BAL']),
        SEX = request.form['SEX'],
        EDUCATION = request.form['EDUCATION'],
        MARRIAGE = request.form['MARRIAGE'],
        AGE = int(request.form['AGE']),
        PAY_0 = request.form['REPAYMENT_STATUS_SEPT'],
        PAY_2 = request.form['REPAYMENT_STATUS_AUGUST'],
        PAY_3 = request.form['REPAYMENT_STATUS_JULY'],
        PAY_4 = request.form['REPAYMENT_STATUS_JUNE'],
        PAY_5 = request.form['REPAYMENT_STATUS_MAY'],
        PAY_6 = request.form['REPAYMENT_STATUS_APRIL'],
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
        result = round(pred[0],2)
        return render_template('index.html',prediction_text="Probability Of Default Is== {}".format(result))
    
    else:
        return render_template('index.html')


# In[1]:


if __name__=="__main__":
    app.run(debug=True)