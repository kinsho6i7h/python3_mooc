"""
The table below outlines the grade boundaries on a certain university course.
Please write a program which asks for the amount of points received and then
prints out the grade attained according to the table.

points	grade
< 0	impossible!
0-49	fail
50-59	1
60-69	2
70-79	3
80-89	4
90-100	5
> 100	impossible!

How many points [0-100]: 76
Grade: 3

How many points [0-100]: -3
Grade: impossible!

"""

points = int(input("How many points [0-100]: "))

if points < 0 or points > 100:
    print("impossible! ")
elif int(points) in range (-1, 50):
    print ("Grade: fail ")
elif int(points) in range (49, 60):
    print ("Grade: 1")
elif int(points) in range (59, 70):
    print ("Grade: 2")
elif int(points) in range (69, 80):
    print ("Grade: 3")
elif int(points) in range (79, 90):
    print ("Grade: 4")
elif int(points) in range (89, 101):
    print ("Grade: 5")


    



    

    