import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def setAspectEqual3d(ax):
    """Fix equal aspect bug for 3D plots."""

    xlim = ax.get_xlim3d()
    ylim = ax.get_ylim3d()
    zlim = ax.get_zlim3d()

    from numpy import mean
    xmean = mean(xlim)
    ymean = mean(ylim)
    zmean = mean(zlim)

    plot_radius = max([abs(lim - mean_)
                       for lims, mean_ in ((xlim, xmean),
                                           (ylim, ymean),
                                           (zlim, zmean))
                       for lim in lims])

    ax.set_xlim3d([xmean - plot_radius, xmean + plot_radius])
    ax.set_ylim3d([ymean - plot_radius, ymean + plot_radius])
    ax.set_zlim3d([zmean - plot_radius, zmean + plot_radius])


def sph2cart(lon_deg,lat_deg,r):
    lon = lon_deg/180*np.pi
    lat = lat_deg/180*np.pi
    
    x = r*np.cos(lat)*np.cos(lon)
    y = r*np.cos(lat)*np.sin(lon)
    z = r*np.sin(lat)
    
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

def merid(lon_deg):
    list_x = []
    list_y = []
    list_z = []
    
    r = 1
    
    for lat_deg in range(0,360):
        x,y,z = sph2cart(lon_deg,lat_deg,r)
        list_x.append(x)
        list_y.append(y)
        list_z.append(z)

    return list_x,list_y,list_z
par_x,par_y,par_z = parallele(0.0)

#INITIALISATION DU PLOT3D
fig = plt.figure()
ax = Axes3D(fig,proj_type='ortho',)
ax.set_aspect('equal')  
#FIN INITIALISATION DU PLOT3D

filepath = "coast_coarse.bna"

List_X = []
List_Y = []
List_Z = []
new_list_X = []
new_list_Y = []
new_list_Z = []

with open(filepath) as fp:
    line = fp.readline().strip()
    while line:

        if len(line.split(",")) >2:
            List_X.append(new_list_X)
            new_list_X = []
            List_Y.append(new_list_Y)
            new_list_Y = []
            List_Z.append(new_list_Z)
            new_list_Z = []
        else:
            lon,lat = line.split(",")
            lon = float(lon)
            lat = float(lat)
            
            X,Y,Z = sph2cart(lon,lat,1)
            
            new_list_X.append(X)
            new_list_Y.append(Y)
            new_list_Z.append(Z)
        
        line = fp.readline().strip()

#PLOTS...
        
ax.plot3D(equ_x,equ_y,equ_z,linewidth=2.5,color='gray')

for lat_deg in range(-90,90,10):
    par_x,par_y,par_z = parallele(lat_deg)
    ax.plot3D(par_x,par_y,par_z,linewidth=0.5,color='gray')  
    
for lon_deg in range(-90,90,10):
    mer_x,mer_y,mer_z = merid(lon_deg)
    ax.plot3D(mer_x,mer_y,mer_z,linewidth=0.5,color='gray')

index = 0
for lists in List_X:
    if index > 1:
        if len(lists)>0:
            x = lists
            y = List_Y[index]
            z = List_Z[index]
            #print(x,y,z)
            ax.plot3D(x,y,z,linewidth = 1)
    index += 1


#FIN PLOTS...


#FIN DU PLOT3D
setAspectEqual3d(ax)
#FIN FIN DU PLOT3D

  