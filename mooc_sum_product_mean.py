"""
Sum And Product
"""

import statistics

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

sum = number1 + number2
product = number1 * number2
mean = statistics.mean([number1, number2])

print(f"The sum of the numbers: {sum} ")
print(f"The product of the numbers: {product} ")
print(f"The mean of the numbers: {mean} ")