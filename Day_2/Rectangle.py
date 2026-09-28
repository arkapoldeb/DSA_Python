x = int(input("Enter the length of the rectangle: "))
y = int(input("Enter the width of the rectangle: "))
if (x==y):
    print("It is a Square.")
    area1 = x * y
    per1= 4 * x
    print("Area of sq: " ,area1," and perimeter: ",per1)
else:
    print("It is Rectangle.")
    area2 = x * y
    per2 = 2 * (x + y)
    print("Area of Rectange is ",area2," and perimeter: ",per2)