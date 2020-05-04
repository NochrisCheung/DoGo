import requests
import json


def find_coord_with_postcode(postcode):
    location_details = requests.get('https://api.postcodes.io/postcodes/'+ postcode).json()
    return parse_coordinates(location_details)

def parse_coordinates(location_details):
     return [location_details['result']['latitude'], location_details['result']['longitude']]
