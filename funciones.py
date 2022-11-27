# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:18:08 2022

@author: luish
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.stats as stats
import seaborn as sns
from sklearn.preprocessing import StandardScaler


def graficar_data_densidad(df, col1):
    """
        Funcion para graficar densidad de los datos del dataset
    """
    sns.set_style("dark")
    x = df[col1]
    ax = sns.distplot(x, color ='#20DF97')
    plt.title("Densidad-Histograma: " + str(col1))
    plt.show()
    


def getColumnsDataTypes(df):
    """
        Funcion para detectar tipo de variables
    """
    categoric_vars = []
    discrete_vars = []
    continues_vars = []

    for colname in df.columns:
        if(df[colname].dtype == 'object'):
            categoric_vars.append(colname)
        else:
            cantidad_valores = len(df[colname].value_counts())
            if(cantidad_valores <= 30):
                discrete_vars.append(colname)
            else:
                continues_vars.append(colname)

    return categoric_vars, discrete_vars, continues_vars



def plot_density_variable(df, col1):
    """
        Funcion para graficar variables categorias del dataset
    """
    plt.figure(figsize = (15,6))
    plt.subplot(121)
    df[col1].hist(bins=30)
    plt.title(col1)
    
    plt.subplot(122)
    stats.probplot(df[col1], dist="norm", plot=plt)
    plt.show()


def FillNaN_Corr_DF(df, col1, col2):
    """
        Funcion para imputacion de valores nulos
    """
    mean_val = np.round(df[col1].mean(), 0)
    print(f'La media es: {mean_val}')
    median_val = np.round(df[col1].median(), 0)
    print(f'La mediana es: {median_val}')
    df_LF_meanImp = df[col1].fillna(mean_val)
    df_LF_meadianImp = df[col1].fillna(median_val)
    corr1 = np.corrcoef(df_LF_meanImp, df[col2])[0,1]
    corr2 = np.corrcoef(df_LF_meadianImp, df[col2])[0,1]
    print(corr1)
    print(corr2)
    if corr1 >= corr2:
        df[col1] = df[col1].fillna(mean_val)
    else:
        df[col1] = df[col1].fillna(median_val)
    print('Validacion Valores Nulos:')
    print(df[col1].isnull().sum())