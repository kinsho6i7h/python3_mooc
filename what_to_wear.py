"""
Sample Outputs
--------------
What is the weather forecast for tomorrow?
Temperature: 7
Will it rain (yes/no): no
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you
--------------
What is the weather forecast for tomorrow?
Temperature: 21
Will it rain (yes/no): no
Wear jeans and a T-shirt
--------------
What is the weather forecast for tomorrow?
Temperature: 3
Will it rain (yes/no): yes
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you
Make it a warm coat, actually
I think gloves are in order
Don't forget your umbrella!
--------------
"""

print("What is the weather forecast for tomorrow?")
temp = float(input("Temperature:"))
rain = str(input("Will it rain (yes/no):"))

if temp >= 20:
    print("Wear jeans and a T-shirt")
    if rain == "yes":
        print("Don't forget your umbrella!")

elif int(temp) in range(11, 20):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    if rain == "yes":
        print("Don't forget your umbrella!")

elif int(temp) in range (6, 11):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    if rain == "yes":
        print("Don't forget your umbrella!")

elif temp <= 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
    if rain == "yes":
        print("Don't forget your umbrella!")
        
"""
Model Code
----------
print("What is the weather forecast for tomorrow?")

temperature = int(input("Temperature: "))

rain = input("Will it rain (yes/no): ")

print("Wear jeans and a T-shirt")

if temperature < 21:

    print("I recommend a jumper as well")

if temperature < 11:

    print("Take a jacket with you")

if temperature < 6:

    print("Make it a warm coat, actually")

    print("I think gloves are in order")

if rain == "yes":

    print("Don't forget your umbrella!")
    
"""
