# Routing API documentation: https://developer.tomtom.com/routing-api/routing-api-documentation-routing/calculate-route

import requests
import json
import postcode_api
import coordinate_mapping

start_coord_from_postcode = postcode_api.find_coord_with_postcode('se16fp')
end_coord_from_postcode = postcode_api.find_coord_with_postcode('w23uy')
api_key = 'aQIOZxsbTndh01CWzf8fiAXBFaF03fA6'

def get_route_details(start_coord_from_postcode, end_coord_from_postcode):
    api_startcoord = str(start_coord_from_postcode[0]) + ',' + str(start_coord_from_postcode[1])
    api_endcoord = str(end_coord_from_postcode[0]) + ',' + str(end_coord_from_postcode[1])

    api_url = str('https://api.tomtom.com/routing/1/calculateRoute/'
    + api_startcoord + ':' + api_endcoord +
    '/json?&sectionType=traffic&report=effectiveSettings&traffic=true&avoid=unpavedRoads&travelMode=bicycle&key='
    +api_key)

    return requests.get(api_url).json()

def get_legs(route_details):
    return route_details['routes'][0]['legs'][0]['points']
