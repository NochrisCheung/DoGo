
min_price = 3.50
service_fee = 0.25
def get_price(distance):
        return round(max(min_price + service_fee, 0.259*distance*distance + 2.71),2)


print(get_price(6.3))
