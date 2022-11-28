from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
from termcolor import colored

app = Flask(__name__)

#modelo_entrenado_para_produccion = joblib.load('./clase5/housePrice_pipeline_v112022.pkl')
#FEATURES = joblib.load('./clase5/FEATURES.pkl')

@app.route("/PredSurv", methods=['POST'])
def PredSurv():
    #data = request.get_json(force=True)
    
    return jsonify({'mensaje': 'Todo Ok'})



app.run(port=5000, debug=True)