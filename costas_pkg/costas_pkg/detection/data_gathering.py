"""Data gathering module.

The sets of functions here help to gather the data from the source.

Authors: 
"""

import re
import numpy as np
import pandas as pd


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
		
def cut(c):
    """Cut the data by a patron defined and return a tuple.

    Keyword arguments:
    data -- the data to cut, list
    
    """
    flag = True
    data = []
    head = []
    patron = re.compile("\s+")
    for i in c:
        if flag == True:
            head.append(patron.split(i))
            flag = False
        else:
            data.append(patron.split(i))
    return np.array(data),head

def parser(data):
    """Transform data from source txt to an structure and return a pd.DataFrame.

    Keyword arguments:
    data -- the data to transform, list
    
    """
    c = []
    alpha = []
    gamma = []
    flag = 0
    flag1 = False
    for i in range(len(data)):
        flag1= re.findall("\# ######### LIGHT ",data[i])
        if flag1:
            data= data[i+1:]
            break
    for i in range(len(data)):
        head = re.findall("\A#\s+(.+)",data[i])
        new_line = re.findall("\A   (.+)",data[i]) 
        ra = re.findall("\#ra=\s+(.+)",data[i])
        dec = re.findall("\#dec=\s+(.+)",data[i])

        if ra:
            ra_aux = ra
        if dec:
            dec_aux = dec
        if head:
            [c.append(j) for j in head]
        if new_line:
            [c.append(k) for k in new_line]
            alpha.append(ra_aux)
            gamma.append(dec_aux)
            try:
                next_line = re.findall("\A   (.+)",data[i+1])
                if not next_line:
                    reg, col= cut(c)
                    if flag == 0:
                        print('cut: in: '+str(type(c))+', out:'+str(type(cut(c))))
                        df = pd.DataFrame(reg,columns=col)
                        df["RA"] = np.array(alpha)
                        df["DEC"] = np.array(gamma)
                        c = []
                        alpha = []
                        gamma = []
                        flag += 1                    
                    else:
                        df_aux = pd.DataFrame(reg,columns=col)
                        df_aux["RA"] = np.array(alpha)
                        df_aux["DEC"] = np.array(gamma)
                        df = pd.concat([df,df_aux],ignore_index=True)
                        c = []
                        alpha = []
                        gamma = []

            except:
                reg, col = cut(c)
                if flag == 0:
                    df = pd.DataFrame(reg,columns=col)
                    df["RA"] = np.array(alpha)
                    df["DEC"] = np.array(gamma)
                    c = []
                    alpha = []
                    gamma = []
                    flag += 1   
                else:    
                    df_aux = pd.DataFrame(reg,columns=col)
                    df_aux["RA"] = np.array(alpha)
                    df_aux["DEC"] = np.array(gamma)
                    df = pd.concat([df,df_aux],ignore_index=True)

    col[0].remove('GRADE')
    df[col[0]] = df[col[0]].astype(float)

    return df