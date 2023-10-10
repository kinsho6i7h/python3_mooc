# 1st version using the break command

sum = 0
my_number = 0

while True:
    my_number = int(input("Please type in a number, -1 to exit: "))
    if my_number == -1:
        break
    sum += my_number

print (f"The sum is {sum}")