x=input("Enter the length of the triangle: ")
y=input("Enter the breadth of the triangle: ")
z=input("Enter the height of the triangle: ")
if(x==y and x==z):
    print("The triangle is an equilateral triangle")
elif(x==y or x==z or y==z):
    print("The triangle is an isosceles triangle")
else:
    print("The triangle is a scalene triangle")