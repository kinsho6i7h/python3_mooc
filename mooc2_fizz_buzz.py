fizz_buzz = int(input("Number: "))

if fizz_buzz % 3 == 0 and fizz_buzz % 5 == 0:
    print("FizzBuzz")
    
elif fizz_buzz % 3 == 0:
    print("Fizz")
        
elif fizz_buzz % 5 == 0:
    print("Buzz")