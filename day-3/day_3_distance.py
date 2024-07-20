from qgis.core import QgsDistanceArea

san_francisco = (37.7749, -122.4194)
new_york = (40.661, -73.944)

# Initialize a class and construct an object 
d = QgsDistanceArea()
d.setEllipsoid('WGS84')

lat1, lon1 = san_francisco
lat2, lon2 = new_york
point1 = QgsPointXY(lon1, lat1)
point2 = QgsPointXY(lon2, lat2)

distance = d.measureLine([point1, point2])
print('Distance in meters', distance) # in meters
print('Distance in kilometers', distance/1000) # in kilometers

### Exercise 1
las_vegas = (36.1699, -115.1398)
lat3, lon3 = las_vegas
point3 = QgsPointXY(lon3, lat3)
distance13 = d.measureLine([point1, point3])
distance32 = d.measureLine([point3, point2])
print((distance13 + distance32)/1000)

### Convert to miles
distance_mi = d.convertLengthMeasurement(distance, Qgis.DistanceUnit.DistanceMiles)
print('Distance in miles', distance_mi)