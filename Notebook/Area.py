def area_circle(radius):
    global pi
    pi = 3.14
    area = round(pi * radius ** 2, 2)
    return area
print(area_circle(5))
print(pi)