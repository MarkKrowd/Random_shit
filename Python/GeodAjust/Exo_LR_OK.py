import numpy as np
import matplotlib.pyplot as plt

def ell2cart(a,e,long_deg,lat_deg,h):
    lat_rad = lat_deg / 180 * np.pi
    long_rad = long_deg / 180 * np.pi
    RN = a / (np.sqrt(1 - e**2 * (np.sin(lat_rad))**2))
    x = (RN+h) * np.cos(lat_rad) * np.cos(long_rad)
    y = (RN+h) * np.cos(lat_rad) * np.sin(long_rad)
    z = (RN * (1-e**2)+  h) * np.sin(lat_rad)
    
    return x,y,z

def cart2ell(a,e,x,y,z) :
    lambda_rad = np.arctan(y / x)
    lambda_deg = lambda_rad / np.pi * 180
    
    hi = 0
    hj = 1
    RNi = 1
    phi_i_rad = 0
    
    while abs(hi - hj) > 0.000001 :
        hj = hi
        phi_i_rad = np.arctan2(z,np.sqrt(x**2 + y**2) * (1 - RNi / (RNi + hi) * e**2))
        RNi = a / (np.sqrt(1 - e**2 * np.sin(phi_i_rad)**2))
        hi = np.sqrt(x**2 + y**2) / np.cos(phi_i_rad) - RNi
        
    phi_rad = phi_i_rad
    h = hi
    phi_deg = phi_rad / np.pi * 180
    
    return (lambda_deg,phi_deg,h)

def sph2cart(lon,lat,r):
    lon_rad = lon/180*np.pi
    lat_rad = lat/180*np.pi
    
    x = r * np.cos(lon_rad) * np.cos(lat_rad)
    y = r * np.cos(lat_rad) * np.sin(lon_rad)
    z = r * np.sin(lat_rad)
    
    return x,y,z

def car2sph(x,y,z) :
    r = np.sqrt(x**2 + y**2 + z**2)
    
    lon_rad = np.arctan(y / x)
    lat_rad = np.arctan(z / np.sqrt(x**2 + y**2))    
    lon_deg = lon_rad / np.pi * 180
    lat_deg = lat_rad / np.pi * 180
    
    return (lon_deg,lat_deg,r)

#Paramètres de l'élipsoïde
a = 6378137
f = 1/298.257222101

b = - (f * a - a)
e = np.sqrt(a**2 - b**2) / a

#Calcul des coordonnées cartésiennes
liste_x = []
liste_y = []
liste_z = []
for n in range (-90,90) :
    xn,yn,zn = ell2cart(a,e,6.65909,n,0)
    liste_x.append(xn)
    liste_y.append(yn)
    liste_z.append(zn)

#Calcul du nombre de points à transformer
nbr_pts = len(liste_x)

#Calcul des coordonnées sphériques
lon_sph = []
lat_sph = []
r_sph = []
for i in range(nbr_pts) :
    lon_i,lat_i,r_i = car2sph(liste_x[i],liste_y[i],liste_z[i])
    lon_sph.append(lon_i)
    lat_sph.append(lat_i)
    r_sph.append(r_i)

#Calcul des coordonnées ellipsoïdales
lon_eli = []
lat_eli = []
h_eli = []
for i in range(nbr_pts) :
    lon_i,lat_i,h_i = cart2ell(a,e,liste_x[i],liste_y[i],liste_z[i])
    lon_eli.append(lon_i)
    lat_eli.append(lat_i)
    h_eli.append(h_i)

#Calcul de la différence entre la latitude sphérique et la latitude ellipsoïdale
diff_lat = []
for i in range (nbr_pts) :
    diff_i = lat_eli[i] - lat_sph[i]
    diff_lat.append(diff_i)

#Plot du premier graphique
plt.subplot(2, 1, 1)
plt.plot(lat_sph,diff_lat)
plt.title('EXERCICE Référentiels géodésiques')
plt.ylabel('Diff lat ell. - lat sph. [deg]')

#Plot du second graphique
plt.subplot(2, 1, 2)
plt.plot(lat_sph,r_sph)
plt.xlabel('Latitude sphérique [deg]')
plt.ylabel('Altitude ell. [m]')
