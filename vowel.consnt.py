# Check the input is is a vowel or consonant.

var = input("enter a letter: ")
if var=="a" or var=="e" or var=="i" or var=="o" or var=="u":
    print("it is a vowel")
elif var=="A" or var=="E" or var=="I" or var=="O" or var=="U":
    print("it is a vowel")
elif var:
    print("it is a consonant")
else:
    print("integer or special character")
