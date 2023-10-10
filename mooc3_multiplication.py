"""
Please write a program which asks the user for a positive integer number.
The program then prints out a list of multiplication operations until both
operands reach the number given by the user. See the examples below for details:

Please type in a number: 2
1 x 1 = 1
1 x 2 = 2
2 x 1 = 2
2 x 2 = 4

Please type in a number: 3
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9

"""

my_number = int(input("Please type in a number: "))
index_a = 1

# Nested loop follows

while index_a <= my_number:
    index_b = 1
    while index_b <= my_number:
        print(f"{index_a} x {index_b} = {index_a * index_b}")
        index_b += 1
    index_a += 1