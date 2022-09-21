import math

Point = tuple[float, float]

def distance(point1: Point, point2: Point) -> float:
    # calculate Distance Between Two Points on Earth

    lat1, lon1 = math.radians(point1[0]), math.radians(point1[1])
    lat2, lon2 = math.radians(point2[0]), math.radians(point2[1])

    a = math.sin((lat2 - lat1) / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2)**2

    # 6371 - radius of earth in kilometers
    return 2 * 6371 * math.asin(math.sqrt(a))

if __name__ == '__main__':
    point1 = (53.32055555555556, -1.7297222222222221)
    point2 = (53.31861111111111, -1.6997222222222223)

    print(distance(point1, point2), "K.M")