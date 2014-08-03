'''
Created on 03-Aug-2014

@author: rahul
'''
from optparse import OptionParser
from connection import get_connection
from cexceptions import MissingArguments
from dao import Location


def update(redis_conn, lat, lon, tag):
    '''
        Given the lat, lon and tag updates the location index.
    '''
    loc = Location(lat, lon, tag)
    loc.save(redis_conn)
    print "Success!"


def find(redis_conn, lat, lon):
    '''
        Given the lat/lon finds the location and associated tag.
    '''
    loc = Location.get_by_lat_lon(redis_conn, lat, lon)
    print loc


def query(redis_conn, lat, lon, radius):
    '''
        Given the lat, lon and radius finds all the locations
        that are within the radius kms.
    '''
    locs = Location.find_locations_in_radius(redis_conn, lat, lon, radius)
    # Just print all the locations.
    for loc in locs:
        print "{0} - {1} KMs".format(loc[0], loc[1])


def _assert_length(args, length, msg):
    '''
        Asserts the minimum length for the args.
    '''
    if len(args) < length:
        MissingArguments(msg)

if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option("-u", "--update", dest="update",
                      action='store_true', default=False,
                      help='Updates the index with provided location details.')

    parser.add_option("-f", "--find", dest="find",
                      action='store_true', default=False,
                      help='Finds the tag associates with give lat lon.')

    parser.add_option("-q", "--query", dest="query",
                      action='store_true', default=False,
                      help='Finds all the locations within the radius')

    parser.add_option("-p", "--profile", dest="profile", default="default",
                      type="string", help="redis conf profile to use",
                      metavar="PROFILE")

    (options, args) = parser.parse_args()
    profile = options.profile
    redis_conn = get_connection(profile)

    _assert_length(args, 2, "Need 2 parameters at the minimum: lat lon")

    lat = float(args[0])
    lon = float(args[1])

    if options.update:
        _assert_length(args, 3, "Need 3 parameters for update: lat lon tag")
        tag = args[2]
        update(redis_conn, lat, lon, tag)

    elif options.find:
        find(redis_conn, lat, lon)

    elif options.query:
        _assert_length(args, 3, "Need 3 parameters for query: lat lon radius")
        radius = float(args[2])
        query(redis_conn, lat, lon, radius)
