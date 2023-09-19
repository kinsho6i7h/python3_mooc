"""
Some say paying taxes makes Finns happy, so let's see if the secret of happiness
lies in one of the taxes set out in Finnish tax code.

According to the Finnish Tax Administration, a gift is a transfer of property to
another person against no compensation or payment. If the total value of the
gifts you receive from the same donor in the course of 3 years is €5,000 or
more, you must pay gift tax.

When the gift is received from a close relative or a family member, the amount
of tax to be paid is determined by the following table.

Value of gift	Tax at the lower limit	Tax rate for the exceeding part (%)
    5000            — 25000	        100	    8
    25000           — 55000	        1700	10
    55000           — 200000	    4700	12
    200000          — 1000000	    22100	15
    1000000                 	    142100	17

So, for a gift of 6000 euros the recipient pays a tax of 180 euros
(100 + (6000 - 5000) * 0.08). Similarly, for a gift of 75000 euros the
recipient pays a tax of 7100 euros (4700 + (75000 - 55000) * 0.12).

Please write a program which calculates the correct amount of tax for a gift
from a close relative. Have a look at the examples below to see what is
expected. Notice the lack of thousands separators in the input values
- you may assume there will be no spaces or other thousands separators in
the numbers in the input, as we haven't yet covered dealing with these.

Value of gift: 3500
No tax!

Value of gift: 5000
Amount of tax: 100.0 euros

Value of gift: 27500
Amount of tax: 1950.0 euros

"""

gift_value = int(input("Value of gift: "))

if int (gift_value) < 5000:
    print("No tax!")

elif int (gift_value) in range(4999, 25001):
    tax = (100 + (gift_value - 5000) * 0.08)
    print(f"Amount of tax: {tax} euros")

elif int( gift_value) in range(24999, 55001):
    tax = (1700 + (gift_value - 25000) * 0.10)
    print(f"Amount of tax: {tax} euros")

elif int( gift_value) in range(44999, 199999):
    tax = (4700 + (gift_value - 55000) * 0.12)
    print(f"Amount of tax: {tax} euros")

elif int( gift_value) in range(199999, 1000001):
    tax = (22100 + (gift_value - 200000) * 0.15)
    print(f"Amount of tax: {tax:.4f} euros")

elif int(gift_value) >= 1000000:
    tax = (142100 + (gift_value -1000000) * 0.17)
    print(f"Amount of tax: {tax} euros ")



