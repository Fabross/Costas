"""Features extraction module.

The objective of this module is analyze the preprocessed light curves.

Authors: 
"""

from scipy.optimize import curve_fit
import numpy as np
import pandas as pd

def lineal_fit(t,a,b):
    """Lineal fit to data and return param m np.narray.

    Keyword arguments:
    t -- A np.narray
    a -- A float
    b -- A float
    
    """
    m = a+b*t
    return m

def parabolic_fit(t,a,b,c):
    """Parabolic fit to data and return param m np.narray.

    Keyword arguments:
    t -- A np.narray
    a -- A float
    b -- A float
    c -- A float
    
    """
    m = a + b*t + c*t*t
    return m

# Por ahora fit puede ser lineal o parabolico
def get_statistics(t,y):
    """Obtain and return Q1', C1, Q2' and C2.

    Keyword arguments:
    t -- A np.narray
    y -- A np.narray
    
    """
    # Desviacion estandar y
    dep = np.std(y)
    #para fit lineal
    poptl, pcovl = curve_fit(lineal_fit, t, y)
    y_hatl = lineal_fit(t,*poptl)
    perrl = np.sqrt(np.diag(pcovl))
    defl = np.sqrt(np.sum((y_hatl- y)*(y_hatl- y))/len(y))
    q1 = poptl[1]/perrl[1]
    c1 = 1-(defl/dep)
    # Para fit parabolico
    poptp, pcovp = curve_fit(parabolic_fit, t, y)
    y_hatp = parabolic_fit(t,*poptp)
    perrp = np.sqrt(np.diag(pcovp))
    defp = np.sqrt(np.sum((y_hatp- y)*(y_hatp- y))/len(y))
    q2 = poptp[2]/perrp[2]
    c2 = 1-(defp/defl)
    stat = [q1,c1,q2,c2]
    return stat

def get_ra_dec(data):
    """Obtain and return RA and DEC, both str.
    
    RA is the Right Ascencion.
    DEC is the Declination.

    Keyword arguments:
    data -- the data to analyze, pd.DataFrame
    
    """
    ra= data.iloc[0]["RA"].values[0]
    ra= ra.split(" ")
    dec= data.iloc[0]["DEC"].values[0]
    dec= dec.split(" ")
    return ra[0],dec[0]
