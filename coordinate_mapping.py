
# from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

def plot_route(route_points):
    route_points_latitude = []
    route_points_longitude = []
    for i in route_points:
        route_points_latitude.append(i['latitude'])
        route_points_longitude.append(i['longitude'])

    fig, ax = plt.subplots()
    ax.plot(route_points_latitude, route_points_longitude)
    plt.show()
