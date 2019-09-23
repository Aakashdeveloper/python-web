import folium
map = folium.Map(location=[32.58,-99.09],zoom_start=6,title="Mapbox Bright")
fg = folium.FeatureGroup(name="Volcanoes")

for coordinate in [[32.58,-99.09], [33.58,-98.09]]:
    fg.add_child(folium.Marker(location=coordinate,popup="Hi i am marker",icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map3.html")
print(map)