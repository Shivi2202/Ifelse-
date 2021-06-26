num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))
if num2>num1>num3 or num2<num1<num3:
    print("num1 is second larg",num1)
elif num1>num2>num3 or num1<num2<num3:
    print("num2 is second large",num2)
elif num1>num3>num2 or num1<num3<num2:
    print("num3 is second large",num3)
else:
    print("num1=num2=num3")





a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if b>a>c or b<a<c:
    print("a is second max",a)
elif a>b>c or a<b<c:
    print("b is second max",b)
elif a>c>b or a<c<b:
    print("c is second max",c)
