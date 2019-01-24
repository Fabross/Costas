"""Preprocessing module.

The sets of functions here help from the perspective of preprocessing, complementing
the module of data gathering and features extraction.

Authors: 
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table,join
        
def outliers_iqr(data_col, aperture='0'):
    """Delete atypical data and return a astropy.table.

    Keyword argument:
    ys -- the data, {np.narray, astropy.table, astropy.table.column}
    aperture -- the aperture index, str
    
    """
    if (type(data_col)==Table):
        quartile_1, quartile_3 = np.percentile(data_col['MAG_'+aperture], [25,75])
        iqr = quartile_3 - quartile_1
        lower_bound = quartile_1 - (iqr*1.5)
        upper_bound = quartile_3 + (iqr*1.5)
        res = data_col[np.where((data_col['MAG_'+aperture] <= upper_bound) & (data_col['MAG_'+aperture] >= lower_bound))]
        res = join(res,data_col)
        
    else:
        quartile_1, quartile_3 = np.percentile(data_col, [25, 75])
        iqr = quartile_3 - quartile_1
        lower_bound = quartile_1 - (iqr*1.5)
        upper_bound = quartile_3 + (iqr*1.5)
        res = data_col[np.where((data_col <= upper_bound) & (data_col >= lower_bound))]
        if (type(data_col)==Table.Column):
            res = Table([res], names=(data_col.name,), dtype=('f8',))
            res.meta = data_col.meta
        else:
            res = Table([res], names=('MAG_'+'i', ))
    return res
        
def high_photometric_errors(data_col, aperture='0'):
    """Delete high photometric errors and return a astropy.table.

    Keyword argument:
    data -- the data to analyze, {np.narray, astropy.table, astropy.table.column}
    aperture -- the aperture index, str
    
    """
    if (type(data_col)==Table):    
        mer_mean = np.mean(data_col['MAG_'+aperture])
        mer_std = np.std(data_col['MAG_'+aperture])
        error_limit = mer_mean + 3*mer_std
        res = data_col[np.where(data_col['MAG_'+aperture] < error_limit)]
        res = join(res,data_col)
    else:
        mer_mean = np.mean(data_col)
        mer_std = np.std(data_col)
        error_limit = mer_mean + 3*mer_std
        res = data_col[np.where(data_col < error_limit)]
        if (type(data_col)==Table.Column):
            res = Table([res], names=(data_col.name,), dtype=('f8',))
            res.meta = data_col.meta
        else:
            res = Table([res], names=('MAG_'+'i', ))
    return res

# funcion que hace todo el preprocesamiento
def preprocessing(data,aperture):
    """Preprocess data for an aperture and return a astropy.table.

    Keyword arguments:
    data -- the data to analyze, {np.narray, astropy.table, astropy.table.column}
    aperture -- the aperture index, str
    
    """
    # 1 - se eliminan las mediciones con alto error fotometrico
    data_aux = high_photometric_errors(data,aperture)
    #2 - se eliminan datos atípicos
    data_aux = outliers_iqr(data_aux,aperture)
    # Se retornan los dias julianos y la magnitud de la apertura seleccionada
    return join(data, data_aux)
