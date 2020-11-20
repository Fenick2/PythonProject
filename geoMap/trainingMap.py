import folium
from folium.plugins import MarkerCluster
import pandas as pd


data = pd.read_csv('Volcanoes_USA.txt')
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']


# Change colors
def color_change(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev <= 3000:
        return 'orange'
    else:
        return 'red'


# Creating base map
map = folium.Map(location=[37.296933, -121.9574983], zoom_start=8)

# Create Cluster
marker_cluster = MarkerCluster().add_to(map)

# Plot makers and add to 'marker_cluster'
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.CircleMarker(location=(lat, lon), radius=9, popup=str(elevation) + 'm',
                        fill_color=color_change(elevation), color='gray', fill_opasity=0.9).add_to(marker_cluster)

map.save("t_map.html")
