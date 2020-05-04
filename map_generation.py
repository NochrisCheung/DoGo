

import matplotlib.pyplot as plt
import osmnx as ox
import postcode_api

start_coord_from_postcode = postcode_api.find_coord_with_postcode('se16fp')
end_coord_from_postcode = postcode_api.find_coord_with_postcode('w23uy')
start_coord_from_postcode
end_coord_from_postcode

north_bound = max(start_coord_from_postcode[0], end_coord_from_postcode[0])
south_bound = min(start_coord_from_postcode[0], end_coord_from_postcode[0])
east_bound = max(start_coord_from_postcode[1], end_coord_from_postcode[1])
west_bound = min(start_coord_from_postcode[1], end_coord_from_postcode[1])

latitude_bleed = (north_bound - south_bound)*0.05
longtitude_bleed = (east_bound - west_bound)*0.05

north_bound = north_bound + latitude_bleed
south_bound = south_bound - latitude_bleed
east_bound = east_bound + longtitude_bleed
west_bound = west_bound - longtitude_bleed

# G = ox.graph_from_place('Liverpool, United Kingdom', network_type='bike')
G = ox.core.graph_from_bbox(
    north = north_bound,
    south = south_bound,
    east = east_bound,
    west = west_bound,
    network_type= 'bike')
    # 51.5155, 51.4971 , -0.09974,  -0.178514)
fig, ax = ox.plot_graph(G)
plt.tight_layout()
