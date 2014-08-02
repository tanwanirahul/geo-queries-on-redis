'''
Created on 03-Aug-2014

@author: rahul
'''
from redis.client import Redis
from exceptions import ImproperlyConfigured

CONF = {
    "default": {
        "host": "localhost",
        "port": "6379",
        "db": 1,
        }
    }


def get_connection(conf_profile):
    '''
        Returns the Redis client instance with the connection
        established to configured server.
    '''
    conf = CONF.get(conf_profile) or {}

    if not conf:
        raise ImproperlyConfigured("Specified conf profile is missing.")

    return Redis(**conf)
