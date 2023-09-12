"""
prints name and age
"""
name = input("What is your name? ")
year_born = int(input("Which year were you born? "))
year_now = 2021
result = year_now - year_born
print(
    f"Hi {name}, you will be {result} years old at the end of the year{year_now}"
)
