"""
Let's create a program along the lines of the example above.
This program should print out the message "hi" and then ask "Shall we continue?"
until the user inputs "no". Then the program should print out "okay then" and
finish. Please have a look at the example below.

hi
Shall we continue? yes

hi
Shall we continue? oui

hi
Shall we continue? jawohl

hi
Shall we continue? no

okay then
"""

while True:
    print("hi")
    my_answer = str(input("Shall we continue? "))
    if my_answer == "no":
        break

print("okay then")
