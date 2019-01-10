# FEATURES EXTRACTION
import numpy as np
import pandas as pd
import os

from scipy.optimize import curve_fit

def lineal_fit(t,a,b):
	m = a+b*t
	return m

def parabolic_fit(t,a,b,c):
	m = a + b*t + c*t*t
	return m

# Por ahora fit puede ser lineal o parabolico
def get_statistics(t,y):
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
	ra= data.iloc[0]["RA"].values[0]
	ra= ra.split(" ")
	dec= data.iloc[0]["DEC"].values[0]
	dec= dec.split(" ")
	return ra[0],dec[0]
