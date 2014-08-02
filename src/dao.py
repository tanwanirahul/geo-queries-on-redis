'''
Created on 02-Aug-2014

@author: rahul
'''


class Location(object):
    '''
        Represents all the operations performed on location entity.
    '''
    REDIS_KEY = "locations"

    def __init__(self, redis_conn, lat, lon):  # @ReservedAssignment
        '''
            Initializes the given location parameters as well
            as the redis wrapper.
        '''
        self.conn = redis_conn
        self.lat = lat
        self.lon = lon

    @classmethod
    def get_by_lat_lon(self, lat, lon):
        '''
        '''
        pass

    @classmethod
    def get_by_geohash_key(cls, geo_key):
        '''
        '''
        pass

    def save(self):
        '''
            Save this instance into redis.
        '''
        pass

    @classmethod
    def get_distance_by_geohash(cls, start, end):
        '''
            Returns the distance between two locations.
            both start and end are expected to be geo hashed keys.
        '''
        pass

    @classmethod
    def get_distance_by_lat_lon(cls, start, end):
        '''
            Returns the distance between two locations.
            both start and end are expected to be dicts with lat and lon keys.
        '''
        pass

    @classmethod
    def get_redis_key(cls):
        '''
            Returns the redis key for this entity.
        '''
        # we could keep this with same name as class but if we later change
        # the class name, we don't want to get into migration stuff.
        return cls.REDIS_KEY

    def get_hash(self):
        '''
            Returns the geo hash for this instance.
        '''
        pass

    @classmethod
    def get_hash_for_lat_lon(cls, lat, lon):
        '''
            Returns the geo hash for the given latitude and longitude.
        '''
        pass
