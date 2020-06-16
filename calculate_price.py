import tomtom_api
import postcode_api

min_price = 3.50
service_fee = 0.25

def get_price(distance):
          # return round(max(min_price + service_fee, 0.259*distance*distance + 2.71),2)
          return round(max(3.5, 1.5*distance + 2),2)

start_coord_from_postcode = postcode_api.find_coord_with_postcode('se18bw')
end_coord_from_postcode = postcode_api.find_coord_with_postcode('e49bp')
distance = tomtom_api.get_travel_distance(tomtom_api.get_route_details(start_coord_from_postcode, end_coord_from_postcode))
time = tomtom_api.get_travel_time(tomtom_api.get_route_details(start_coord_from_postcode, end_coord_from_postcode))
print(distance, time)
print(get_price(distance))
