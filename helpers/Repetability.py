import pandas as pd
from scipy.stats import f_oneway

df = pd.read_csv('MáquinaSensor.csv', sep=";")

df = df[['Referencia', 'Resistencia1', 'Resistencia2']]
df.describe()
df1 = df.pivot(columns='Referencia', values='Resistencia2')
print(df1.describe())
df1.to_csv('Resistencia2')
print(f_oneway(df1['812737-06/00'].dropna(axis=0), df1['812742-06/00'].dropna(axis=0),
               df1['813235-06/00'].dropna(axis=0)))

""" if the p value is greater than 0.05 Differences between the means are not statistically significant """

df2 = df.pivot(columns='Referencia', values='Resistencia1')
print(df2.describe())
df2.to_csv('Resistencia1.csv')
print(f_oneway(df2['812737-06/00'].dropna(axis=0),
      df2['812742-06/00'].dropna(axis=0), ))
