import folium
import pandas as pd
import postcode_api


start_coord_from_postcode = postcode_api.find_coord_with_postcode('se16fp')


map = folium.Map(location= start_coord_from_postcode , default_zoom_start=0.5)
# map.choropleth(geo_path="census_tracts_2010.geojson")
map.save(outfile='datamap.html')
