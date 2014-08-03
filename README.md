geo-queries-on-redis
====================

This is a simple project to demonstrate the geo location based queries on Redis.

What is this about?
====================
Assume we have a set of locations and a tag associated with each location. Now, given the latitude and longitude, you want to find out all the locations within N kms. This project address just that.


How to use?
====================
1. First off install the dependencies from requirements.txt
    * pip install -r requirements.txt
  
2. cd to src directory.

3. Update the geo index with few locations to work upon.
    * python geoindex.py -u 12.0 77.01 "CCD first"
    * python geoindex.py -u 12.04 77.01 "CCD second"
    * python geoindex.py -u 12.04 77.08 "CCD third"
    * python geoindex.py -u 12.04 77.15 "CCD fourth"
    * python geoindex.py -u 12.04 77.7 "CCD fifth"

  Now we have 5 location entries in our index. -u option as you might have just guessed by now is to update the index.

4. Get the location for a give lat / lon.
    * python geoindex.py -f 12.04 77.01

  This should give us back the object with the tag "CCD second". Again, -f option is to find a specific location tag.

5. Get all the locations within x radius of KMs.
    * python geoindex.py -q 12.00 77.00 100
    
    This should give us all the locations we have, since all the locations are within 80 kms of range.
    
    
    * python geoindex.py -q 12.00 77.00 20
    
    This should give us first 4 locations which are within 20 kms of range.
    
    
    * python geoindex.py -q 12.00 77.00 10
    
    This should give us first 3 locations which are within 10 kms of range.
    
    
    * python geoindex.py -q 12.00 77.00 5
    
    This should give us first 2 locations which are within 5 kms of range.
    
    
    * python geoindex.py -q 12.00 77.00 3
    
    This should give us first location which has distance of around 1 Km.





