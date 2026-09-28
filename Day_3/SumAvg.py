sum = 0
count = 0

for i in range(4):
    n = int(input("Enter a number: "))

    if n == 0:
        break

    sum = sum + n
    count = count + 1

if count > 0:
    average = sum / count
    print("Sum =", sum)
    print("Average =", average)
else:
    print("No numbers were entered")