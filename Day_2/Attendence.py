x=int(input("Enter total number of class = "))
y=int(input("Enter number of classes attended = "))
if ((y/x)*100>=75):
    print("You are allowed to sit in exam")
else:
    z=input("Any medical cause? (Y/N) = ")
    if((y/x)*100>=40):
        if(z=='Y' or z=='y'):
            print("You are allowed to sit in exam")
        else:
            print("You are not allowed to sit in exam")

    