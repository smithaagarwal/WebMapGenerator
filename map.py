import folium
import pandas

data = pandas.read_csv("uk-towns-sample.csv")
lat = list(data.latitude)
lon = list(data.longitude)
county = list(data.county)
areas = list(data.local_government_area)
elevations = list(data.elevation)

def color_producer(elevation):
    if elevation<50:
        return "green"
    else:
        return "red"

map = folium.Map(location=[51,0], zoom_start=5, tiles="Stamen Toner")
fgv = folium.FeatureGroup(name = "Cities")

for lt, ln, coun, area, elev in zip(lat, lon, county, areas, elevations ):
    if coun == "Kent" :
        #fg.add_child(folium.Marker(location=[lt,ln],popup=area,icon=folium.Icon(color=color_producer(elev))))
#map.add_child(fg)
        fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=area,
                                         fill_color=color_producer(elev), color='grey', fill=True, fill_opacity=0.7))
fgp = folium.FeatureGroup(name = 'Population')

fgp.add_child(folium.GeoJson(data=(open('europe.json','r', encoding='utf-8-sig').read()),
                            style_function= lambda x:{'fillColor':'yellow' if x['properties']['pop_est']<50000000
                                                      else 'orange' if 50000000<= x['properties']['pop_est'] < 100000000
                                                      else 'red' }))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")


