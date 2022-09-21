import math

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
    
    def has_intersections_with(self, circle: 'Circle'):
        max_dist = self.radius + circle.radius
        actual_dist = self.center.distance_to(circle.center)

        return actual_dist <= max_dist

    def has_inside(self, circle: 'Circle'):
        between_centers = self.center.distance_to(circle.center)

        return between_centers + circle.radius <= self.radius

    def __str__(self):
        return f"{self.__class__.__name__}(radius={round(self.radius, 3)})"
