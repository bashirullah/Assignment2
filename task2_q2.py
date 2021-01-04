ent_val=int(input("enter a number \t"))
num1=int(input("enter  1st value \t"))
num2=int(input("enter 2nd value \t"))

if(ent_val==1):
    print("addation ")
    sum=num1+num2
    print(sum)
    if(sum<0):
        print("Nagivate Number")

if(ent_val==2):
    print(" Substraction")
if(ent_val==3):
    print("division")
if(ent_val==4):
    print("Multiplication")

if(ent_val==5):
    print("average")
    avg= (num1+num2)/2
    print(avg)

