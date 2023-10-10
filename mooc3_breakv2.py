# 2nd version without the break command

my_sum = 0
my_number = 0

while my_number != -1:
    my_number = int(input("Please type in a number, -1 to exit: "))
    if my_number != -1:
        my_sum += my_number

print (f"The sum is {my_sum}")