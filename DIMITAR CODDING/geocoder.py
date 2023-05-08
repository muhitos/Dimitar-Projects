import folium

m = folium.Map(location=[42.6713, 23.3290])
output = 'base_map.html'
m.save(output)
