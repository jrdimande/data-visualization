import json

# Explore the sructure of the data
filename='../../data/eq_1_day_ml.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

# Extracting Magnitudes, Location
mags, lons,lats = [], [], []
for eq_dict in all_eq_dicts[:5]:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)




