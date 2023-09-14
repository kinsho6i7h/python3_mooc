"""
Please write a program which asks the user for a word and then prints out the
number of characters, if there was more than one typed in.
"""

word = str(input("Please type in a word: "))
word_len = int(len(word))

if len(word) >1:
    print(f"There are {word_len} letters in the word {word}")
    
print("Thank you!")