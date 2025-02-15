# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:52:03 2019

@author: RMichaud
"""

import numpy as np

def Cardan2R3D(alpha_deg,beta_deg,gamma_deg):
    alpha_rad = alpha_deg/180*np.pi
    beta_rad = beta_deg/180*np.pi
    gamma_rad = gamma_deg/180*np.pi
    Rz = np.array([[np.cos(gamma_rad),np.sin(gamma_rad),0],
            [-np.sin(gamma_rad),np.cos(gamma_rad),0],
            [0,0,1]])
    Ry = np.array([[np.cos(beta_rad),0,-np.sin(beta_rad)],
            [0,1,0],
            [np.sin(beta_rad),0,np.cos(beta_rad)]])
    Rx = np.array([[1,0,0],
            [0,np.cos(alpha_rad),np.sin(alpha_rad)],
            [0,-np.sin(alpha_rad),np.cos(alpha_rad)]])
    R = Rz@Ry@Rx
    return R

print(Cardan2R3D(10,20,30))
