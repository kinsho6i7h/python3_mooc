"""
Sample Outputs
--------------
How many points are on your card? 55
Your bonus is 10 %
You now have 60.5 points

How many points are on your card? 95
Your bonus is 10 %
Your bonus is 15 %
You now have 120.175 points
"""

points = int(input("How many points are on your card? "))

if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

elif points == 100 or points > 100:
    points *= 1.15
    print("Your bonus is 15 %")

print(f"You now have {points:.2f} points")

