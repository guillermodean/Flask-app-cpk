
from flask import Flask
from flask import jsonify
from flask import render_template
from flask.wrappers import Request
from flaskext import mysql
from flask import request
import os

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='Guillermo11'
app.config['MYSQL_DATABASE_DB']='cpk'

#mysql= mysql.MySQL(app)
mysql = mysql.MySQL(app, prefix="mysql1", host='localhost', user='root',password='Guillermo11',db='cpk', autocommit=True)
mysql.init_app(app)

from products import products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/templates/graficas')
def graficas():
    return render_template('graficas.html')

@app.route('/templates/tablas')
def tablas():
    return render_template('tabla.html')

@app.route('/añadir_cpk')
def formulario():
    return render_template('Formulario.html')

@app.route('/añadir_cpk',methods =['POST'])
def addcpk():
    if request.method=='POST':
        button = request.form['Button']
        seat = request.form['seat']
        cpk = request.form ['cpk']
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO `cpk-resultst`(`Button`, `seat`, `cpk`) VALUES (%s,%s,%s)',(button,seat,cpk))

    return 'received'


#PARA LANZAR LOS USUARIOS Y LAS CONEXIONES

# @app.route('/ping')
# def ping():
#     return jsonify({"message": "pong"})

# @app.route('/products')
# def getProducts():
#     return jsonify({"products": products, "message": "product list"})

# @app.route('/products/<string:product_name>')
# def getProduct():
#     return jsonify({""})

if __name__ == '__main__':
    app.run(debug=True, port=4000) #debug true lo que hace es que cada vez que cambie algo se reinicia