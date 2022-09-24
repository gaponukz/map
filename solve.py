import json
import time
from utils import *

E = 1 # constant of angle

with open("setting.json", 'r', encoding='utf-8') as out:
    setting = json.load(out)

little_radius: float = setting['little_radius']
big_radius: float = setting['big_radius']
lat, lng = setting['center']

start_time = time.time()

main_circle = Circle(big_radius, (lat, lng))

circles: list[Circle] = []
current_circle = main_circle.build_inside_circle_on_angel(0, little_radius)
circles.append(current_circle)

for circle in circles:
    for angel in range(0, 360, E):
        new_circle = circle.build_neighboring_circle_on_angel(angel)

        if main_circle.has_inside(new_circle):
            if all([not _circle.has_intersections_with(new_circle) for _circle in circles if new_circle != _circle]):
                circles.append(new_circle)
    
    print(len(circles))

    if circle == circles[-1]:
        break

print(time.time() - start_time)