"""Data acquisition module.

The sets of functions here help to gather the data from the source.

Authors: 
"""

import re
import numpy as np
from astropy.table import Table,vstack,join

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
    """Transform data from source txt to an structure and return a astropy.table.

    Keyword arguments:
    data -- the data to transform, list
    
    """
    c = []
    alpha = []
    gamma = []
    flag = 0
    flag1 = False
    typ= ('f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8',np.str,'f8',np.str,np.str)
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
                        col[0].append('RA')
                        col[0].append('DEC')
                        reg = np.c_[reg,np.array(alpha),np.array(gamma)]
                        t = Table(reg, names=tuple(col[0]), dtype = typ)
                        c = []
                        alpha = []
                        gamma = []
                        flag += 1
                    else:
                        col[0].append('RA')
                        col[0].append('DEC')
                        reg = np.c_[reg,np.array(alpha),np.array(gamma)]
                        t_aux = Table(reg, names=tuple(col[0]), dtype = typ)
                        t = vstack([t, t_aux])
                        c = []
                        alpha = []
                        gamma = []

            except:
                reg, col = cut(c)
                if flag == 0:
                    col[0].append('RA')
                    col[0].append('DEC')
                    reg = np.c_[reg,np.array(alpha),np.array(gamma)]
                    t = Table(reg, names=tuple(col[0]), dtype = typ)
                    c = []
                    alpha = []
                    gamma = []
                    flag += 1   
                else:
                    col[0].append('RA')
                    col[0].append('DEC')
                    reg = np.c_[reg,np.array(alpha),np.array(gamma)]
                    t_aux = Table(reg, names=tuple(col[0]), dtype = typ)
                    t = vstack([t, t_aux])
    file.close()