import mysql.connector as mysql
import json

ENTORNO = "produccion"

with open('./helpers/config.json', 'r') as file:
    config = json.load(file)

usuario = config[ENTORNO]['user']
contraseña = config[ENTORNO]['password']


def conexion():
    try:
        db = mysql.connect(host='10.73.83.220', user=usuario,
                           password=contraseña, db='opcua_client_db')
        print("conectado")

    except mysql.Error as err:
        print('error de conexion ala BBDD' + str(err))
    return db
