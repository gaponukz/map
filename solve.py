import json
from utils import *

E = 1 # constant of angle

with open("setting.json", 'r', encoding='utf-8') as out:
    setting = json.load(out)

little_radius: float = setting['little_radius']
big_radius: float = setting['big_radius']
lat, lng = setting['center']

main_circle = Circle(big_radius, (lat, lng))

circles: list[Circle] = []
current_circle = main_circle.build_inside_circle_on_angel(0, little_radius)
circles.append(current_circle)

for circle in circles:
    for angel in range(0, 360, E):
        new_circle = circle.build_neighboring_circle_on_angel(angel)

        if main_circle.has_inside(new_circle) and all([not _circle.has_intersections_with(new_circle) for _circle in circles if new_circle != _circle]):
            circles.append(new_circle)
            print(angel)
            print(new_circle.center.lat, new_circle.center.lng)
    
    print(len(circles))
    break