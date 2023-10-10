"""
Please modify the previous program so that it also asks for the height,
and prints out a rectangle of hash characters accordingly.

Width: 10
Height: 3
##########
##########
##########

"""

width = int(input("Width: "))
height = int(input("Height: "))
iteration = 0

my_char = '#'

while True:
        if iteration < height:
                print(my_char * width)
                iteration += 1
        else:
            break
        