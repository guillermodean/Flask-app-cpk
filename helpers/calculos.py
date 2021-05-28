import numpy as np


def cp(mylist, usl, lsl):  # calculo capacidad del equipo a partir de una lista el limite inferior y el limite superior
    sigma = mylist.std(axis=0)
    sigma = (float(sigma))
    if sigma == 0:
        cp = 0
        return cp
    else:
        print('sigma= ' + str(sigma) + ' usl' + str(usl) +
              ' lsl' + str(lsl) + ' resta' + str(float(usl - lsl)))
        cp = float(usl - lsl) / (6 * sigma)
        return cp


def filtrar(data):  # removes zeros and values that fall outside the quantiles 15%
    # quitar ceros y nulos TODO dropna y que coja mas datos. no dejar los ceros
    datafiltered = data[(data != 0)]
    Q1 = datafiltered.quantile(0.15)
    Q3 = datafiltered.quantile(0.85)
    IQR = Q3 - Q1
    data_noutliers = datafiltered[~((datafiltered < (
        Q1 - 1.5 * IQR)) | (datafiltered > (Q3 + 1.5 * IQR))).any(axis=1)]
    return data_noutliers


def cpk(mylist, usl, lsl):  # calculation of the process capacity from a list, the lower limit and the upper limit
    sigma = mylist.std(axis=0)
    sigma = (float(sigma))
    if sigma == 0:
        cpk = 0
        return cpk
    else:
        m = mylist['valores'].mean()
        Cpu = float(usl - m) / (3 * sigma)
        Cpl = float(m - lsl) / (3 * sigma)
        cpk = np.min([Cpu, Cpl])
        return cpk


def cpu(mylist, usl):  # calculation of the process capacity based on its upper limit
    sigma = mylist.std(axis=0)
    sigma = (float(sigma))
    if sigma == 0:
        cpu = 0
        return cpu
    else:
        m = mylist['valores'].mean()
        Cpu = m + (sigma * 3)
        return Cpu


def cpl(mylist, lsl):  # calculation of the process capacity based on its lower limit
    sigma = mylist.std(axis=0)
    sigma = (float(sigma))
    if sigma == 0:
        cpl = 0
        return cpl
    else:
        m = mylist['valores'].mean()
        Cpl = m - (sigma * 3)
        return Cpl


def filtraryjuntar(data, fecha, familias):
    datafecha = data[data['Date'] > fecha]
    data = datafecha.merge(familias, on='Modelo')
    return data


def means(data):
    dataall = data.drop(['Id'], axis=1)
    dataall = dataall[
        ['Modelo', 'familia', 'Button1_Value', 'Button2_Value', 'Button3_Value', 'Button4_Value', 'Button5_Value',
         'Button6_Value', 'Button7_Value', 'Button8_Value', 'Button9_Value', 'Button10_Value', 'Button11_Value',
         'Button12_Value', 'Button13_Value']]
    dataxfamilia = dataall.pivot(columns='familia',
                                 values=['Button1_Value', 'Button2_Value', 'Button3_Value', 'Button4_Value',
                                         'Button5_Value', 'Button6_Value', 'Button7_Value', 'Button8_Value',
                                         'Button9_Value', 'Button10_Value', 'Button11_Value', 'Button12_Value',
                                         'Button13_Value'])
    return dataxfamilia


def graficamedias(data, date, familias):
    datafecha = data[data['Date'] > date]
    dataall = datafecha.merge(familias, on='Modelo')
    dataall = dataall.drop(['Id'], axis=1)
    dataporfamilia = dataall.groupby(['familia']).agg(['mean', 'std', 'size'])
    dataporfamilia.to_csv('medias.csv', sep=';')
    return dataporfamilia


def boxplot(data):
    dataf = data.drop(columns=['Button1_State', 'Button2_State', 'Button3_State', 'Button4_State', 'Button5_State',
                               'Button6_State', 'Button7_State', 'Button8_State', 'Button9_State', 'Button10_State',
                               'Button11_State', 'Button12_State', 'Button13_State', 'Side', 'Resultado_OK',
                               'Isri_Order', 'Id'])
    return dataf


def correlation(data):
    cols = ['Button1_Value', 'Button2_Value', 'Button3_Value', 'Button4_Value', 'Button5_Value', 'Button6_Value',
            'Button7_Value', 'Button8_Value', 'Button9_Value', 'Button10_Value', 'Button11_Value', 'Button12_Value',
            'Button13_Value']
    data[cols] = data[cols].replace({0: np.nan})
    datapivotf = data.pivot_table(data, columns='familia')
    print(datapivotf)
    corr = datapivotf.corr()
    print(corr)
    return corr
