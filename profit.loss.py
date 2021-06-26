

cp=int(input("cost price : "))
sp=int(input("selling price : "))
if cp<sp:
    print("profit",":",sp-cp,"rupees")
elif cp>sp:
    print("loss",":",cp-sp,"rupees")
else:
    print("no profit,no loss")