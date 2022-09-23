from utils import *

circle1 = Circle(100, (50.41102382133477, 30.62288617200263))
circle2 = Circle(100, (50.41100696142142, 30.622844755542562))

print(circle1.has_intersections_with(circle2))