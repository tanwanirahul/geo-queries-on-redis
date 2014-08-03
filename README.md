geo-queries-on-redis
====================

This is a simple project to demonstrate the geo location based queries on Redis.

What is this about?
====================
Assume we have a set of locations and a tag associated with each location. Now, given the latitude and longitude, you want to find out all the locations within N kms. This project addresses just that.


How to use?
====================
1. First off install the dependencies from requirements.txt
    * **_pip install -r requirements.txt_**
  
2. cd to src directory.

3. Update the geo index with few locations to work upon.
    * **_python geoindex.py -u 12.0 77.01 "CCD first"_**
    * **_python geoindex.py -u 12.04 77.01 "CCD second"_**
    * **_python geoindex.py -u 12.04 77.08 "CCD third"_**
    * **_python geoindex.py -u 12.04 77.15 "CCD fourth"_**
    * **_python geoindex.py -u 12.04 77.7 "CCD fifth"_**

  Now we have 5 location entries in our index. -u option as you might have just guessed by now is to update the index.

4. Get the location for a give lat / lon.
    * **_python geoindex.py -f 12.04 77.01_**

  This should give us back the object with the tag "CCD second". Again, -f option is to find a specific location tag.

5. Get all the locations within x radius of KMs.
    * **_python geoindex.py -q 12.00 77.00 100_**
    
    This should give us all the locations we have, since all the locations are within 80 kms of range.
    
    
    * **_python geoindex.py -q 12.00 77.00 20_**
    
    This should give us first 4 locations which are within 20 kms of range.
    
    
    * **_python geoindex.py -q 12.00 77.00 10_**
    
    This should give us first 3 locations which are within 10 kms of range.
    
    
    * **_python geoindex.py -q 12.00 77.00 5_**
    
    This should give us first 2 locations which are within 5 kms of range.
    
    
    * **_python geoindex.py -q 12.00 77.00 3_**
    
    This should give us first location which has distance of around 1 Km.

   The q option is for querying. Required parameters for this options are the starting latitude and longitude and      the radius.
