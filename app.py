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

def generateLog(message,logType):
    f=open("logsData.log","a")
    message = message+ datetime.today().strftime('%Y-%m-%d %H:%M:%S') +';'+'\n'
    f.write(message)
    if(logType==10):
        strColor = 'yellow'
    elif(logType==30):
        strColor='red'
    elif(logType== 90):
        strColor='green'
    print(colored(message, strColor))    
    f.close()


@app.route("/PredSurv", methods=['POST'])
def PredSurv():
    data = request.get_json(force=True)
    dataframe = pd.json_normalize(data)

    ###informar sobre transformacion de json (logs) 
    logStr = '0x10 - INFO JSON - transformado exitosamente - ' 
    generateLog(logStr,10)

    ## codigo para este API
    ids = dataframe['PassengerId']
    dataframe = dataframe[FEATURES]

    #prediccion
    try:
        nomr_preds = modelo_RF.predict(dataframe)
        outPredict = np.exp(nomr_preds) 
        out = {}
        for index,item in enumerate(outPredict):
            out[str(ids[index])]=round(item,2)
        logStr1 = "0x90 - exito - se genero correctamente la prediccion - con RandomForest"
        generateLog(logStr1,90)   
        
        nomr_preds2 = modelo_LR.predict(dataframe)
        outPredict2 = np.exp(nomr_preds2) 
        out2 = {}
        for index,item in enumerate(outPredict2):
            out2[str(ids[index])]=round(item,2)
        logStr2 = "0x90 - exito - se genero correctamente la prediccion - con LogisticRegression"
        generateLog(logStr2,90)   

        nomr_preds3 = modelo_GBC.predict(dataframe)
        outPredict3 = np.exp(nomr_preds3) 
        out3 = {}
        for index,item in enumerate(outPredict3):
            out3[str(ids[index])]=round(item,2)
        logStr3 = "0x90 - exito - se genero correctamente la prediccion - con GradientBoostingClassifier"
        generateLog(logStr3,90) 

        return jsonify(out,{'mensaje':logStr1}, out2,{'mensaje':logStr2}, out3,{'mensaje':logStr3}) 


    except ValueError:
        logStr = '0x30 - Predict Error - se genero un error en la prediccion - ' 
        generateLog(logStr,30) 
        return jsonify({'mensaje':logStr})   


app.run(port=5000, debug=True)