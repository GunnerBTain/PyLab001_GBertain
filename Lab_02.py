#Part 1
name = "Gunner Bertain"
age = 19
height = 5.11
favorite_color = "Yellow"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"Hello {name} ,my favorite color is {favorite_color}! I am {age} years old, and I am {height} feet tall")

print(f"""  
 Name: {name}
 Age: {age}
 Height: {height}
 Favorite Color: {favorite_color}
""")

from math import pi

radius = 5
circle_area = pi * radius**2
print(f"The area of the circle with a radius of {radius} is {circle_area:.1f}")

#Part 2
import math as m

sqrt_of_age = m.sqrt(age)
print(f"The square root of his age is: {sqrt_of_age:.2f}")
sin_height = m.sin(height)
cos_height = m.cos(height)
print(f"The cosine of height is: {cos_height:.2f}")
print(f"The sine of height is: {sin_height:.2f}")

#Part 3
sum_age = age + 5
dif_height = height - 4
product_age_height = age * height
quotient_height = height / 2
remainder_age = age / 3
age_power = age**2

print("Age + 5:",sum_age)
print("Difference between height and 4:",dif_height)
print("Product of age and height:",product_age_height)
print("Quotient of height divided by 2",quotient_height)
print("Remainder of age divided by 3:",remainder_age)
print("Age to the power of 2:",age_power)

#Part 4
fahrenheit = int(input("Enter degrees in fahrenheit and I'll convert it to celsius: "))
celsius = (fahrenheit - 32) * 5/9
print("Your fahrenheit temperature is", celsius,"degrees celsius.")

print("Lab 2 Finished!")