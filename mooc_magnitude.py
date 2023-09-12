"""
Sample output
-------------
Please type in a number: 2
This number is smaller than 1000
This number is smaller than 100
This number is smaller than 10
Thank you!
"""

number = abs(int(input("Please type in a number: ")))

if number < 1000:
    print("This number is smaller than 1000")
if number < 100:
    print("This number is smaller than 100")
if number < 10:
    print("This number is smaller than 10")

print("Thank you!")