"""
Please change the program from the previous exercise so that the user
gets to input also the base which is multiplied (in the previous program
the base was always 2).

Upper limit: 27
Base: 3
1
3
9
27

Upper limit: 1234567
Base: 10
1
10
100
1000
10000
100000
1000000

"""
count = 1
my_num_limit = int(input("Upper limit: "))
my_base = int(input("Base: "))

while count <= my_num_limit:
    print (count)
    count *= my_base