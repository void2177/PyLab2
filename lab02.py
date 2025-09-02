name = "carter_brody"
age = 18
height = 5.6
favorite_color = "black"
print(name)
print(age)
print(height)
print(favorite_color)
print(name, age, height, favorite_color)
print(f"Hello {name}, my favorite color is {favorite_color}!")

test = "hello"
print(f"{test:>20}")
print (f"{test:^50}")

num = 89495825.685
print(f"{num:,}")

import math
pi = math.pi
print(f"{pi:f}")
print(f"{pi:.3f}")

print(f"""
    Here is my record!
    Name: {name}
    Age: {age}
        Height {height}
Favorite Color: {favorite_color}""")

radius = 5
circle_area = pi * radius ** 2
print(circle_area)
print(f"{circle_area:.1f}")

import math
sqrt = math.sqrt
agrt = sqrt(age)
print(agrt)

print(f"{math.sin(age), math.cos(age)}")

print(f"""
{age + 5},
{age - 4},
{age * height},
{height / 2}, 
{age / 3},
{age ** 2},
""")
import math
temperature = input("What fahrenheit degree temperature would you like to convert to celsius?")
print(f"{temperature - 32 * (5/9)}")