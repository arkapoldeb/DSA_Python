n = int(input("Enter number of elements in first tuple: "))

t1 = ()

for i in range(n):
    x = int(input("Enter element: "))
    t1 = t1 + (x,)

n = int(input("Enter number of elements in second tuple: "))

t2 = ()

for i in range(n):
    x = int(input("Enter element: "))
    t2 = t2 + (x,)

print("Before swapping:")
print("First tuple:", t1)
print("Second tuple:", t2)

t1, t2 = t2, t1

print("After swapping:")
print("First tuple:", t1)
print("Second tuple:", t2)