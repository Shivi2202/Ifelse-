#check whether the input is alphabet,digit or special character

char = input("enter a character : ")
if (char>="A" and char<="Z") or (char>="a" and char<="z"):
    print("it is a alphabet")
elif char>="0" and char<="9":
    print("it is a digit")  
else:
    print("special character")
