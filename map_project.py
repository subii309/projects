import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

df = pandas.read_csv(r"C:\Users\hp\Desktop\volcanoes.tsv",sep='\t')

lat = list(df['Latitude'])
long = list(df['Longitude'])
vol = list(df['Volcano Name'])
elev = list(df['Elev'])

lat.pop(0)
long.pop(0)
vol.pop(0)
elev.pop(0)

fg = folium.FeatureGroup(name="My Map")

def get_colors(elev):
    if elev < 1000:
        return 'green'
    elif elev < 3000 and elev > 1000 :
        return 'orange'
    else :
        return 'red'


for lat,long,elev in zip(lat,long,elev):
    fg.add_child(folium.CircleMarker(location=[lat, long],radius=6, popup=str(elev)+" m",fill=True, fill_color=get_colors(elev), color='grey',fill_opacity=0.7)) 


map.add_child(fg)

map.save("map.html")

