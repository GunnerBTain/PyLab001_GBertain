#import math
from math import pi, sqrt
#print(math.pi)

radius = 5
area = pi * radius**2
print(area)

radius = 3
volume = (4/3 * pi * radius**3)
print(volume)

side_a = 3
side_b = 4
side_c_sq = side_a**2 + side_b**2
side_c = int(sqrt(side_c_sq))
print(side_c)

my_name = "Gunner Bertain"
name_len = len(my_name)
print(name_len)

first_name = "Gunner"
last_name = "Bertain"
print(name_len)

my_name = first_name +" "+ last_name
print(my_name)

my_name_uc = my_name.upper()
print(my_name_uc)
my_name_lc =my_name.lower()
print(my_name_lc)

age = 19
height = 70
weight = 167.0

print(type(age), type(height), type(weight))
BMI = weight / height**2 * 703
print(BMI)