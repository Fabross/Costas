"""Classification module.

The objective of this module is to classify each star by his light curve's
params obtained from features extraction module, filtering by a group of 
thresholds the stars that are not large period variable.

Authors: 
"""

import pandas as pd
import numpy as np

def grades():
    """Ask for grades to keyboard input and return a list with the keyboard input."""
    try:
        grades = input('Select GRADE, usage "A,B,..." with valid options A,B,C,D: ')
        if not(set(grades.split(",")) <= {'A','B','C','D'}):
            raise ValueError(grades)
        return grades.split(",")
    except ValueError:
        print("incorrect GRADE, ingressed: ",grades)
        raise
        
def mags():
    """Ask for magnitudes to keyboard input and return a tuple."""
    try:
        mags = input('Select MAG, usage MAG_2,MAG_0,MAG_1,MAG_3,MAG_4 like 0,0,1,0,0 for only MAG_1 with full weight: ')
        if (int(max(set(mags.split(",")))) > 1):
            raise ValueError(mags)
        return tuple(mags.split(","))
    except ValueError:
        print("incorrect MAG, ingressed: ",mags)
        raise
        
def stars_filter(data, ThreshQ1, ThreshC1, ThreshQ2, ThreshC2):
    """Filter the data by thresholds and return the filtered data as pd.DataFrame.

    Keyword arguments:
    data -- the data to analyze, pd.DataFrame
    ThreshQ1 -- the threshold for Q1
    ThreshC1 -- the threshold for C1
    ThreshQ2 -- the threshold for Q2
    ThreshC2 -- the threshold for C2
    """
    return data[(data['Q1']>=ThreshQ1)&(data['C1']>ThreshC1)&(data['Q2']>=ThreshQ2)&(data['C2']>ThreshC2)]
