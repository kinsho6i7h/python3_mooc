"""
String Indexing

Please type in a string: monkey
m
o
k

"""

input_string = input("Please type in a string: ")
print(input_string[0])
print(input_string[1])
print(input_string[3])

"""

Since the first character in a string has the index 0, the last character has the index length - 1.
The following program prints out the first and the last characters of a string:

Please type in a string: testing
First character: t
Last character: g
"""

input_string = input("Please type in a string: ")
print("First character: " + input_string[0])
print("Last character: " + input_string[len(input_string) - 1])

"""
The following program loops through all the characters in a string from first to last:

Please type in a string: test
t
e
s
t
"""

input_string = input("Please type in a string: ")
index = 0
while index < len(input_string):
    print(input_string[index])
    index += 1
    
"""
You can also use negative indexing to access characters counting from the end of the string.
The last character in a string is at index -1, the second to last character
is at index -2, and so forth.
You can think of input_string[-1] as shorthand for input_string[len(input_string) - 1].

Please type in a string: testing
First character: t
Last character: g

"""

input_string = input("Please type in a string: ")
print("First character: " + input_string[0])
print("Last character: " + input_string[-1])

"""
IndexError: string index out of range

If you tried the above examples for yourself, you may already have come across
the error message IndexError: string index out of range.
This error appears if you try to access an index which is not present in the string.

Please type in a string: introduction to programming
The tenth character: i
"""

input_string = input("Please type in a string: ")
print("The tenth character: " + input_string[9])

"""
Please type in a string: python

Traceback (most recent call last):
File "", line 1, in 
IndexError: string index out of range

Sometimes an indexing error is caused by a bug in the code. For example,
it is quite common to index too far when trying to access the last character in a string:
"""

input_string = input("Please type in a string: ")
print("Last character: " + input_string[len(input_string)])

"""
Since string indexing begins at zero, the last character is at index len(input_string) - 1,
not at len(input_string).

There are situations where the program should prepare for errors caused by input from the user:

"""

input_string = input("Please type in a string: ")
if len(input_string) > 0:
    print("First character: " + input_string[0])
else:
    print("The input string is empty. There is no first character.")
    
"""
In the example above, if the programmer hadn't included a check for the length
of the input string, a string of length zero would have caused an error.
A string of length zero is also called an empty string,
and here it would be achieved by just pressing Enter at the input prompt.
"""


