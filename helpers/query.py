def querys(modelo, querySQLModelo, querySQLNOModelo):
    if modelo != "":
        query = querySQLModelo
        #query_select_mysql = 'SELECT Button' + str(n) + '_Value     FROM opcua_client_db.test_result where test_result.Modelo="' + modelo + '" ORDER BY Id DESC limit 50'
    else:
        query = querySQLNOModelo
        #query_select_mysql = 'SELECT Button' + str(n) + '_Value FROM opcua_client_db.test_result ORDER BY Id DESC limit 200'
    return query
