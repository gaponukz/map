from utils import *

circle = Circle(1052.0418381213346, (50.40444089177163, 30.62135376141017))
new_circle1 = circle.build_neighboring_circle_on_angel(90)
new_circle2 = circle.build_neighboring_circle_on_angel(180)

print(new_circle1.center.lat, new_circle1.center.lng)
print(new_circle2.center.lat, new_circle2.center.lng)
