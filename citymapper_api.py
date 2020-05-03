from flask import Flask, render_template
import urllib2
import json
import postcode_api
from datetime import datetime

start_coord_from_postcode = postcode_api.find_coord_with_postcode('se16fp')
end_coord_from_postcode = postcode_api.find_coord_with_postcode('w23uy')

api_startcoord = str(start_coord_from_postcode[0]) + ',' + str(start_coord_from_postcode[1])
api_endcoord = str(end_coord_from_postcode[0]) + ',' + str(end_coord_from_postcode[1])

api_time = datetime.now().isoformat()

# print(my_date)
# api_time ='2020-05-03T19%3A00%3A02-0500'
api_time_type = 'department'
api_key = '17bcb241f54d73b30552ef894edca604'
x = json.load(urllib2.urlopen(
    'https://developer.citymapper.com/api/1/traveltime/?'
    +'startcoord='+ api_startcoord
    +'&endcoord='+ api_endcoord
    +'&time=' + api_time
    +'&time_type=' + api_time_type
    +'&key='+api_key
    )
)

print(x)
