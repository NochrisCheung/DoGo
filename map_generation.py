# osmnx documentation: https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.core.graph_from_bbox
import osmnx as ox
import postcode_api
import numpy as np
import plotly.graph_objects as go
import tomtom_api
# def determine_map_bound(start_coord_from_postcode, end_coord_from_postcode):
#     north_bound = max(start_coord_from_postcode[0], end_coord_from_postcode[0])
#     south_bound = min(start_coord_from_postcode[0], end_coord_from_postcode[0])
#     east_bound = max(start_coord_from_postcode[1], end_coord_from_postcode[1])
#     west_bound = min(start_coord_from_postcode[1], end_coord_from_postcode[1])
#
#     latitude_bleed = (north_bound - south_bound)*0.1
#     longtitude_bleed = (east_bound - west_bound)*0.1
#
#     north_bound = north_bound + latitude_bleed
#     south_bound = south_bound - latitude_bleed
#     east_bound = east_bound + longtitude_bleed
#     west_bound = west_bound - longtitude_bleed
#     return [north_bound, south_bound, east_bound, west_bound]
#
# start_coord_from_postcode = postcode_api.find_coord_with_postcode('se16fp')
# end_coord_from_postcode = postcode_api.find_coord_with_postcode('w23uy')
# bound_coordinates = determine_map_bound(start_coord_from_postcode, end_coord_from_postcode)

# G = ox.graph_from_place('Liverpool, United Kingdom', network_type='bike')
# G = ox.core.graph_from_bbox(
#     north = bound_coordinates[0],
#     south = bound_coordinates[1],
#     east = bound_coordinates[2],
#     west = bound_coordinates[3],
#     network_type= 'bike')
#     # 51.5155, 51.4971 , -0.09974,  -0.178514)
# fig, ax = ox.plot_graph(G, bgcolor='#FEFFF0', node_color = '#C0F0ED', edge_color = '#FFBA64')

# bound_coordinates
#
# start_node = ox.get_nearest_node(G, start_coord_from_postcode)
# end_node = ox.get_nearest_node(G, end_coord_from_postcode)
# route = nx.shortest_path(G,start_node, end_node, weight = 'length')
#
# origin_point = (33.787201, -84.405076)
# [origin_point[0]]
#
# route_latitude = []
# route_longitude = []
# for i in route:
#     point = G.nodes[i]
#     route_longitude.append(point['x'])
#     route_latitude.append(point['y'])
def get_lat_and_log(route_points):
    route_points_latitude = []
    route_points_longitude = []
    for i in route_points:
        route_points_latitude.append(i['latitude'])
        route_points_longitude.append(i['longitude'])
    return [route_points_latitude, route_points_longitude]


start_coord_from_postcode = postcode_api.find_coord_with_postcode('WC2H7JS')
end_coord_from_postcode = postcode_api.find_coord_with_postcode('e149bf')

route_details = tomtom_api.get_route_details(start_coord_from_postcode,end_coord_from_postcode)
legs = tomtom_api.get_legs(route_details)
[route_latitude, route_longitude] = get_lat_and_log(legs)


# adding the lines joining the nodes
fig = go.Figure(go.Scattermapbox(
    name = 'Path',
    mode = 'lines',
    lon = route_longitude,
    lat = route_latitude,
    line = dict(width = 3,
        color = 'orange'
        )
    )
)
# adding source marker
fig.add_trace(go.Scattermapbox(
    name = 'Source',
    mode = 'markers',
    lon = [start_coord_from_postcode[1]],
    lat = [start_coord_from_postcode[0]],
    marker = dict(size = 10,
        color = 'green',
        # symbol = 'square',
    )
))

# adding destination marker
fig.add_trace(go.Scattermapbox(
    name = 'Destination',
    mode = 'markers',
    lon = [end_coord_from_postcode[1]],
    lat = [end_coord_from_postcode[0]],
    marker = dict(size = 10,
        color = 'red',
        # symbol = 'square',
    )
))

# getting center for plots:
lat_center = np.mean(route_latitude)
long_center = np.mean(route_longitude)

# defining the layout using mapbox_style
fig.update_layout(mapbox_style="carto-positron",
    mapbox_center_lat = 30, mapbox_center_lon=-80)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
    mapbox = {
      'center': {'lat': lat_center,
      'lon': long_center},
      'zoom': 13})

fig.show()
