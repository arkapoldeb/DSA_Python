d = {}

n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value
print("Original Dictionary:", d)
a = dict(sorted(d.items()))
print("Dictionary sorted by Key:", a)
b = dict(sorted(d.items(), key=lambda x: x[1]))

print("Dictionary sorted by Value:", b)