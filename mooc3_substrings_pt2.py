"""
Please write a program which asks the user to type in a string.
The program then prints out all the substrings which end with the
last character, from the shortest to the longest.

Have a look at the example below.

Please type in a string: test
t
st
est
test
"""

word = input("Please type in a string: ")
iterator = -1
my_sum = "" # create variable
while iterator >= -len(word):
    my_sum = word[iterator] + my_sum
    print(my_sum)
    iterator -= 1
    
"""
Model Solution::

string = input("Please type in a string: ")
 
start = len(string) - 1
while start >= 0:
    print(string[start:])
    start -= 1
"""

