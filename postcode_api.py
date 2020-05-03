import urllib2
import json


def find_coord_with_postcode(postcode):
    location_details = json.load(urllib2.urlopen('https://api.postcodes.io/postcodes/'+ postcode))
    return parse_coordinates(location_details)

def parse_coordinates(location_details):
    return [location_details['result']['latitude'], location_details['result']['longitude']]
