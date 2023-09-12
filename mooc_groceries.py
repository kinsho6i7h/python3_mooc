"""
Projected Output

How many times a week do you eat at the student cafeteria? 4
The price of a typical student lunch? 2.5
How much money do you spend on groceries in a week? 28.5

Average food expenditure:
Daily: 5.5 euros
Weekly: 38.5 euros
"""
cafeteria = int(
    input("How many times a week do you eat at the student cafeteria? "))
lunch = float(input("The price of a typical student lunch? "))
groceries = float(
    input("How much money do you spend on groceries in a week? "))

cafeteria_total = (cafeteria * lunch)
weekly = float(groceries + cafeteria_total)
daily = float (weekly / 7)

print(f"Average food expenditure: ")
print(f"Daily:  {daily} euros ")
print(f"Weekly: {weekly} euros ")
