import json
import time
from utils import *

E = 2 # constant of angle

with open("setting.json", 'r', encoding='utf-8') as out:
    setting = json.load(out)

little_radius: float = setting['little_radius']
big_radius: float = setting['big_radius']
lat, lng = setting['center']

start_time = time.time()

main_circle = Circle(big_radius, (lat, lng))

circles: list[Circle] = []

for angel in range(0, 330, E):
    new_circle = main_circle.build_inside_circle_on_angel(angel, little_radius)

    if main_circle.has_inside(new_circle):
        if all([not _circle.has_intersections_with(new_circle) for _circle in circles if new_circle != _circle]):
            circles.append(new_circle)

print(len(circles))

for circle in circles:
    for angel in range(60, 330, E):
        new_circle = circle.build_neighboring_circle_on_angel(angel)

        if main_circle.has_inside(new_circle):
            if all([not _circle.has_intersections_with(new_circle) for _circle in circles if new_circle != _circle]):
                circles.append(new_circle)
                break
    
    print(len(circles))

    if circle == circles[-1]:
        break

print(time.time() - start_time)
