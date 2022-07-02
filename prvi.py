
#Projekat GIS Programiranje (Putevi na teritoriji Cacka)

#importovanje neophodnih biblioteka
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import MultiLineString, Polygon
from fiona.crs import from_epsg

#ubacivanje shp fajlova
#shp fajl Putevi
a=r'/home/ap/Downloads/putevii/putevii.shp'
#shp fajl putevi_cacak
cp = r'/home/ap/Downloads/cacak_putevi/cacak_putevi.shp'
#shp fajl Cacak
rp = r'/home/ap/Downloads/cacak/cacak.shp'



#ucitavanje prvog fajla
put= gpd.read_file(a)
print(put)
#prikaz
put.plot()
plt.title('Putevi u Srbiji')
plt.show()

#citanje treceg fajla
data2 = gpd.read_file(rp)
print(data2)
#prikaz treceg lejera

data2.plot(facecolor='red');
plt.title('Cacak')
plt.show()

#provera koord.sistema
data2.crs
print(data2.crs)


#presek lejera Putevi i ca shp
intersection=gpd.overlay(put,data2, how= 'intersection')
print(intersection)
intersection.plot()
plt.title('Preseceno')
plt.show()

#cuvanje dobijenog shp fajla
izlaz= r'/home/ap/PycharmProjects/pythonProject3/venv/izlaz/Putevipreseceno.shp'
intersection.to_file(izlaz)


#citanje  drugog fajla
data = gpd.read_file(cp)
print(data)

#prikaz drugog fajla
data.plot(facecolor='blue');
plt.title('Putevi')
plt.show()

#provera koord sistema
data.crs
print(data.crs)


#menjanje naziva kolone
data2=data2.rename(columns={'Opstina': 'Grad'})
data2.columns
print(data2)

#racunanje povrsine_cacka

data2 ['area'] = None
for povrsina, row in data2.iterrows():
        data2.loc[povrsina, 'area']= row['geometry'].area
print(data2['area'].head())
print(data2)
#pretvaranje u iz m2 u km2
data2 ['area'] = data2.area/1000000
print(data2)


#ukupna duzina puteva_cacak
data ['length'] = None
for duzina, row in data.iterrows():
        data.loc[duzina, 'length']= row['geometry'].length
print(data['length'].head())
print(data)
#pretvaranje iz m u km
data ['length'] = data.length/1000
print(data)

#koord sistem

data.crs=from_epsg(6316)
print(data.crs)
data2.crs=from_epsg(6316)
print(data2.crs)

data.plot(column= 'length');
plt.title('Putevi')
plt.show()


#cuvanje oba fajla
plotovanje=r'/home/ap/PycharmProjects/pythonProject3/venv/izlaz/putevi.shp'
data.to_file(plotovanje)
plotovanje=r'/home/ap/PycharmProjects/pythonProject3/venv/izlaz/cacak.shp'
data2.to_file(plotovanje)

#prikaz spojenih lejera
sp=data.geometry.append(data2.geometry)
print(sp.crs)
print(sp)
sp.plot( figsize=(10,10), cmap='jet')
plt.title('Putevi na teritoriji Cacka')
plt.show()

