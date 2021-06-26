#check the number is divisible by 5 & 11 or not

a = int(input("enter a number : "))
if a%5==0 and a%11==0:
    print("a is divisible by 5 and 11")
elif a%5==0 and a%11!=0:
    print("a is divisible by 5 but not divisible by 11")
elif a%5!=0 and a%11==0:
    print("a is divisible by 11 but not divisible by 5")
else:
    print("a is not divisible by 5 and 11")