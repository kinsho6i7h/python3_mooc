"""
Please write a program which asks the user for a string and then prints it out
so that exactly 20 characters are displayed. If the input is shorter than 20 characters,
the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Please type in a string: python

**************python

Please type in a string: alongerstring

*******alongerstring

Please type in a string: averyverylongstring

*averyverylongstring

"""

max_string_length = 20
my_char = '*'

input_string = str(input("Please type in a string: "))
input_string_length = len(input_string)

asterix_length = int(max_string_length - input_string_length)
print (f"{my_char * asterix_length}{input_string}")

