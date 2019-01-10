# PREPROCESSING
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def grades():
    try:
        grades = input('Select GRADE, usage "A,B,..." with valid options A,B,C,D: ')
        if not(set(grades.split(",")) <= {'A','B','C','D'}):
            raise ValueError(grades)
        return grades.split(",")
    except ValueError:
        print("incorrect GRADE, ingressed: ",grades)
        raise
        
def mags():
    try:
        mags = input('Select MAG, usage MAG_2,MAG_0,MAG_1,MAG_3,MAG_4 like 0,0,1,0,0 for only MAG_1 with full weight: ')
        if (int(max(set(mags.split(",")))) > 1):
            raise ValueError(mags)
        return tuple(mags.split(","))
    except ValueError:
        print("incorrect MAG, ingressed: ",mags)
        raise
        
def outliers_iqr(ys):
	quartile_1, quartile_3 = np.percentile(ys, [25, 75])
	iqr = quartile_3 - quartile_1
	lower_bound = quartile_1 - (iqr*1.5)
	upper_bound = quartile_3 + (iqr*1.5)
	return np.where((ys > upper_bound) | (ys < lower_bound))
        
def high_photometric_errors(data):
	mer_mean = np.mean(data)
	mer_std = np.std(data)
	error_limit = mer_mean + 3*mer_std
	return np.where((data >= error_limit))

# funcion que hace todo el preprocesamiento
def preprocessing(data,aperture):
	# 1 - se eliminan las mediciones con alto error fotometrico
	hpe_index = high_photometric_errors(data["MER_"+aperture].values)
	data = data.drop(data.index[hpe_index[0]])
	#2 - se eliminan datos atípicos
	outliers_index = outliers_iqr(data["MAG_"+aperture].values)
	data = data.drop(data.index[outliers_index[0]])
	# Se retornan los dias julianos y la magnitud de la apertura seleccionada
	return data["HJD"].values.ravel(),data["MAG_"+aperture].values.ravel()

def grade_filter(df,grades,mags):
    mask = df['GRADE'].isin(grades).all(1)
    res = df[mask]
    for i in mags:
        if (int(i)!=0):
            data = preprocessing(res,i)
    return data

def Sort(tup): 
    # reverse = True (Sorts in Descending order) 
    # key is set to sort using float elements 
    # lambda has been used 
    return(sorted(tup, key = lambda x: float(x[0]), reverse = True)) 
        
def graph(res,number,filename):
    res = Sort(res)
    fig, ax = plt.subplots()
    ax.scatter(res[0],res[1])
    ax.set(xlabel='HJD', ylabel='Magnitude',
           title=filename)
    ax.grid()
    fig.savefig("test/test"+str(number)+".png")
