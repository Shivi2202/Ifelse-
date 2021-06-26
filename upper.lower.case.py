#check whether the input is in uppercase or lowercase

case = input("enter a character")
if case>="A" and case<="Z":
    print("uppercase")
elif case>="a" and case<="z":
    print("lowercase")
else:
    print("invalid character")
