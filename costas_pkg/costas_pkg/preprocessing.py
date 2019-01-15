"""Preprocessing module.

The sets of functions here help from the perspective of preprocessing, complementing
the module of data gathering and features extraction.

Authors: 
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
        
def outliers_iqr(ys):
    """Delete atypical data.

    Keyword argument:
    ys -- the data, np.narray
    
    """
    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr*1.5)
    upper_bound = quartile_3 + (iqr*1.5)
    return np.where((ys > upper_bound) | (ys < lower_bound))
        
def high_photometric_errors(data):
    """Delete high photometric errors and return a np.narray.

    Keyword argument:
    data -- the data to analyze, np.narray
    
    """
    mer_mean = np.mean(data)
    mer_std = np.std(data)
    error_limit = mer_mean + 3*mer_std
    return np.where((data >= error_limit))

# funcion que hace todo el preprocesamiento
def preprocessing(data,aperture):
    """Preprocess data for an aperture and return a tuple.

    Keyword arguments:
    data -- the data to analyze, pd.DataFrame
    aperture -- the aperture index, str
    
    """
    # 1 - se eliminan las mediciones con alto error fotometrico
    hpe_index = high_photometric_errors(data["MER_"+aperture].values)
    data = data.drop(data.index[hpe_index[0]])
    #2 - se eliminan datos atípicos
    outliers_index = outliers_iqr(data["MAG_"+aperture].values)
    data = data.drop(data.index[outliers_index[0]])
    # Se retornan los dias julianos y la magnitud de la apertura seleccionada
    return data["HJD"].values.ravel(),data["MAG_"+aperture].values.ravel()

def grade_filter(df,grades,mags):
    """Filter the data to preprocess and return a tuple.

    Keyword arguments:
    df -- the data to analyze, pd.DataFrame
    grades -- the grades to analyze, list
    mags -- the magnitudes to analyze, tuple
    
    """
    mask = df['GRADE'].isin(grades).all(1)
    res = df[mask]
    for i in mags:
        if (int(i)!=0):
            data = preprocessing(res,i)
    return data

def Sort(tup):
    """Sort a tuple in descending order and return a tuple.

    Keyword arguments:
    tup -- tuple to sort, tuple
    
    """
    # reverse = True (Sorts in Descending order)
    return(sorted(tup, key = lambda x: float(x[0]), reverse = True))
        
def graph(data,path,title):
    """Graph in a scatter type and save to a folder.

    Keyword arguments:
    data -- the data to graph, tuple
    path -- the path to save, str
    title -- the graph title, str
    
    """
    data = Sort(data)
    fig, ax = plt.subplots()
    ax.scatter(data[0],data[1])
    ax.set(xlabel='HJD', ylabel='Magnitude',
           title=title)
    ax.grid()
    fig.savefig(path+"/"+title+"_fig.png")
