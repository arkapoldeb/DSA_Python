n = int(input("Enter the number of elements: "))

list1 = []

for i in range(n):
    x = int(input("Enter element: "))
    list1.append(x)

print("Original list:", list1)

list1[0], list1[-1] = list1[-1], list1[0]

print("After interchange:", list1)