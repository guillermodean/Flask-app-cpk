import mysql.connector as mysql
import json

ENTORNO = "LOCAL"

with open('../config.json', 'r') as file:
    config = json.load(file)

usuario = config[ENTORNO]['USER']
contraseña = config[ENTORNO]['PASS']
server=config[ENTORNO]['HOST']
database=config[ENTORNO]['DATABASE']


def conexion():
    try:
        db = mysql.connect(host=server, user=usuario,
                           password=contraseña, db=database)
        print("conectado")

    except mysql.Error as err:
        print('error de conexion ala BBDD' + str(err))
    return db
