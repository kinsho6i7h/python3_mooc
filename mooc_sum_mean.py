"""
Number 1: 2
Number 2: 1
Number 3: 6
Number 4: 7
The sum of the numbers is 16 and the mean is 4.0
"""
import statistics

num1 = int(input(f"Number 1:"))
num2 = int(input(f"Number 2:"))
num3 = int(input(f"Number 3:"))
num4 = int(input(f"Number 4:"))

sum = int( num1 + num2 + num3 + num4)
numlist = ([num1, num2, num3, num4])
mean_result = float (statistics.mean (numlist))

print(f"The sum of the numbers is {sum} and the mean is {mean_result}")