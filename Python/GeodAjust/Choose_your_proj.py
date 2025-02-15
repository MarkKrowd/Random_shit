import numpy as np
import matplotlib.pyplot as plt


#############################################################################################################

#TOUTES LES LON ET LAT PEUVENT ETRE RECUPEREES DANS LIS_OF_TOUT

#############################################################################################################

type_proj = "Mercator"


def projection(Lon_deg,Lat_deg,type_proj):
    R = 6378000
    lamb = Lon_deg/180*np.pi
    phii = Lat_deg/180*np.pi
    if type_proj == "TheFuck":
        phi_zero = np.pi/3
        
        
        
        alpha = np.cos(phii)/(phi_zero-phii+1/np.tan(phi_zero))*lamb
        rho = 6376000*(phi_zero-phii+1/np.tan(phi_zero))
        
        Est = rho*np.sin(alpha)
        Nord = -rho*np.cos(alpha)
    
        return(Est,Nord)
        
    elif type_proj == "Mercator":
        Est = lamb*R
        Nord = np.log(np.tan(np.pi/4+phii/2))*R
        return(Est,Nord)
        
    elif type_proj == "PlateCarree":
        Est = lamb*R
        Nord = phii*R
        return(Est,Nord)
    elif type_proj == "Gerth":
        Est = R*lamb
        Nord = R*np.sin(phii)
        return(Est,Nord)
    elif type_proj == "Michaud":
        Est = R*lamb
        Nord = R*np.tan(phii)
        return(Est,Nord)
    else:
        print("nope")



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

def circles(Rayon):
    list_x = []
    list_y = []
    list_z = []
    list_lamb = []
    list_phi = []
    r = 1
    for lon_deg in range(-180,180,10):
        for lat_deg in range(-80,90,10):
            list_x_temp = []
            list_y_temp = []
            list_z_temp = []
            list_lamb_temp = []
            list_phi_temp = []
            for alpha in range(0,360,18):
                
                
                delta_phi = (Rayon/6380)*np.cos(alpha/180*np.pi)
                phii = lat_deg + delta_phi/np.pi*180
                
                delta_lambda = 1/np.cos(phii/180*np.pi)*np.sin(alpha/180*np.pi)*(Rayon/6380)
                lamb = lon_deg+ delta_lambda/np.pi*180
                
                x,y,z = sph2cart(lamb,phii,r)
                list_lamb_temp.append(lamb)
                list_phi_temp.append(phii)
                list_x_temp.append(x)
                list_y_temp.append(y)
                list_z_temp.append(z)
            list_lamb_temp.append(list_lamb_temp[0])
            list_phi_temp.append(list_phi_temp[0])
            list_x.append(list_x_temp)
            list_y.append(list_y_temp)
            list_z.append(list_z_temp)
            list_lamb.append(list_lamb_temp)
            list_phi.append(list_phi_temp)
                
    
    return list_x,list_y,list_z,list_lamb,list_phi

plt.Figure()



par_x,par_y,par_z = parallele(0.0)

#INITIALISATION DU PLOT3D

#FIN INITIALISATION DU PLOT3D

filepath = "coast_coarse.bna"

List_X = []
List_Y = []
List_Z = []
new_list_X = []
new_list_Y = []
new_list_Z = []
List_lon = []
List_lat = []
new_list_lon = []
new_list_lat = []


LIST_OF_TOUT_LON = []
LIST_OF_TOUT_LAT = []

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
            List_lon.append(new_list_lon)
            new_list_lon = []
            List_lat.append(new_list_lat)
            new_list_lat = []
        else:
            lon,lat = line.split(",")
            lon = float(lon)
            lat = float(lat)
            
            X,Y,Z = sph2cart(lon,lat,1)
            
            new_list_lon.append(lon)
            new_list_lat.append(lat)
            
            
            new_list_X.append(X)
            new_list_Y.append(Y)
            new_list_Z.append(Z)
        
        line = fp.readline().strip()

#PLOTS...
        
#ax.plot3D(equ_x,equ_y,equ_z,linewidth=2.5,color='gray')

for lat_deg in range(-80,90,10):
    list_lon = []
    list_lat = []
    for lon_deg in range(-180,190,10):
        list_lon.append(lon_deg)
        list_lat.append(lat_deg)
    
    E = []
    N = [] 
    
    for i in range(len(list_lon)):
        Est, Nord = projection(list_lon[i],list_lat[i],type_proj)
        E.append(Est)
        N.append(Nord)
        
    plt.plot(E,N,linewidth=0.5,color='gray')
    
    for lists in list_lon:
        LIST_OF_TOUT_LON.append(lists)
    for lists in list_lat:
        LIST_OF_TOUT_LAT.append(lists)
    
for lon_deg in range(-180,190,10):
    list_lon = []
    list_lat = []
    for lat_deg in range(-80,90,10):
        list_lon.append(lon_deg)
        list_lat.append(lat_deg)
    
    E = []
    N = [] 
    
    for i in range(len(list_lon)):
        Est, Nord = projection(list_lon[i],list_lat[i],type_proj)
        E.append(Est)
        N.append(Nord)
    
    
    
    plt.plot(E,N,linewidth=0.5,color='gray')
    
    for lists in list_lon:
        LIST_OF_TOUT_LON.append(lists)
    for lists in list_lat:
        LIST_OF_TOUT_LAT.append(lists)

index = 0
for lists in List_X:
    if index > 1:
        if len(lists)>1:
            x = lists
            y = List_Y[index]
            z = List_Z[index]
            E = []
            N = []
            
            for i in range(len(List_lon[index])):
                Est, Nord = projection(List_lon[index][i],List_lat[index][i],type_proj)
                E.append(Est)
                N.append(Nord)
            #print(x,y,z)
            #plt.plot(List_lon[index],List_lat[index],linewidth = 1,color='black')
            plt.fill(E,N,c='gray')
            LIST_OF_TOUT_LON.append(List_lon[index])
            LIST_OF_TOUT_LAT.append(List_lat[index])
            
    index += 1

#cercles de machin, entrer rayon en km

X_cercles,Y_cercles,Z_cercles,lambs,phis = circles(200)

index = 0

for lists in lambs:
    E = []
    N = []
    for i in range(len(lambs[index])):
        
        Est, Nord = projection(lambs[index][i],phis[index][i],type_proj)
        E.append(Est)
        N.append(Nord)
        
    
    plt.plot(E,N,linewidth = 1,color='blue')
    LIST_OF_TOUT_LON.append(lambs[index])
    LIST_OF_TOUT_LAT.append(phis[index])
    index += 1
#FIN PLOTS...
plt.draw()



#FIN DU PLOT3D

#FIN FIN DU PLOT3D



plt.axis("equal")
  