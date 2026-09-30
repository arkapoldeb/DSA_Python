n = int(input("Enter number of elements: "))

t1 = ()
t2 = ()

print("Enter elements for first tuple:")

for i in range(n):
    x = int(input("Enter element: "))
    t1 = t1 + (x,)

print("Enter elements for second tuple:")

for i in range(n):
    x = int(input("Enter element: "))
    t2 = t2 + (x,)

result = ()

for i in range(n):
    x = t1[i] % t2[i]
    result = result + (x,)

print("First tuple:", t1)
print("Second tuple:", t2)
print("Modulo tuple:", result)