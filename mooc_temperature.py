"""
Sample Output
-------------
Please type in a temperature (F): 101
101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

Please type in a temperature (F): 21
21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
Brr! It's cold in here!
"""

fahrenheit = float(input("Please type in a temperature (F): "))
celsius = float((fahrenheit - 32) * 5.0 / 9.0)

if celsius == 0 or celsius > 0:
    print(
        f"{int(fahrenheit)} degrees Fahrenheit equals {celsius:.2f} degrees Celsius"
    )

if celsius < 0:
    print(
        f"{int(fahrenheit)} degrees Fahrenheit equals {celsius:.2f} degrees Celsius"
    )
    print("Brr! It's cold in here!")
