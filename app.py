from flask import Flask, url_for, redirect, flash
from flask import render_template
from flaskext import mysql
from flask import request
import json
from helpers import calculo_cp_sql

ENTORNO = "PRODUCCION"  # produccion

####### Obtener las variables de acceso #######

with open('config.json', 'r') as file:
    config = json.load(file)

server = config[ENTORNO]['HOST']
database = config[ENTORNO]['DATABASE']
username = config[ENTORNO]['USER']
password = config[ENTORNO]['PASS']
table = config[ENTORNO]['TABLE']

app = Flask(__name__)

# MYSQL

mysql = mysql.MySQL(app, prefix="mysql",
                    user=username, password=password, db=database, port="3306", host=server, autocommit=True)
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
    cursor.execute('SELECT * FROM `' + str(table) + '` ORDER BY Id DESC;')
    data = cursor.fetchall()
    return render_template('tabla.html', resultados=data)


@app.route('/añadir_cpk')
def formulario():
    return render_template('Formulario.html')


@app.route('/añadir_cpk', methods=['POST'])
def addcpk():
    if request.method == 'POST':
        date = request.form['Date']
        button = request.form['Button']
        media = request.form['Media']
        tol_inf = request.form['Tol_inf']
        tol_sup = request.form['Tol_sup']
        cp = request.form['cp']
        cpk = request.form['cpk']
        modelo = request.form['modelo']
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO `' + str(
            table) + '`(`Date`,`Button`, `Media`, `Tol_inf`,`Tol_sup`,`cp`,`cpk`,`modelo`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
                       (date, button, media, tol_inf, tol_sup, cp, cpk, modelo))
        flash('Resultado añadido correctamente', 'alert alert-primary')
    return redirect(url_for('addcpk'))


@app.route('/delete/<string:id>')
def delete(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('DELETE FROM `' + str(table) + '` WHERE `Id`={0}'.format(id))
    flash('borrado', 'alert alert-danger alert-dismissible fade show')
    return redirect(url_for('tablas'))


@app.route('/run-script')
def run_script():
    try:
        message = calculo_cp_sql.run_cpk_script()  # TODO ver si la mierda de flask puede llamar al script como estoy haciendo ahora
        flash(message)
    except TypeError:
        print("la movida es: "+TypeError)
    return redirect(url_for('tablas'))


@app.route('/edit/<string:id>')
def edit(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM `' + str(table) + '` WHERE `Id`={0}'.format(id))
    data = cursor.fetchall()
    print(data[0])
    return render_template('Formulario_update.html', resultado=data[0])


@app.route('/update/<string:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        Date = request.form['Date']
        Button = request.form['Button']
        Media = request.form['Media']
        cpk = request.form['cpk']
        cp = request.form['cp']
        modelo = request.form['modelo']
        Tol_inf = request.form['Tol_inf']
        Tol_sup = request.form['Tol_sup']
        cursor = mysql.get_db().cursor()
        cursor.execute('UPDATE `' + str(
            table) + '` SET `Date`=%s,`Button`=%s,`Media`=%s,`Tol_inf`=%s,`Tol_sup`=%s,`cp`=%s,`cpk`=%s,`modelo`=%s WHERE `id`=%s',
                       (Date, Button, Media, Tol_inf, Tol_sup, cp, cpk, modelo, id))
        flash('modificado', 'alert alert-warning alert-dismissible fade show')
        return redirect(url_for('tablas'))


if __name__ == '__main__':
    # debug true lo que hace es que cada vez que cambie algo se reinicia
    app.run(debug=True, host='0.0.0.0')
