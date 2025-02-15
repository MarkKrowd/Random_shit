# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:29:42 2019

@author: RMichaud
"""

import numpy as np

def ell2cart(a,e,lambda_deg,phi_deg,h):
    RN = a/(1-e**2*np.sin(phi_deg/180*np.pi)**2)**0.5
    x = (RN+h)*np.cos(phi_deg/180*np.pi)*np.cos(lambda_deg/180*np.pi)
    y = (RN+h)*np.cos(phi_deg/180*np.pi)*np.sin(lambda_deg/180*np.pi)
    z = (RN*(1-e**2)+h)*np.sin(phi_deg/180*np.pi)
    
    return x,y,z

def cart2ell(a,e,x,y,z):
    lambda_deg = np.arctan2(y,x)/np.pi*180
    
    hi = 0
    old_hi = 1
    RNi = 1
    
    while abs(hi-old_hi)>0.000001:
        old_hi = hi
        phi_i = np.arctan2(z,((x**2+y**2)**0.5)*(1-(RNi/(RNi+hi))*(e**2)))
        RNi = a/(1-((e**2)*((np.sin(phi_i))**2)))**0.5
        hi = ((x**2+y**2)**0.5/np.cos(phi_i))-RNi
        
    h = hi
    
    phi_deg = phi_i/np.pi*180
    return lambda_deg,phi_deg,h

a = 6378137
f = 1/298.257222101
b = a-a*f
e = (a**2-b**2)**0.5/a
c = e*a

x,y,z = ell2cart(a,e,8.5,46.5,500)
print(x,y,z)
print(cart2ell(a,e,x,y,z))
