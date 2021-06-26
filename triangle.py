# Check the inputs contain a triangle or not.

a=int(input("enter first angle: "))
b=int(input("enter second angle: "))
c=int(input("enter third angle: "))
sum=a+b+c
if a==b==c and sum==180:
    print("equilateral triangle")
elif a==b!=c or a!=b==c or a==c!=b and sum==180:
    print("isosceles triangle")
elif a!=b!=c and sum==180:
    print("scalene triangle")
else:
    print("invalid triangle")