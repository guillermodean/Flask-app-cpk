import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from helpers.calculos import boxplot
from helpers.calculos import graficamedias
from helpers.calculos import filtraryjuntar
from helpers.calculos import means
from helpers.conexion import conexion

familias = pd.read_csv('helpers/familias.csv', sep=';',
                       names=['modeloISRI', 'Modelo', 'nombre', 'familia'])
query = 'SELECT * FROM opcua_client_db.test_result  ORDER BY Id DESC'
data = pd.read_sql(query, con=conexion())
date = '2021-01-01'

graficamedias(data, date, familias)
data = filtraryjuntar(data, date, familias)
databoxplot = boxplot(data, )
datafamily = means(data, )
# corr=correlation(data)
# sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)

for i in range(13):
    a = i + 1
    datacol = data['Button' + str(a) + '_Value']
    datacol = datacol.replace(0, np.nan)
    datacol = datacol.dropna(how='all', axis=0)
    x = pd.Series(datacol, name='Button' + str(a) + '_Value')
    datafamily1 = (datafamily['Button' + str(a) + '_Value'])
    recuento = len(datafamily1)
    datafamily1 = datafamily1.dropna(how='all', axis=0)
    fig, axes = plt.subplots(1, 3, figsize=(10, 5))
    fig.suptitle('Button' + str(a) + '_Value')
    axes[0].set_title('DIST')
    axes[1].set_title('BOX')

    for label, content in datafamily1.items():
        df = content.to_frame()
        df = df.dropna(how='all', axis=0)
        count = len(df)
        name = label
        axes[2].set_title('DIST_FAM N=' + str(count))
        ax2 = sns.distplot(df, ax=axes[2], label=label, hist=False)
        ax = sns.distplot(x, ax=axes[0])
        ax1 = sns.boxplot(ax=axes[1], data=databoxplot,
                          x='familia', y=('Button' + str(a) + '_Value'))
        ax2.legend()
plt.show()
