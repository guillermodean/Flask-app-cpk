
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

mysql = mysql.MySQL(app, prefix="mysql",
                    user='calidad', password='Pamp3701', db='opcua_client_db', port="3306", host="10.73.83.220", autocommit=True)
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
    cursor.execute('SELECT * FROM opcua_client_db.results_cpk_ ORDER BY Id DESC;')
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
        flash('Resultado añadido correctamente','alert alert-primary')
    return redirect(url_for('addcpk'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('DELETE FROM `cpk-resultst` WHERE `id`={0}'.format(id))
    flash('borrado','alert alert-danger alert-dismissible fade show')
    return redirect(url_for('tablas'))

@app.route('/edit/<string:id>')
def edit(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM `cpk-resultst` WHERE `id`={0}'.format(id))
    data= cursor.fetchall()
    print(data[0])
    return render_template('Formulario_update.html',resultado=data[0])

@app.route('/update/<string:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        Button=request.form ['Button']
        seat=request.form ['seat']
        cpk=request.form ['cpk']
        cursor = mysql.get_db().cursor()
        cursor.execute('UPDATE `cpk-resultst` SET `Button`=%s,`seat`=%s,`cpk`=%s WHERE `id`=%s',(Button,seat,cpk,id))
        flash('modificado','alert alert-warning alert-dismissible fade show')
        return redirect(url_for('tablas'))

    


if __name__ == '__main__':
    # debug true lo que hace es que cada vez que cambie algo se reinicia
    app.run(debug=True, host='0.0.0.0')
