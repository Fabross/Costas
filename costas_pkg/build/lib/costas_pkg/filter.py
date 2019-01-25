"""Filter module.

The objective of this module is to classify each star by his light curve's
params obtained from features extraction module, filtering by a group of 
thresholds the stars that are not periodic large variable.

Authors: 
"""
from astropy.table import Table,join
import numpy as np

def grade_filter(data,grades):
    """Filter the data to preprocess and return a astropy.table.

    Keyword arguments:
    data -- the data to analyze, astropy.table
    grades -- the grades to analyze, tuple
    
    """
    data_aux = Table([grades], names=['GRADE'])
    res = join(data, data_aux, join_type='right')
    if (len(res)) == 0:
        print("there's no values asociated with "+str(grades)+" apertures, no table returned")
        return -1
    if res.masked:
        del res[res['HJD'].mask.nonzero()[0]]
    return res

def stars_Cfilter(data, ThC1=0.02, ThC2=0.02):
    """Filter the data by thresholds and return the filtered data as astropy.table.
    
    ThreshC1 -- the threshold for C1
    ThreshC2 -- the threshold for C2
    
    """
    return data[np.where((data['C1']>=ThC1)&(data['C2']>=ThC2))]
    
def stars_Qfilter(data, ThQ1=4, ThQ2=4):
    """Filter the data by thresholds and return the filtered data as astropy.table.
    
    ThreshC1 -- the threshold for C1
    ThreshC2 -- the threshold for C2
    
    """
    return data[np.where((data['Q1']>=ThQ1)&(data['Q2']>=ThQ2))]
