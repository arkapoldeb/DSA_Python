n = int(input("Enter the number of elements: "))
list1 = []
for i in range(n):
    x = int(input("Enter element: "))
    list1.append(x)

positive = 0
negative = 0

for i in list1:
    if i > 0:
        positive = positive + 1
    elif i < 0:
        negative = negative + 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)