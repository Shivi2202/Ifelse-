# Find the percentage and grade for the respective subjects.

a=int(input("marks of physics: "))
b=int(input("marks of chemistry: "))
c=int(input("marks of biology: "))
d=int(input("marks of maths: "))
e=int(input("marks of computer: "))
per=(a+b+c+d+e)/5
if per>=90:
    print("percentage","=",per)
    print("Grade A")
elif per>=80:
    print("percentage","=",per)
    print("Grade B")
elif per>=70:
    print("percentage","=",per)
    print("Grade C")
elif per>=60:
    print("percentage","=",per)
    print("Grade D")
elif per>=40:
    print("percentage","=",per)
    print("Grade E")
elif per<40:
    print("percentage","=",per)
    print("Grade F","fail")
else:
    print("fail")