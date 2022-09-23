import math
import geopy.distance

'''
 NOTE: dev/mul 1000 because all in meters!
'''

class Point(object):
    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng
    
    def distance_to(self, point) -> float:
        # calculate Distance Between Two Points on Earth

        point = point if isinstance(point, Point) else Point(*point)

        lat1, lon1 = math.radians(self.lat), math.radians(self.lng)
        lat2, lon2 = math.radians(point.lat), math.radians(point.lng)

        a = math.sin((lat2 - lat1) / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2)**2

        # 6371 - radius of earth in kilometers
        return 2 * 6371 * math.asin(math.sqrt(a))
    
    def __str__(self):
        return f"{self.__class__.__name__}(radius={round(self.lat, 3)}, {round(self.lng, 3)})"

class Circle(object):
    def __init__(self, radius: float, center: Point):
        self.radius = radius
        self.center = center if isinstance(center, Point) else Point(*center)
    
    def has_intersections_with(self, circle: 'Circle') -> bool:
        # check if 'self circle' has intersections with 'argument circle'

        max_dist = self.radius + circle.radius
        actual_dist = self.center.distance_to(circle.center) * 1000

        return actual_dist >= max_dist

    def has_inside(self, circle: 'Circle') -> bool:
        # check if 'argument circle' inside the 'self circle'

        between_centers = self.center.distance_to(circle.center) * 1000

        return between_centers + circle.radius <= self.radius
    
    def build_neighboring_circle_on_angel(self, angel: float) -> 'Circle':
        # return Circle that touches a 'self circle' at an angel
        # NOTE: distance between centers - diameter of 'self circle'
        center_point = geopy.distance.distance(miles=to_miles(self.radius * 2) / 1000).destination((self.center.lat, self.center.lng), bearing=angel)

        return Circle(self.radius, (center_point.latitude, center_point.longitude))

    def build_inside_circle_on_angel(self, angel: float, radius) -> 'Circle':
        # return Circle that touches inside a 'self circle' at an angel
        center_point = geopy.distance.distance(miles=to_miles((self.radius - radius) / 1000)).destination((self.center.lat, self.center.lng), bearing=angel)

        return Circle(radius, (center_point.latitude, center_point.longitude))

    def __str__(self):
        return f"{self.__class__.__name__}(radius={round(self.radius, 3)})"

def to_kilometers(miles: float) -> float:
    return miles / 0.62137119

def to_miles(kilometers: float) -> float:
    return kilometers * 0.62137119
