n = int(input("Enter number of elements: "))

t1 = ()

for i in range(n):
    x = int(input("Enter element: "))
    t1 = t1 + (x,)

start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

t2 = t1[start:end]

print("Original tuple:", t1)
print("New tuple:", t2)