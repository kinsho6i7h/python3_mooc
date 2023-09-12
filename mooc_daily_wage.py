"""
Sample Outputs
--------------
Hourly wage: 8.5
Hours worked: 3
Day of the week: Monday
Daily wages: 25.5 euros
--------------
Hourly wage: 12.5
Hours worked: 10
Day of the week: Sunday
Daily wages: 250.0 euros
--------------
"""
h_wage = float(input("Hourly wage: "))
h_worked = float(input("Hours worked: "))
day_week = str(input("Day of the week: "))
daily_wages = float(h_wage * h_worked)

if day_week =="Sunday":
    print(f"Daily wages: {daily_wages*2} euros")
    
if day_week !="Sunday":
    print(f"Daily wages: {daily_wages} euros")


