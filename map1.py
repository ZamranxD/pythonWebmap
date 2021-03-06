import folium
import pandas

#processing the Volcanoes' data file to get their longitude and latitude so that we can use them later to make markers
volcanic_data = pandas.read_csv("Volcanoes.txt")
latitude = list(volcanic_data["LAT"]) #extracting the latitude column and converting it into a list
longitude = list(volcanic_data["LON"]) #extracting the longitude column and converting it into a list
elevation = list(volcanic_data["ELEV"]) #extractin the elevation column into a list

#makin a function to change marker colors with respect to their elevation
def color_prod(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation >= 1000 and elevation < 3000:
        return 'orange'
    else:
        return 'red'

#creating an instance of the Map object provided by folium
#and since map is a reserved keyword, so i'll have to use another variable name
map1 = folium.Map(location=[38.375321, -99.345116], zoom_start=6, tiles="Stamen Terrain")

#making a feature group to add more layers/children to the map instance
fgv = folium.FeatureGroup(name="Volcano Markers")
#making multiple markers for the volcanoes by looping through the latitude and longitude lists
#also making the popups dynamic by pushing the elevation values in them
for lat, lon, elev in zip(latitude, longitude, elevation):
    fgv.add_child(folium.CircleMarker(location=[lat, lon], radius=6, popup=str(elev)+"m",
     fill_color = color_prod(elev), color = 'grey', fill_opacity = 0.7))

#color grading the countries according to the polulation
#making a feature group for layer control
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'} ))

map1.add_child(fgv)
map1.add_child(fgp)
map1.add_child(folium.LayerControl()) #this layer control helps to turn layers on and off from the UI

#converting this map object to an html file so that it can be viewed in the browser
map1.save("map1.html")