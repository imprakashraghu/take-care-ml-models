# author imprakashraghu

from Diabetes import predictDiabetes
from Heart import predictHeartDisease
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask("prediction api")
CORS(app, support_credentials=True)

@app.route("/")
@cross_origin(support_credentials=True)
def home():
    return "welcome to prediction model"

@app.route("/predict")
@cross_origin(support_credentials=True)
def predict():
    prediction = {}     
    glucose = request.args.get('glucose')    
    heartRate = request.args.get('heart')
    bp = request.args.get('bp')
    rfbs = 0
    if int(glucose) < 140:
        rfbs=1
    else:
        rfbs=0    
    heartResult = predictHeartDisease().predict(([[int(heartRate), int(bp), int(rfbs)]]))        
    if heartResult == 0:
        prediction['heart'] = "Negative"
    else:
        prediction['heart'] = "Positive"
    diabetesResult = predictDiabetes().predict(([[int(glucose)]]))    
    if diabetesResult == 0:
        prediction['diabetes'] = "Negative"
    else:
        prediction['diabetes'] = "Positive"
    
    return jsonify(prediction)

app.run(host= '0.0.0.0', port=5001)    