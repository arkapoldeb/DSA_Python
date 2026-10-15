d1 = {}
d2 = {}

n = int(input("Enter number of elements in first dictionary: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value

m = int(input("Enter number of elements in second dictionary: "))

for i in range(m):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d2[key] = value

search = input("Enter key to search from first dictionary: ")

if search in d1:
    if search in d2.values():
        print("Key is present in values of second dictionary")
    else:
        print("Key is not present in values of second dictionary")
else:
    print("Key is not present in first dictionary")