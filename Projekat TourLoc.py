#  Uvoženje neophodnih biblioteka za projekat
from shapely.geometry import Point
import geopandas as gpd
from fiona.crs import from_epsg
import matplotlib.pyplot as plt

#  Definisanje tačaka, odnosno turističkih lokaliteta, zajedno sa koordinatama, dobijenih iz datoteke konvert_to_cartes.py
l1 = Point(7573051.694640536, 4798354.2681178935)   # Niska tvrdjava
l2 = Point(7575409.489791939, 4796885.634328285)   # Cele kula
l3 = Point(7582181.556032651, 4794807.053727293)   # Niska banja (park)
l4 = Point(7574133.577824903, 4796918.636816507)   # Bazen Cair
l5 = Point(7574998.754432337, 4797728.3713657055)   # Park Sv. Save
l6 = Point(7577375.09481449, 4796598.63705776)   # Medijana
l7 = Point(7572502.777235423, 4798840.518856636)   # Logor Crveni Krst
l8 = Point(7571228.945065863, 4796022.980969675)   # Spomen-park Bubanj
l9 = Point(7576836.349357419, 4802788.508487865)   # Cegar
l10 = Point(7576519.1732090395, 4810000.0702409325)   # Cerjanska pecina

#  Proveravanje tipa objekta
print(l1)
print(type(l1))

#  Kreiranje liste torki
lista = [(l1, 'Niska tvrdjava'), (l2, 'Cele kula'), (l3, 'Niska banja (park)')
         , (l4, 'Bazen Cair'), (l5, 'Park Sv. Save'), (l6, 'Medijana')
         , (l7, 'Logor Crveni Krst'), (l8, 'Spomen-park Bubanj'), (l9, 'Cegar')
         , (l10, 'Cerjanska pecina')]

#  Kreiranje GeoDataFrame-a
df = gpd.GeoDataFrame()
df['geometry'] = None

"""Iteracija redova, kreiranje kolone koja predstavlja geometriju (koordinate tačaka)
 i kolone koja predstavlja Ime lokaliteta, sa ispisanim nazivima entiteta iz liste"""
for id, (lokacija, ime) in enumerate(lista):
    df.loc[id, 'geometry'] = lokacija
    df.loc[id, 'Ime lokaliteta'] = ime

#  Učitavanje koordinatnog sistema i prikazivanje tačaka na grafikonu
df.crs = from_epsg(6316)
df.plot(facecolor='green')
plt.title('Turisticki lokaliteti')
plt.show()

#  Davanje naziva novom shp fajlu i snimanje istog
out_file = r'E:\MAS GIS\GIS programiranje\TourLoc\Lokaliteti.shp'  # Promeniti putanju
df.to_file(out_file)

#  Učitavanje datoteke Nis sa Niskom banjom.shp
fp = r'E:\MAS GIS\GIS programiranje\TourLoc\Nis sa Niskom banjom.shp'  # Promeniti putanju
teritorija = gpd.read_file(fp)
print(teritorija)
print(teritorija.crs)
print(teritorija['geometry'].head())

#  Promena imena kolone "Opstina" u "Naziv opstine"
teritorija = teritorija.rename(columns={'Opstina': 'Naziv opstine'})
print(teritorija.columns)
print(teritorija)

#  Dodavanje nove kolone "area" i ispisivanje izračunatih površina u km2
teritorija['area'] = None
for P, red in teritorija.iterrows():
    teritorija.loc[P, 'area'] = red['geometry'].area/1000000
print(teritorija['area'].head())
print(f'Povrsine u km2 iznose: \n {teritorija}')
teritorija.crs = from_epsg(6316)
print(teritorija.crs)

#  Prikazivanje karte Niša i Niške banje, sa legendom i koordinatnom mrežom
teritorija.plot(column='Naziv opstine', cmap='tab10', legend=True)
# internet sajt za colormaps https://www.analyticsvidhya.com/blog/2020/09/colormaps-matplotlib/
plt.title('Opstine Nisa')
plt.grid()
plt.tight_layout()
plt.show()

#  Davanje naziva novom shp fajlu i snimanje istog
out_file2 = r'E:\MAS GIS\GIS programiranje\TourLoc\Teritorija Nisa i Niske banje.shp'  # Promeniti putanju
teritorija.to_file(out_file2)

print('---------------------------------------')
print(df.crs)
print(teritorija.crs)

#  Spajanje tačaka turističkih lokaliteta sa niškim opštinama (Nišom i Niškom banjom) i prikazivanje rezultata na mapi
df.to_crs(teritorija.crs, inplace=True)
preklapanje = df.geometry._append(teritorija.geometry)
print(preklapanje.crs)
print(preklapanje)

preklapanje.plot(cmap='Paired')
plt.title("Turisticki lokaliteti na teritoriji Nisa")
plt.show()

