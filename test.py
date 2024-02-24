from src.Credit_Card_Default_Prediction.pipelines.prediction_pipeline import CustomData,PredictPipeline
custdataobj = CustomData(90000.0,'Female','University','Single',34,0,0,0,0,0,0,29239.0,14027.0,13559.0,14331.0,14948.0,15549.0,1518.0,1500.0,1000.0,1000.0,1000.0,5000.0)
#
data = custdataobj.get_data_as_dataframe()
Predict_Pipeline = PredictPipeline()
pred = Predict_Pipeline.predict(data)
result = round(pred[0],2)
if result == 0:
    print('Customer will be not get default')
else:
    print('Customer will be get default')
