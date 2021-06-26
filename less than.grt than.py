# Check the number is less than 10 or greater than 20 or less than 20 and greater than 10.

num=int(input("enter number : "))
if num<10:
    print(num,"is less than 10")
elif num>10 and num<20:
    print(num,"is greater than 10 and less than thn 20")
elif num>20:
    print(num,"is greater than 20")
