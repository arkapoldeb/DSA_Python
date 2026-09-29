n = int(input("Enter the number of elements: "))

list1 = []

for i in range(n):
    x = int(input("Enter element: "))
    list1.append(x)

even = 0
odd = 0

for i in list1:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers:", even)
print("Odd numbers:", odd)