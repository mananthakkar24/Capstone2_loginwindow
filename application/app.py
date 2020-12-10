from flask import Flask, render_template, redirect, url_for, request
from flask import session, abort, flash, jsonify
import pymysql
import os
import pandas as pd
import flask
import numpy as np
import scipy
from sklearn.model_selection import train_test_split
from scipy import integrate
import io
import requests
from multiprocessing.pool import ThreadPool
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import Dense 
from keras.layers import Dropout
from keras.layers import LSTM 
from sklearn.preprocessing import StandardScaler
from keras.models import model_from_yaml
import urllib.request
import ssl
import pickle
ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen('https://www.python.org')
#print(response.read().decode('utf-8'))

file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

yaml_file = open('model1.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
# load weights into new model
loaded_model.load_weights("model1.h5")

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

app.debug = True

app.secret_key = os.urandom(12)

import requests
import random

@app.route('/otp_ver')
def otp_ver(number = 9671144600):
    otp = random.randint(1000,9999)

    otp = str(otp)
    number = str(number)
    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization":"aNjoWx03jO",
    "sender_id":"FSTSMS","message":"Your OTP is " + otp + " Thank you for using MAST ", "language":"english","route":"p","numbers":number}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    {
        "return": True,
        "request_id": "lwdtp7cjyqxvfe9",
        "message": [
            "Message sent successfully to NonDND numbers"
        ]
    }

    {
        "return": True,
        "request_id": "vrc5yp9k4sfze6t",
        "message": [
            "Message sent successfully"
        ]
    }
    return otp


def tablelist():
    file_location = "https://api.covid19india.org/csv/latest/state_wise.csv"
    file_data = pd.read_csv(file_location)
    indexNames = file_data[file_data['State'] == "Total" ].index
    file_data.drop(indexNames , inplace=True)
    result = file_data['State'].values.tolist()
    result = zip(file_data.State,file_data.Active,file_data.Confirmed,file_data.Recovered,file_data.Deaths)
    return result

def covid_info():
    file_location = "https://api.covid19india.org/csv/latest/state_wise.csv"
    file_data = pd.read_csv(file_location)
    a = file_data[0:1]
    totalcount = a.iat[0,1]
    recoveredcount = a.iat[0,2]
    deathcount = a.iat[0,3]
    activecount = a.iat[0,4]
    lastupdate = a.iat[0,5]
    output = file_data[['State','Confirmed','Recovered','Deaths']].groupby('State').sum()
    output = output.drop(['Total'])
    output = output.reset_index()
    output = output.sort_values(by='Confirmed',ascending=False)
    confirmed_val = output['Confirmed'].values.tolist()
    state_name = output['State'].values.tolist()
    recoverd_val = output['Recovered'].values.tolist()
    death_val = output['Deaths'].values.tolist()
    total = {'lastupdate':lastupdate,
    'totalcount':totalcount,'recoveredcount':recoveredcount,
    'activecount':activecount,'deathcount':deathcount,'state_name':state_name, 
    'confirmed_val':confirmed_val, 'recovered_val':recoverd_val,'death_val':death_val}
    return total

def lstmPredictions():
    scaler=StandardScaler()
    acd = pd.read_csv('https://api.covid19india.org/csv/latest/case_time_series.csv')
    acd["Active"]=acd["Total Confirmed"]-acd["Total Deceased"]-acd['Total Recovered']
    Indian = acd.groupby(["Date_YMD"])["Active"].sum().reset_index().sort_values("Date_YMD")
    acdf = Indian[['Date_YMD','Active']]
    datee = Indian[['Date_YMD']]
    acdf.reset_index()
    acdf = acdf.set_index('Date_YMD')
    # print(acdf)
    acdf['Active']=scaler.fit_transform(acdf['Active'].values.reshape(-1,1))
    len(acdf)
    ind=int(0.8*len(acdf))
    acdf_train=acdf.iloc[:ind,:]
    acdf_test=acdf.iloc[ind:,:]
    exp=acdf.iloc[0:]
    exp=pd.DataFrame(exp)

    obs_lag = 20
    n_feature= 1
    l=exp.values.tolist()
    #TimeseriesGenerator will convert the samples into supervised learning
    generator = TimeseriesGenerator(l,l, length=obs_lag, batch_size=1)

    lstm_predictions = list()

    batch = acdf['Active'][-obs_lag:]
    batchDate = acdf.index[-obs_lag:]

    current_batch = batch.values.reshape((1, obs_lag, n_feature))
    ls=current_batch[0]
    for i in range(5):   
        lstm_pred = loaded_model.predict(current_batch)[0]
        lstm_predictions.append(lstm_pred) 
        current_batch = np.append(current_batch[:,1:,:],[[lstm_pred]],axis=1)
        
    lstm_predictions_Active = scaler.inverse_transform(lstm_predictions)
    return lstm_predictions_Active

