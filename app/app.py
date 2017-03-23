

from flask import Flask 
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from flask import jsonify
from flask import abort
from flask import session
from flask import escape
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = 'Ascds123/#fsd&%sadasdsa2234DSsfdw'
app.config['MONGO_DB'] = 'laramongo'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/laramongo'

mongo = PyMongo(app)
   

@app.route('/')
@app.route('/index')

def index():
     return render_template("home.html",title="Home",active_home="active")


@app.route('/user', methods=['GET'])
def user():
    if request.method == 'GET': 
            dbtest = mongo.db.test
            data = dbtest.find()

    return render_template("userall.html",title="User",active_user="active", x=data)



@app.route('/adduser', methods=['GET','POST'])
def adduser():     

    if request.method == 'POST':      
            dbtest = mongo.db.test
            nama = request.form['nama']
            usia = request.form['usia']
            alamat = request.form['alamat']           
            data = dbtest.insert_one({'nama' : nama,'usia' : usia,'alamat' : alamat})  
            pesan = flash('Suskes Add User')
            return redirect(url_for('user'))

    return render_template("useradd.html",title="User",active_user="active")
      

@app.route('/apiuser', methods=['GET'])
def apiuser():
    
    if request.method == 'GET':
        dbtest = mongo.db.test
        output = []
        for s in dbtest.find():
            output.append({'nama' : s['nama'], 'usia' : s['usia'],'alamat' : s['alamat'] })

    return jsonify(output)



if __name__ == "__main__":
    app.run()
