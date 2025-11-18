import math


def square(side):
    area_square = side*side
    return math.ceil(area_square)


print(square(1.7))
