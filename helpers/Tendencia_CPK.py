import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def tendenciacpk(db, n):
    querycpk = "SELECT Button,Date,cpk  FROM opcua_client_db.results_cpk_ WHERE Button='Button" + str(
        n) + "_Value' ORDER BY Id DESC"
    cpkten = pd.read_sql(querycpk, con=db)
    cpkten = cpkten[cpkten['Date'] > '2021-05-13']
    x = cpkten['Date']
    y = cpkten['cpk']
    z = [1.66] * len(cpkten['Date'])
    fig = plt.figure(figsize=(8, 5))
    plt.title('Button' + str(n) + '_Value')
    plt.xlabel('Date')
    plt.ylabel('cpk')
    plt.plot(x, y)
    plt.plot(x, z, color='red', linestyle='--')
    my_file = 'cpk_graph+' + str(n) + '.png'
    # plt.show()
    fig.savefig('graphs/cpk' + my_file)
