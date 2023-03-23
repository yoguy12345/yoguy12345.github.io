from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

import os

file_path = 'diamond.pkl'
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    print("File exists and is not empty.")
else:
    print("File does not exist or is empty.")
    
import sys

print(sys.version)


from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('diamond.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        carat = float(request.form['Carat'])
        depth=float(request.form['Depth'])
        table=float(request.form['Table'])
        #Kms_Driven2=np.log(Kms_Driven)
        #Owner=int(request.form['Owner'])
        
        cut=request.form['Cut']
        if(cut=='Good'):
                cut_Good=1
                cut_Ideal=0
                cut_Premium=0
                cut_veryGood=0
        elif(cut=='Ideal'):
                cut_Good=0
                cut_Ideal=1
                cut_Premium=0
                cut_veryGood=0
        elif(cut=='Premium'):
                cut_Good=0
                cut_Ideal=0
                cut_Premium=1
                cut_veryGood=0
        else:
                cut_Good=0
                cut_Ideal=0
                cut_Premium=0
                cut_veryGood=1
                
        color=request.form['Color']
        
        if(color=='color_E'):
            color_E = 1
            color_F = 0
            color_G = 0
            color_H = 0
            color_I = 0
            color_J = 0
        elif(color=='color_F'):
            color_E = 0
            color_F = 1
            color_G = 0
            color_H = 0
            color_I = 0
            color_J = 0
        elif(color=='color_G'):
            color_E = 0
            color_F = 0
            color_G = 1
            color_H = 0
            color_I = 0
            color_J = 0
        elif(color=='color_H'):
            color_E = 0
            color_F = 0
            color_G = 0
            color_H = 1
            color_I = 0
            color_J = 0
        elif(color=='color_I'):
            color_E = 0
            color_F = 0
            color_G = 0
            color_H = 0
            color_I = 1
            color_J = 0
        else:
            color_E = 0
            color_F = 0
            color_G = 0
            color_H = 0
            color_I = 0
            color_J = 1
            
        clarity=request.form['Clarity']
        
        if(clarity=='clarity_E'):
            clarity_E = 1
            clarity_F = 0
            clarity_G = 0
            clarity_H = 0
            clarity_I = 0
            clarity_J = 0
            clarity_K = 0
        elif(clarity=='clarity_F'):
            clarity_E = 0
            clarity_F = 1
            clarity_G = 0
            clarity_H = 0
            clarity_I = 0
            clarity_J = 0
            clarity_K = 0
        elif(clarity=='clarity_G'):
            clarity_E = 0
            clarity_F = 0
            clarity_G = 1
            clarity_H = 0
            clarity_I = 0
            clarity_J = 0
            clarity_K = 0
        elif(clarity=='clarity_H'):
            clarity_E = 0
            clarity_F = 0
            clarity_G = 0
            clarity_H = 1
            clarity_I = 0
            clarity_J = 0
            clarity_K = 0
        elif(clarity=='clarity_I'):
            clarity_E = 0
            clarity_F = 0
            clarity_G = 0
            clarity_H = 0
            clarity_I = 1
            clarity_J = 0
            clarity_K = 0
        elif(clarity=='clarity_J'):
            clarity_E = 0
            clarity_F = 0
            clarity_G = 0
            clarity_H = 0
            clarity_I = 0
            clarity_J = 1
            clarity_K = 0
        else:
            clarity_E = 0
            clarity_F = 0
            clarity_G = 0
            clarity_H = 0
            clarity_I = 0
            clarity_J = 0
            clarity_K = 1
        prediction=model.predict([[carat,depth,table,cut_Good,cut_Ideal,cut_Premium,cut_veryGood,\
          color_E,color_F,color_G,color_H,color_I,color_J,clarity_E,clarity_F,clarity_G,\
                               clarity_H,clarity_I,clarity_J,clarity_K]])
        
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this diamond")
        else:
            return render_template('index.html',prediction_text="You Can Sell The diamond at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)