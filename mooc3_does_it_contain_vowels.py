"""
Please write a program which asks the user to input a string.
The program then prints out different messages if the string contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

Please type in a string: hello there
a not found
e found
o found

Please type in a string: hiya
a found
e not found
o not found
"""

vowel_a = 'a'
vowel_e = 'e'
vowel_o = 'o'
input_string = str(input("Please type in a string: "))


if vowel_a in input_string:
        print(f"{vowel_a} found")
if vowel_a not in input_string:
        print(f"{vowel_a} not found")

        
if vowel_e in input_string:
        print(f"{vowel_e} found")
if vowel_e not in input_string:
        print(f"{vowel_e} not found")

        
if vowel_o in input_string:
        print(f"{vowel_o} found")
if vowel_o not in input_string:
        print(f"{vowel_o} not found")
        
"""
Model Solution:

string = input("Please type in a string: ")
vowels = "aeo"
index = 0
 
while index < len(vowels):
    vowel = vowels[index]
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1
"""
