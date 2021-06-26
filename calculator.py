# Write a program to calculate to numbers.

num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
num3 = input("operator : ")
if num3=="+":
    print(num1+num2,"sum")
elif num3=="-":
    print(num1-num2,"subtract")
elif num3=="*":
    print(num1*num2,"multiple")
elif num3=="/":
    print(num1/num2,"div")
elif num3=="//":
    print(num1//num2,"floor div")
elif num3=="**":
    print(num1**num2,"exp")
elif num3=="%":
    print(num1%num2,"mod")
else:
    print("invalid")