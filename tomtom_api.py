# Routing API documentation: https://developer.tomtom.com/routing-api/routing-api-documentation-routing/calculate-route

import requests
import json
import postcode_api
import coordinate_mapping

start_coord_from_postcode = postcode_api.find_coord_with_postcode('se16fp')
end_coord_from_postcode = postcode_api.find_coord_with_postcode('w23uy')

api_key = 'aQIOZxsbTndh01CWzf8fiAXBFaF03fA6'
api_startcoord = str(start_coord_from_postcode[0]) + ',' + str(start_coord_from_postcode[1])
api_endcoord = str(end_coord_from_postcode[0]) + ',' + str(end_coord_from_postcode[1])

api_endcoord
api_startcoord

travel_details = requests.get('https://api.tomtom.com/routing/1/calculateRoute/'
+api_startcoord + ':' + api_endcoord + '/json?\
&vehicleHeading=90&sectionType=traffic\
&travelMode=bicycle\
&key=aQIOZxsbTndh01CWzf8fiAXBFaF03fA6'
).json()

# set().union(*(d.keys() for d in travel_details['routes']))
route_points = travel_details['routes'][0]['legs'][0]['points']
coordinate_mapping.plot_route(route_points)
#
#
# route_points_latitude
# travel_summary = travel_details['routes'][0]['summary']
# travel_summary
#
# travel_time_in_minute = travel_details['routes'][0]['summary']['travelTimeInSeconds']
#
# print(travel_time_in_minute)
