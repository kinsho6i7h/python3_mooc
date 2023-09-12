"""This module displays basic hello world. py3.11 """

msg = "Hello World"
print(msg)
print("Keith")

mymsg = "This is python3!"
print(mymsg)

txt = input("Type something to test this out: ")

print(f"Is this what you just said? {txt}")

ans = input("Please answer 'y', or 'n': ")
if ans == "y":
    print("thought so: \n")
elif ans == "n":
    print("you may be mistaken: \n")

print("End Program")