def get_db():
    db = pymysql.connect(host='localhost', user='root', passwd='root@123',
                         db='test', charset='utf8mb4')
    return db

@app.route('/main')
def main():
    covid = covid_info()
    result = tablelist()
    lstm = lstmPredictions()
    return render_template('main.html',total = covid, result = result, lstm = lstm)

@app.route('/')
def base():
    covid = covid_info()
    return render_template('home.html',total=covid)

# SignUp
@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if 'email' in request.form \
                and 'password' in request.form:
            name = request.form.get('name')
            age = request.form.get('age')
            #email = request.form.get('email')
            username = request.form.get('username')
            password = request.form.get('password')
            confirmpassword = request.form.get('confirm')
            phone = request.form.get('phone')
            Address = request.form.get('address')
            State = request.form.get('state')
            City = request.form.get('city')
            BodyTemperature = request.form.get('bd')
            RunnyNose = request.form.get('rn')
            BodyAche = request.form.get('ba')
            DifficultyinBreathing = request.form.get('db')
            DryCough = request.form.get('dc')
            Otp = request.form.get('op')
            db = get_db()
            c = db.cursor()
            c.execute('select phone from testApi where phone = %s', phone)
            account = c.fetchone()
            if account:
              flash('Email already exists please try again with another email!')
              return redirect(url_for('base'))
            else:
              if password == confirmpassword:
                b = otp_ver(phone)
                c.execute('insert into testApi (name,age,phone,username,password,Address,City,State,BodyTemperature,RunnyNose,BodyAche,DifficultyinBreathing,DryCough) values (%s, %s, %s, %s, md5(%s), %s, %s, %s, %s, %s, %s, %s, %s)', (name,age,phone,username,password,Address,City,State,BodyTemperature,RunnyNose,BodyAche,DifficultyinBreathing,DryCough ))
                db.commit()
                flash('Registered Successfully')
                c.close()
                db.close()
                return redirect(url_for('base'))
              else:
                flash('Passwords do not match!')
                return redirect(url_for('base'))
        else:
            flash("Please enter all the details.")
            return redirect(url_for('base'))
    else:
        return redirect(url_for('base'))

# Login
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form \
            and 'password' in request.form:
        try:
            username = request.form['username']
            password = request.form['password']
            db = get_db()
            c = db.cursor()
            c.execute('SELECT * from testApi WHERE username = %s and password = md5(%s)', (username, password))
            account = c.fetchone()

            if account is not None:
                session['logged_in'] = True
                session['id'] = account[0]
                session['name'] = account[1]
                session['phone'] = account[3]
                session['username'] = account[4]
                
                # Fever,BodyPain,Age,RunnyNose,DiffBreathing,DryCough
                inputFeatures = [account[9], account[11], account[2], account[10], account[12], account[13]]
                infProb = clf.predict_proba([inputFeatures])[0][1]
                ac = account[0]
                session['infection'] = round(infProb*100,3)
                #d = db.cursor()
                #d.execute('INSERT INTO infectionProb (idProb,ProbabilityInfection) VALUES (%s ,%s)', (ac , infProb))
                #c.execute('insert into testApi (name,age,phone,username,password,Address,City,State,BodyTemperature,RunnyNose,BodyAche,DifficultyinBreathing,DryCough) values (%s, %s, %s, %s, md5(%s), %s, %s, %s, %s, %s, %s, %s, %s)', (name,age,phone,username,password,Address,City,State,BodyTemperature,RunnyNose,BodyAche,DifficultyinBreathing,DryCough ))
                db.commit()
                c.close()
                #d.close()
                db.close()
                flash('Logged In Successfully')
                print(session)
                return redirect(url_for('base'))
            else:
                flash('Invalid credentials. Please try again.')
                return redirect(url_for('base'))
        except Exception as e:
            print(e)
        flash('An error occured. Please try again.')
        return redirect(url_for('base'))
    else:
        return redirect(url_for('base'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Logged Out Successfully')
    return redirect(url_for('base'))

'''
ERROR HANDLING
'''
@app.errorhandler(403)
def access_forbidden(error):
    return render_template('403.html'), 403


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)
