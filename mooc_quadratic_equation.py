"""
quadratic equation
---------

x = (-b ± sqrt(b²-4ac))/(2a)

from math import sqrt

a = float(input("Please give your first number: "))
b = float(input("Please give your second number: "))
c = float(input("Please give your third number: "))


# calculate the discriminant
d = (b**2) - (4 * a * c)

# find two solutions
solution1 = (-b - sqrt(d)) / (2 * a)
solution2 = (-b + sqrt(d)) / (2 * a)

print("The two solutions are {0} and {1}".format(solution1, solution2))

code fails
"""
# import complex math module
import cmath

a = float(input("Enter your first number a: "))
b = float(input("Enter your second number b: "))
c = float(input("Enter your third number c: "))

# calculate the discriminant
d = (b**2) - (4 * a * c)

# find two solutions
solution1 = (-b - cmath.sqrt(d)) / (2 * a)
solution2 = (-b + cmath.sqrt(d)) / (2 * a)
print("The two solutions are {0} and {1}".format(solution1, solution2))
