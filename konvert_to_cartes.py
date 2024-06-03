import pyproj
import numpy as np
from pyproj import Transformer

lat, lon = 43.326105792484576, 21.895373713186704
lat_ca,lon_ca = 43.326105792484576, 21.895373713186704
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy1 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy1, 'Niska tvrdjava')

lat, lon = 43.312655175793886, 21.924241642701922
lat_ca,lon_ca = 43.312655175793886, 21.924241642701922
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy2 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy2, 'Cele kula')

lat, lon = 43.29324014985429, 22.00740347017487
lat_ca,lon_ca = 43.29324014985429, 22.00740347017487
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy3 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy3, 'Niska banja (park)')

lat, lon = 43.313078558906675, 21.908519035107894
lat_ca,lon_ca = 43.313078558906675, 21.908519035107894
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy4 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy4, 'Bazen Cair')

lat, lon = 43.3202813261858, 21.919293524496663
lat_ca,lon_ca = 43.3202813261858, 21.919293524496663
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy5 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy5, 'Park Sv. Save')

lat, lon = 43.309873153843064, 21.94842945224371
lat_ca,lon_ca = 43.309873153843064, 21.94842945224371
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy6 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy6, 'Medijana')

lat, lon = 43.33053535208339, 21.888670135869482
lat_ca,lon_ca = 43.33053535208339, 21.888670135869482
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy7 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy7, 'Logor Crveni Krst')

lat, lon = 43.305296437104985, 21.8725999768016
lat_ca,lon_ca = 43.305296437104985, 21.8725999768016
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy8 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy8, 'Spomen-park Bubanj')

lat, lon = 43.36564092604748, 21.942652870447855
lat_ca,lon_ca = 43.36564092604748, 21.942652870447855
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy9 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy9, 'Cegar')

lat, lon = 43.43058118556072, 21.939745152393648
lat_ca,lon_ca = 43.43058118556072, 21.939745152393648
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy10 = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy10, 'Cerjanska pecina')

