import numpy as np
#importation de script 3D de l'autre fichier
import modele_plot3D as plt3D
import matplotlib.pyplot as plt

#création des listes x,y,z pour l'équateur

def sph2cart(lon_deg,lat_deg,r):
    
    lon_rad = lon_deg*np.pi/180
    lat_rad = lat_deg*np.pi/180
    
    x = r*np.cos(lat_rad)*np.cos(lon_rad)
    y = r*np.cos(lat_rad)*np.sin(lon_rad)
    z = r*np.sin(lat_rad)
           
    return x,y,z

def equateur():
    
    list_x = []
    list_y = []
    list_z = []
    
    lat_deg = 0.0
    r = 1
    
    for lon_deg in range(0,360):
        x,y,z = sph2cart(lon_deg,lat_deg,r)
        list_x.append(x)
        list_y.append(y)
        list_z.append(z)
        
    
    return list_x,list_y,list_z

equ_x,equ_y,equ_z = equateur()

def parallele(lat_deg):
    
    list_x = []
    list_y = []
    list_z = []
    
    r = 1
    
    for lon_deg in range(0,360):
        x,y,z = sph2cart(lon_deg,lat_deg,r)
        list_x.append(x)
        list_y.append(y)
        list_z.append(z)
        
    
    return list_x,list_y,list_z

par_x,par_y,par_z = parallele(0.0)

#INITIALISATION DU PLOT3D
fig = plt.figure()
ax = plt3D.Axes3D(fig,proj_type='ortho',)
ax.set_aspect('equal')  
#FIN INITIALISATION DU PLOT3D


#PLOTS...
ax.plot3D(equ_x,equ_y,equ_z,linewidth=2.5,color='red')

for lat_deg in range(-90,90,10):
    par_x,par_y,par_z = parallele(lat_deg)
    ax.plot3D(par_x,par_y,par_z,linewidth=0.5,color='blue')
    


#FIN PLOTS...


#FIN DU PLOT3D
plt3D.setAspectEqual3d(ax)
#FIN FIN DU PLOT3D