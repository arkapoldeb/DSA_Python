n = int(input("Enter the number of elements: "))

list1 = []

for i in range(n):
    x = int(input("Enter element: "))
    list1.append(x)

list1.sort()

print("Sorted list:", list1)
print("Second largest number:", list1[-2])