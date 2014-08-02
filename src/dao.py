'''
Created on 02-Aug-2014

@author: rahul
'''
from utils import get_geo_hash, get_distance_by_geohash,\
    get_distance_by_lat_lon, find_locations_in_radius


class Location(object):
    '''
        Represents all the operations performed on location entity.
    '''
    REDIS_KEY = "locations"
    UNIQUE_KEYS_SET = "locations:set"
    KEYS_TO_SAVE = ["lat", "lon", "tag"]

    def __init__(self, lat, lon, tag):  # @ReservedAssignment
        '''
            Initializes the given location parameters.
            tag can be anything like coffee shop name etc.
        '''
        self.lat = lat
        self.lon = lon
        self.tag = tag

    @classmethod
    def get_by_lat_lon(cls, redis_conn, lat, lon):
        '''
            Given the lat and long returns the Location instance.
        '''
        # find geo hash value form lat and lon.
        geo_hash = cls.get_hash_by_lat_lon(lat, lon)
        # delegate further processing to get_by_geohash.
        return cls.get_by_geohash_key(redis_conn, geo_hash)

    @classmethod
    def get_by_geohash_key(cls, redis_conn, geo_key):
        '''
            Returns the mapping based on
        '''
        # find the key name based on hash value.
        loc_key_name = cls.get_hashed_key_by_geokey(geo_key)
        # find all the fields form this mapping
        values = redis_conn.hmget(loc_key_name, *cls.KEYS_TO_SAVE)
        # return the location object.
        return Location(**dict(zip(cls.KEYS_TO_SAVE, values)))

    def save(self, redis_conn):
        '''
            Save this instance into redis.
            Two data structures are being used here.
            1. Map - to store all the locations information.
            2. Set - to store the Ids of all the locations.
        '''

        # Hashed value based on lat and lon.
        geohash = self.get_hash()

        # Name of the hash.
        loc_name = self.get_hashed_key()

        # Name of the set containing unique locations hash.
        set_name = self.get_redis_key_location_set()

        # Prepare the data that needs to be saved into hash.
        data = {k: self.__dict__.get(k) for k in self.KEYS_TO_SAVE}
        redis_conn.hmset(loc_name, data)

        # Add the hash into the set as well.
        redis_conn.sadd(set_name, geohash)

    @classmethod
    def find_locations_in_radius(cls, redis_conn, lat, lon, radius):
        '''
            Given the lat, lon and radius in kms returns all the locations that
            are in the given radius.
        '''
        # These are all the locations we have.
        locations = redis_conn.smembers(cls.get_redis_key_location_set())
        locs_in_radius = find_locations_in_radius(lat, lon, locations, radius)
        return [cls.get_by_geohash_key(redis_conn, k) for k in locs_in_radius]

    @classmethod
    def get_distance_by_geohash(cls, start, end):
        '''
            Returns the distance between two locations.
            both start and end are expected to be geo hashed keys.
        '''
        return get_distance_by_geohash(start, end)

    @classmethod
    def get_distance_by_lat_lon(cls, start, end):
        '''
            Returns the distance between two locations.
            both start and end are expected to be dicts with lat and lon keys.
        '''
        return get_distance_by_lat_lon(start, end)

    @classmethod
    def get_redis_key_location_collection(cls):
        '''
            Returns the redis key for this entity.
        '''
        # we could keep this with same name as class but if we later change
        # the class name, we don't want to get into migration stuff.
        return cls.REDIS_KEY

    @classmethod
    def get_redis_key_location_set(cls):
        '''
            Returns the redis key for this entity.
        '''
        # we could keep this with same name as class but if we later change
        # the class name, we don't want to get into migration stuff.
        return cls.UNIQUE_KEYS_SET

    def get_hash(self):
        '''
            Return the hash for this object.
        '''
        get_geo_hash(self.lat, self.lon)

    @classmethod
    def get_hash_by_lat_lon(cls, lat, lon):
        '''
            Return the hash for this object.
        '''
        get_geo_hash(lat, lon)

    def get_hashed_key(self):
        '''
            Returns the geo hashed key for this instance.
        '''
        return self.get_hashed_key_by_geokey(self.get_hash())

    @classmethod
    def get_hashed_key_by_lat_lon(cls, lat, lon):
        '''
            Returns the geo hashed key for this instance.
        '''
        return cls.get_hashed_key_by_geokey(
            cls.get_hash_by_lat_lon(lat, long))

    @classmethod
    def get_hashed_key_by_geokey(cls, key):
        '''
            Given the geo hash key, returns the hash for this object.
        '''
        return "{0}:{1}".format(cls.get_redis_key_location_collection(), key)
