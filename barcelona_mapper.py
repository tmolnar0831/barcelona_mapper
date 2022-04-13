#!/usr/bin/env python

import folium
import pandas

data = pandas.read_csv("locations.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
names = list(data["NAME"])

map = folium.Map(location=[41.41946916670761, 2.161922449252976])

fg = folium.FeatureGroup(name="My Barcelona Map")

for la, lo, na in zip(lat, lon, names):
    fg.add_child(folium.Marker(location=[la, lo], popup=na))

map.add_child(fg)

map.save("barcelona_map.html")