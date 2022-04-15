from flask import Flask,render_template,request,session
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

pipeline = joblib.load('./LR_model.sav')

global x_train, y_train, x_test, y_test


#from sklearn.feature_extraction.text import TfidfVectorizer
#vectorizer = TfidfVectorizer()
#Xv_train = vectorizer.fit_transform(x_train)
#Xv_test = vectorizer.transform(x_test)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/predict1',methods =['POST','GET'])
def pred():
    s = []
    if request.method== 'POST':
        news= request.form['news']
        #testing_data = {"text": [news]}
        #testing_df = pd.DataFrame(testing_data)
        #testing_df["text"]= testing_df["text"].apply(word_drop)
        #data_x_test = testing_df["text"]
        #data_xv_test = vectorizer.transform(data_x_test)
        #Predict_Model(data_xv_test)
        pred = pipeline.predict([news])
        return render_template('predict.html', msg="success", op=pred)

if __name__ == '__main__':
    app.secret_key = "hai"
    app.run(port=8080, debug=True)