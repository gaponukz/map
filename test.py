from geopy.distance import distance, Distance

point = distance(miles=10).destination((34, 148), bearing=90, distance=Distance(100))

print(point.longitude, point.latitude)