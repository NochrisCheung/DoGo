# Routing API documentation: https://developer.tomtom.com/routing-api/routing-api-documentation-routing/calculate-route

import urllib2
import json
import postcode_api

start_coord_from_postcode = postcode_api.find_coord_with_postcode('se16fp')
end_coord_from_postcode = postcode_api.find_coord_with_postcode('w23uy')

api_key = 'aQIOZxsbTndh01CWzf8fiAXBFaF03fA6'
api_startcoord = str(start_coord_from_postcode[0]) + ',' + str(start_coord_from_postcode[1])
api_endcoord = str(end_coord_from_postcode[0]) + ',' + str(end_coord_from_postcode[1])

api_endcoord
api_startcoord

travel_details = json.load(urllib2.urlopen('https://api.tomtom.com/routing/1/calculateRoute/'
+api_startcoord + ':' + api_endcoord + '/json?\
instructionsType=text&language=en-US\
&vehicleHeading=90&sectionType=traffic\
&report=effectiveSettings&routeType=eco\
&traffic=true&avoid=unpavedRoads\
&travelMode=car&vehicleMaxSpeed=120\
&vehicleCommercial=false&vehicleEngineType=combustion\
&key=aQIOZxsbTndh01CWzf8fiAXBFaF03fA6'
))

# set().union(*(d.keys() for d in travel_details['routes']))

travel_time_in_minute = travel_details['routes'][0]['summary']['travelTimeInSeconds']/60

print(travel_time_in_minute)
