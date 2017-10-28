import folium
import os
import pandas as pd
import re
import numpy as np
import json
import random 
import branca


data = pd.DataFrame.from_csv("data/data.tsv", sep='\t', header=0)
data.reset_index(inplace=True)
series = data["sex,age,unit,geo\\time"].copy()
data.drop(["sex,age,unit,geo\\time"], axis=1, inplace=True)
data = data.applymap(lambda x: re.sub('[^.0-9]','', x) if type(x)==str else x)
data = data.applymap(lambda x: np.nan if type(x)==str and x=="" else x)
data.rename(columns=lambda x: x[:-1] if x[-1]==" " else x, inplace=True)
data["age"] = series.apply(lambda x: x.split(",")[1])
data["country"] = series.apply(lambda x: x.split(",")[3])
data = data.apply(pd.to_numeric, errors='ignore')

data_total = data[data["age"] == "TOTAL"].copy()
data_total

europe_geo_path = './topojson/europe.topojson.json'
geo_json_data = json.load(open(europe_geo_path))

colorscale = branca.colormap.linear.YlOrRd.scale(data_total['2016'].min(), data_total['2016'].max())
def style_function(feature):
    d = data_total.loc[data_total['country'] == feature['id']]['2016']
    return {
        'fillOpacity': 0.8,
        'weight': 1,
        'fillColor': '#black' if d.size == 0 else colorscale(d.tolist()[0])
    }


centre_map = folium.Map(
    location=[-59.1759, -11.6016],
    tiles='Mapbox Bright',
    zoom_start=2
)

topojson_file = os.path.join('topojson', 'europe.topojson.json')

with open(topojson_file) as file:
    folium.TopoJson(
        file,
        'objects.europe',
        name='topojson',
        style_function=style_function
    ).add_to(centre_map)

    #folium.LayerControl().add_to(centre_map)
    
centre_map.add_child(colorscale)
centre_map