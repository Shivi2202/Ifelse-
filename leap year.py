# check the year is leap year or not.

Year= int(input("enter year : "))
if Year%4==0 and Year%100!=0: 
    print("it is a leap year")
elif Year%400==0 and Year%100==0 and Year%4==0:
    print("it is a cantury leap year")
else:
    print("it is not a leap year")