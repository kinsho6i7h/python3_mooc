"""
Please write a program which asks the user for two strings and then prints
out whichever is the longer of the two - that is, whichever has the more characters.
If the strings are of equal length, the program should print out 

"The strings are equally long".

Some examples of expected behaviour:

Please type in string 1: hey
Please type in string 2: hiya
hiya is longer

Please type in string 1: howdy doody
Please type in string 2: hola
howdy doody is longer

Please type in string 1: hey
Please type in string 2: bye
The strings are equally long

"""

word1 = str(input("Please type in string 1: "))
word2 = str(input("Please type in string 2: "))

length_word1 = len(word1)
length_word2 = len(word2)

if length_word1 > length_word2:
    print(f"{word1} is longer")
if length_word2 > length_word1:
    print(f"{word2} is longer")
if length_word1 == length_word2:
    print("The strings are equally long")
