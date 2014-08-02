'''
Created on 02-Aug-2014

@author: rahul
'''
from geohasher import hasher


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
