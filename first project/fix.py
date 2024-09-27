def area_equation(x, y):
    area = x * y
    return area

def volume_equation(a, b, c):
    temp = area_equation(a, b)
    result = temp * c
    return result

length_area = 5
hight_area = 3
area = area_equation(length_area, hight_area)
print(f"The shape's area is: {area}")

hight = 4
width = 6
base = 2
volume = volume_equation(hight, width, base)
print(f"The shape's volume is: {volume}")