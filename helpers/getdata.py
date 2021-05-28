from helpers.query import querys
import pandas as pd
from helpers.calculos import filtrar


def getdata(n, db, modelo):
    '''mysql query data'''

    query_select_mysql = 'SELECT Button' + str(n) + '_Value     FROM opcua_client_db.test_result where test_result.Modelo="' + modelo + '" ORDER BY Id ' \
        'DESC limit 50 '
    query_select_mysql_nm = 'SELECT Button' + str(
        n) + '_Value FROM opcua_client_db.test_result ORDER BY Id DESC limit 50'
    query = querys(modelo, query_select_mysql, query_select_mysql_nm)
    data = pd.read_sql(query, con=db)
    data.columns = ['valores']
    dataf = filtrar(data)

    '''mysql select modelos'''

    query_modelos_mysql = "SELECT Button, tol_inf_n, tol_sup_n FROM modelos WHERE Button='Button" + str(
        n) + "_Value' AND Modelo='" + str(modelo) + "'"
    query_modelos_mysql_nm = "SELECT Button, tol_inf_n, tol_sup_n FROM modelos WHERE Button='Button" + str(
        n) + "_Value' AND Modelo='TODOS'"
    query = querys(modelo, query_modelos_mysql, query_modelos_mysql_nm)
    modelos = pd.read_sql(query, con=db)
    toli = modelos.iloc[0, 1]
    tols = modelos.iloc[0, 2]
    if modelo == 'P5802450411':  # for this model we have different tolerances
        if n == 2:
            dataf = dataf[dataf > 40]
            dataf = dataf[dataf < 80]
        else:
            dataf = dataf
    else:
        dataf = dataf
    return dataf, toli, tols, modelos, data
