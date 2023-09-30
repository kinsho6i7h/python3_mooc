"""

Please write a new version of the program in the previous exercise. 
In addition to the result it should also print out the calculation performed:

Limit: 2
The consecutive sum: 1 + 2 = 3

Limit: 10
The consecutive sum: 1 + 2 + 3 + 4 = 10

Limit: 18
The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

"""

upper_limit = int(input("Limit: "))
my_num = 1
final_num = 1
consecutive = "The consecutive sum: "
my_statement = ""
while final_num < upper_limit:
    my_statement += f"{my_num} + "
    my_num += 1
    final_num += my_num
print(f"{consecutive} {my_statement}" + f"{my_num} = {final_num}")
