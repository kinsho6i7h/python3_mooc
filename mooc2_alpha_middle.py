"""
Please write a program which asks the user for three letters.
The program should then print out whichever of the three letters
would be in the middle if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all lowercase.

Some examples of expected behaviour:

1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p

1st letter: C
2nd letter: B
3rd letter: A
The letter in the middle is B
"""

letter_1 = str(input("1st letter: "))
letter_2 = str(input("2nd letter: "))
letter_3 = str(input("3rd letter: "))

letter_list = ([letter_1, letter_2, letter_3])
sorted_letters = sorted(letter_list)

print(f"The letter in the middle is {sorted_letters[1]}")


