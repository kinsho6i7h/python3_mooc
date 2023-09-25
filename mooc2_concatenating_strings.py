codes = ""
attempts = 0

while True:
    code = input("Please type in your PIN: ")
    if code == "quit":
        break
    attempts += 1
    codes += code + ", "
    print(codes)
