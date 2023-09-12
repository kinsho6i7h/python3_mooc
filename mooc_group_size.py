"""
Sample Output

How many students on the course? 8
Desired group size? 4
Number of groups formed: 2
"""

students = int (input ("How many students on the course? "))
group_size = int (input ("Desired group size? "))

group_number = int (students / group_size)

left_over = int(students % group_size)
if left_over > 1:
    x = 1
else: 
    x = 0
    
print (f"Number of groups formed: {group_number + x}")