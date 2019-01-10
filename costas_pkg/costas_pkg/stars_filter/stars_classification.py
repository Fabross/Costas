# FILTER OF NOT LARGE VARIABLE STARS
import pandas as pd
import os

###########################Principal function green box#############################
# usage: path = directory path with data
# ThreshQ1, ThreshC1, ThreshQ2, ThreshC2 are the threshold used in final stage
# optional: when "stop" archives were opened -> stop, if 0 open all archives in path
def green_box(path,ThreshQ1, ThreshC1, ThreshQ2, ThreshC2,stop=0):
    grad = grades()
    mag = mags()
    counter = 0
    row= []
    col= ["ASAS NAME","RA","DEC","Q1","C1","Q2","C2"]
    
    for filename in os.listdir(path):
        file = open(path+filename,"r")
        text = file.readlines()
        df = parser(text)
        file.close()
        res = grade_filter(df,grad,mag)
        counter+=1
        #graph(res,counter,filename)
        stats = get_statistics(res[0],res[1])
        ra,dec= get_ra_dec(df)
        row.append([filename,ra,dec,stats[0],stats[1],stats[2],stats[3]])
        
        if ((stop>0)&(stop==counter)):
            break
    data = pd.DataFrame(row,columns=col)
    return data[(data['Q1']>=ThreshQ1)&(data['C1']>ThreshC1)&(data['Q2']>=ThreshQ2)&(data['C2']>ThreshC2)]

####################################################################################
