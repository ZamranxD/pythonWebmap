import folium

#creating an instance of the Map object provided by folium
#and since map is a reserved keyword, so i'll have to use another variable name
map1 = folium.Map(location=[30.375321, 69.345116], zoom_start=6, tiles="Stamen Terrain")

#making a feature group to add more layers/children to the map instance
fg = folium.FeatureGroup(name="layer1")
#making a marker and adding it on top of the base layer
fg.add_child(folium.Marker(location=[30.375321, 69.345116], popup="Welcome to Pakistan!", icon=folium.Icon(color="blue")))
map1.add_child(fg)

#converting this map object to an html file so that it can be viewed in the browser
map1.save("map1.html")