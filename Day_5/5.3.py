n = int(input("Enter number of tuple elements: "))

t1 = ()

for i in range(n):
    x = int(input("Enter tuple element: "))
    t1 = t1 + (x,)

m = int(input("Enter number of list elements: "))

list1 = []

for i in range(m):
    x = int(input("Enter list element: "))
    list1.append(x)

print("Tuple:", t1)
print("List:", list1)

for i in t1:
    list1.append(i)

print("After adding tuple to list:", list1)