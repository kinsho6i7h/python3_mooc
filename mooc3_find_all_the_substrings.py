"""
Please make an extended version of the previous program,
which prints out all the substrings which are at least three characters long,
and which begin with the character specified by the user.
You may assume the input string is at least three characters long.

Please type in a my_word: mammoth
Please type in a character: m
mam
mmo
mot

Please type in a my_word: banana
Please type in a character: n
nan

"""

my_word = input("Please type in a my_word: ")
my_char = input("Please type in a character: ")
iterate = 0

while iterate < len(my_word)-2:
    if my_word[iterate] == my_char:
        print(my_word[iterate:iterate+3])
    iterate += 1