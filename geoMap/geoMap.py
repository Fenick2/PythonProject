import folium

map = folium.Map(location=[53.903661, 27.555844], zoom_start=10, tiles='Mapbox bright')
folium.Marker(location=[53.9035591, 27.5552952], popup='City hall', icon=folium.Icon(color='lightgray')).add_to(map)


map.save("my_map.html")
