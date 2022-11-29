from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
from termcolor import colored

app = Flask(__name__)

modelo_GBC = joblib.load('proyecto_pipeline_GBC.pkl')
modelo_LR = joblib.load('proyecto_pipeline_LR.pkl')
modelo_RF = joblib.load('proyecto_pipeline_RF.pkl')
FEATURES = joblib.load('FEATURES.pkl')

@app.route("/PredSurv", methods=['POST'])
def PredSurv():
    #data = request.get_json(force=True)
    
    return jsonify({'mensaje': 'Todo Ok'})



app.run(port=5000, debug=True)