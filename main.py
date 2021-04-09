import csv
import lib.pandas as pd
import requests
from lib.flask import Flask,render_template,request,redirect,Response,flash,url_for
#from lib.flask_table import Table, Col
import os     
import sys
from datetime import datetime
CSV_URL = 'https://api.covidtracking.com/v1/states/current.csv'
data=pd.read_csv(CSV_URL)
#print(data.head(1))
#cursor = connection.cursor()  
#app=Flask(__name__, template_folder='templates/')
#if getattr(sys, 'frozen', False):
    #template_folder = os.path.join(sys._MEIPASS, 'templates')
    #static_folder = os.path.join(sys._MEIPASS, 'static')
    #app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
#else:
app = Flask(__name__)
#ui = FlaskUI(app)

#app.config['']
@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/info',methods=['POST','GET'])
def info():
    if request.method == 'POST':
        Sname = request.form['Sname']
        print(Sname)
        Dbase = request.form['Dbase']
        data1=data[(data['state']=='FL') & (data['date']==20210307)]   
        #table = Table(data1)     
        return  render_template('view.html',tables=[data1.to_html(classes='female')],
    titles = ['na', 'Covid Imporamation for '+Sname])
    else:
        return("Bad request please verify the input values.")
#Response (data1.to_json(orient='split'))

if __name__ =="__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True)