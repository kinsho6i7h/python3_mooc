"""
Please write a program which asks the user to type in a string.
The program then prints out all the substrings which begin with 
the first character, from the shortest to the longest. 

Have a look at the example below.

Please type in a string: test
t
te
tes
test
"""

iteration = 0
input_string = str(input("Please type in a string: "))
input_string_length = int(len(input_string))

while True:
    if iteration < input_string_length:
        print(input_string[0:iteration])
        iteration += 1
    else:
        break
print(input_string)
