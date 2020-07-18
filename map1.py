import folium
import pandas


#processing the Volcanoes' data file to get their longitude and latitude so that we can use them later to make markers
volcanic_data = pandas.read_csv("Volcanoes.txt")
latitude = list(volcanic_data["LAT"]) #extracting the latitude column and converting it into a list
longitude = list(volcanic_data["LON"]) #extracting the longitude column and converting it into a list


#creating an instance of the Map object provided by folium
#and since map is a reserved keyword, so i'll have to use another variable name
map1 = folium.Map(location=[30.375321, 69.345116], zoom_start=6, tiles="Stamen Terrain")

#making a feature group to add more layers/children to the map instance
fg = folium.FeatureGroup(name="layer1")
#making multiple markers for the volcanoes by looping through the latitude and longitude lists
for lat, lon in zip(latitude, longitude):
    fg.add_child(folium.Marker(location=[lat, lon], popup="This is a volcano!", icon=folium.Icon(color="red")))


map1.add_child(fg)

#converting this map object to an html file so that it can be viewed in the browser
map1.save("map1.html")