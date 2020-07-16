import folium

#creating an instance of the Map object provided by folium
#and since map is a reserved keyword, so i'll have to use another variable name
map1 = folium.Map(location=[30.375321, 69.345116], zoom_start=6)
#converting this map object to an html file so that it can be viewed in the browser
map1.save("map1.html")