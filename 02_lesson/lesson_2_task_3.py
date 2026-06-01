import math

def square(side): # noqa
    area = side ** 2
    if not isinstance(side, int):
        return math.ceil(area)
    else:
        return area

print(square(5))     # noqa  
print(square(4.2))   # noqa
print(square(3.7))   # noqa  