import math
import datetime
from helpers.calculos import cp, cpk, cpl, cpu
from helpers.interfaz import introducemodelo, modelovar
from helpers.query import querys
from helpers.conexion import conexion
from helpers.getdata import getdata
from helpers.graficar import graficar
from helpers.Tendencia_CPK import tendenciacpk
import time
import pandas as pd


while True:

    """I skip the interface to enter the model, taking all of them, leaving the model variable blank."""
    # introducemodelo()
    #modelo = modelovar()
    modelo = ''
    db = conexion()

    try:
        for i in range(13):  # Loop started for all the 13 buttons
            n = i + 1

            """ importation query from mysql """
            dataf, toli, tols, modelos, data = getdata(n, db, modelo)

            """ cp calculation n round values obtained """

            cp_sql = float(round(cp(dataf, tols, toli), 2))
            cpk_sql = float(round(cpk(dataf, tols, toli), 2))
            fcpu = round(cpu(dataf, tols), 2)
            fcpl = round(cpl(dataf, toli), 2)
            mean = round(dataf['valores'].mean(), 2)
            Button = modelos.iloc[0, 0]
            date = datetime.datetime.now()

            """ validation of the obtained values """

            if math.isnan(mean):
                mean = 0
            if math.isnan(cp_sql):
                cp_sql = 0
            if math.isnan(cpk_sql):
                cpk_sql = 0

            """ print the resulto to be uploaded """

            print(date, Button, mean, toli, tols, cp_sql, cpk_sql)

            """Save the data in the results table cpk"""

            query_insert = "INSERT  opcua_client_db.results_cpk_ (Date,Button,Media,Tol_inf,Tol_sup,cp,cpk,modelo) VALUES " \
                           "('" + str(
                               date) + "','" + Button + "','" + str(mean) + "','" + str(toli) + "','" + str(tols) + "','" + str(
                               cp_sql) + "','" + str(cpk_sql) + "','" + str(modelo) + "')"
            query_insert_nm = "INSERT  opcua_client_db.results_cpk_ (Date,Button,Media,Tol_inf,Tol_sup,cp,cpk,modelo) " \
                              "VALUES ('" + str(
                                  date) + "','" + Button + "','" + str(mean) + "','" + str(toli) + "','" + str(tols) + "','" + str(
                                  cp_sql) + "','" + str(cpk_sql) + "','todos')"
            query = querys(modelo, query_insert, query_insert_nm)
            cursor = db.cursor()
            cursor.execute(query)
            db.commit()

            recuento = len(dataf['valores'])

            """plot"""

            graficar(mean, Button, cpk_sql, cp_sql, recuento,
                     dataf, data, toli, tols, fcpl, fcpu, n)

            """ Trends captures previously measured results and graphs them from a set date """

            tendenciacpk(db, n)
        print('endoflines')
        time.sleep(86400)

    except ValueError:
        print('error total'+ValueError)
