# Citymapper API documentation: https://citymapper.3scale.net/docs

import urllib2
import json
import postcode_api
from datetime import datetime

start_coord_from_postcode = postcode_api.find_coord_with_postcode('se16fp')
end_coord_from_postcode = postcode_api.find_coord_with_postcode('w23uy')

api_startcoord = str(start_coord_from_postcode[0]) + ',' + str(start_coord_from_postcode[1])
api_endcoord = str(end_coord_from_postcode[0]) + ',' + str(end_coord_from_postcode[1])
api_time = datetime.now().isoformat()
api_time_type = 'department'
api_key = '17bcb241f54d73b30552ef894edca604'
travel_time = json.load(urllib2.urlopen(
    'https://developer.citymapper.com/api/1/traveltime/?'
    +'startcoord='+ api_startcoord
    +'&endcoord='+ api_endcoord
    +'&time=' + api_time
    +'&time_type=' + api_time_type
    +'&key='+api_key
    )
)

print(travel_time)
