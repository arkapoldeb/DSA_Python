n = int(input("Enter number of elements: "))

list1 = []

for i in range(n):
    x = int(input("Enter number: "))
    list1.append(x)

result = []

for i in list1:
    cube = i ** 3
    result.append((i, cube))

print("Original list:", list1)
print("List of tuples:", result)