# Check the triangle is valid or not.

a = int(input("enter the first angle: "))
b = int(input("enter the second angle: "))
c = int(input("ente the third angle: "))
sum = a+b+c
if sum==180:
    print("triangle a,b,c is valid")
else:
    print("tringle a,b,c is invalid")

