
import matplotlib.pyplot as plt
import numpy as np
import requests
import json

def get_lat_and_log(route_points):
    route_points_latitude = []
    route_points_longitude = []
    for i in route_points:
        route_points_latitude.append(i['latitude'])
        route_points_longitude.append(i['longitude'])
    return [route_points_latitude, route_points_longitude]

def plot_route(route_points):
    [route_points_latitude, route_points_longitude] = get_lat_and_log(route_points)
    fig, ax = plt.subplots()
    ax.plot(route_points_latitude, route_points_longitude)
    plt.show()
