x=int(input("Enter a number to check perfect Number: "))
i=1
sum=0
while(i<x):
    if x%i==0:
        sum+=i
    i+=1
if sum==x:
    print(x,"is a perfect number")
else:
    print(x,"is not a perfect number")
