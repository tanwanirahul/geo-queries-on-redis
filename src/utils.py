'''
Created on 02-Aug-2014

@author: rahul
'''
from geohasher import hasher
import math


def get_geo_hash(lat, lon):
    '''
        Returns the geo-hashed value for give latitude and longitude.
    '''
    return hasher.encode(lat, lon)


def get_lat_lon_by_geohash(geohash):
    '''
        Returns the tuple with lat and lon elements.
    '''
    return hasher.decode(geohash)


def get_distance_by_geohash(cls, start, end):
    '''
        Returns the distance between two locations.
        both start and end are expected to be geo hashed keys.
    '''
    start_cords = get_lat_lon_by_geohash(start)
    end_cords = get_lat_lon_by_geohash(end)
    return get_distance_by_lat_lon(start_cords, end_cords)


def get_distance_by_lat_lon(cls, start, end):
    '''
        Returns the distance between two locations.
        both start and end are expected to be tuples with lat and lon elements.
    '''
    R = 6371
    dLat = math.radians(end[0]-start[0])
    dLon = math.radians(end[1]-start[1])
    a = math.sin(dLat/2) * math.sin(dLat/2) + \
        math.cos(math.radians(start[0])) * math.cos(math.radians(end[0])) * \
        math.sin(dLon/2) * math.sin(dLon/2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c
