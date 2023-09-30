"""

Please write a program which asks the user to type in a limit.
The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) 
until the sum is at least equal to the limit set by the user.
The program should function as follows:

Limit: 2
3

Limit: 10
10

Limit: 18
21

"""

limit = int(input("Limit: "))
number = 1 
total = 1 
 
while total < limit:
    number += 1 
    total += number 
print(total)