
counter=1
while counter<=5:
    print("the counter ", counter, "Number")
    counter=int(input("Enter number:-"))
    counter=counter+1
    
    if counter!=5:
        print("try againr")
    elif counter==5:
        
        print("good guess")
        
else:
    print("Game over")