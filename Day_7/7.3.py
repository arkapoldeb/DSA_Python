n = int(input("Enter a number: "))

temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    i = 1

    while i <= digit:
        fact = fact * i
        i = i + 1

    sum = sum + fact
    temp = temp // 10

if sum == n and n > 0:
    print("Special number")
else:
    print("Not a Special number")