"""
Please write a program which asks for two integer numbers.
The program should then print out whichever is greater.
If the numbers are equal, the program should print a different message.

Please type in the first number: 5
Please type in another number: 3
The greater number was: 5

Please type in the first number: 5
Please type in another number: 5
The numbers are equal!
"""

x = int(input("Please type in the first number: "))
y = int(input("Please type in another number: "))

if x > y:
    print(f"The greater number was: {x}")
elif x < y:
    print(f"The greater number was: {y}")
else:
    print("The numbers are equal!")