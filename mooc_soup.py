name = str(input("Please tell me your name: "))

if name != "Jerry":
    num_portions = int(input("How many portions of soup? "))
    portion = float(5.90)
    total_cost = abs(float(num_portions * portion)) # can't be negative value
    print(f"The total cost is {total_cost}")
    
print("Next please!")
