from crypt import methods
import profile
from unittest import result
from urllib import request
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('Model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict',methods=['POST'])
def predict():
    outlook = request.form.get('outlook')
    temp = request.form.get('temp')
    humidity = request.form.get('humidity')
    windy = request.form.get('windy')

    testArr = np.array([[outlook,temp,humidity,windy]])


    predict = model.predict(testArr)[0]

    if predict == 0:
        prediction = "You Can't Go To Play"
    else:
        prediction = "You Can Go To Play"

    return render_template('form.html', output = predict)

if __name__ == '__main__':
    app.run(debug=True)