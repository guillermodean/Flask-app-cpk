
from flask import Flask, url_for, redirect, flash
from flask import jsonify
from flask import render_template
from flask.wrappers import Request
from flaskext import mysql
from flask import request
import os
from products import products

app = Flask(__name__)

# MYSQL

mysql = mysql.MySQL(app, prefix="mysql1", host='localhost',
                    user='root', password='Guillermo11', db='cpk', autocommit=True)
mysql.init_app(app)

# Settings
app.secret_key = 'mysecretkey'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/templates/graficas')
def graficas():
    return render_template('graficas.html')


@app.route('/templates/tablas')
def tablas():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT `id`, `Button`, `seat`, `cpk` FROM `cpk-resultst`')
    data = cursor.fetchall()
    return render_template('tabla.html', resultados=data)


@app.route('/añadir_cpk')
def formulario():
    return render_template('Formulario.html')


@app.route('/añadir_cpk', methods=['POST'])
def addcpk():
    if request.method == 'POST':
        button = request.form['Button']
        seat = request.form['seat']
        cpk = request.form['cpk']
        cursor = mysql.get_db().cursor()
        cursor.execute(
            'INSERT INTO `cpk-resultst`(`Button`, `seat`, `cpk`) VALUES (%s,%s,%s)', (button, seat, cpk))
        flash('Resultado añadido correctamente')
    return redirect(url_for('addcpk'))


if __name__ == '__main__':
    # debug true lo que hace es que cada vez que cambie algo se reinicia
    app.run(debug=True, port=4000)
