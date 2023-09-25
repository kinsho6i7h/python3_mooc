attempts = 0

while True:
    code = input("PIN: ")
    attempts += 1

    if code == "4321" and attempts == 1:
        success = True
        break

    elif code == "4321" and attempts > 1:
        success = False
        break

    print("Wrong")

if success:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
