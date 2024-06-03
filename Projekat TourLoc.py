from shapely.geometry import Point
import geopandas as gpd
from fiona.crs import from_epsg
import matplotlib.pyplot as plt

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

print(l1)
print(type(l1))

lista = [(l1, 'Lokalitet 1'), (l2, 'Lokalitet 2'), (l3, 'Lokalitet 3')
         , (l4, 'Lokalitet 4'), (l5, 'Lokalitet 5'), (l6, 'Lokalitet 6')
         , (l7, 'Lokalitet 7'), (l8, 'Lokalitet 8'), (l9, 'Lokalitet 9')
         , (l10, 'Lokalitet 10')]

df = gpd.GeoDataFrame()
df['geometry'] = None

for id, (lokacija, ime) in enumerate(lista):
    df.loc[id, 'geometry'] = lokacija
    df.loc[id, 'Ime lokaliteta'] = ime

df.crs = from_epsg(6316)
df.plot(facecolor='green')
plt.title('Turisticki lokaliteti')
plt.show()

#out_file = r'E:\MAS GIS\GIS programiranje\TourLoc\Lokaliteti.shp'
#df.to_file(out_file)


fp = r'E:\MAS GIS\GIS programiranje\TourLoc\Nis sa Niskom banjom.shp'
teritorija = gpd.read_file(fp)
print(teritorija)
print(teritorija.crs)
print(teritorija['geometry'].head())

teritorija = teritorija.rename(columns={'Opstina': 'Naziv opstine'})
print(teritorija.columns)
print(teritorija)

teritorija['area'] = None
for P, red in teritorija.iterrows():
    teritorija.loc[P, 'area'] = red['geometry'].area/1000000
print(teritorija['area'].head())
print(f'Povrsine u km2 iznose: \n {teritorija}')
teritorija.crs = from_epsg(6316)
print(teritorija.crs)

teritorija.plot(column='Naziv opstine', cmap='tab10', legend=True)
# link za colormaps https://www.analyticsvidhya.com/blog/2020/09/colormaps-matplotlib/
plt.title('Opstine Nisa')
plt.grid()
plt.tight_layout()
plt.show()

print('---------------------------------------')
print(df.crs)
print(teritorija.crs)
df.to_crs(teritorija.crs, inplace=True)
preklapanje = df.geometry._append(teritorija.geometry)
print(preklapanje.crs)
print(preklapanje)

preklapanje.plot(cmap='Paired')
plt.title("Turisticki lokaliteti na teritoriji Nisa")
plt.show()
