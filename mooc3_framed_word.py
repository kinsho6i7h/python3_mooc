"""
Please write a program which asks the user for a string
and then prints out a frame of * characters with the word in the centre.
The width of the frame should be 30 characters. You may assume the input
string will always fit inside the frame.

If the length of the input string is an odd number, you may print out
the word in either of the two possible centre locations.

Word: testing

******************************
*          testing           *
******************************

Word: python

******************************
*           python           *
******************************

"""
stars = 30
my_char = '*'
input_string = str(input("Word: "))
word_string = input_string.center(28, ' ')
star_string = my_char * stars

print(star_string)
print(f"*{word_string}*")
print(star_string)