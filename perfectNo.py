# Perfect number
# sum of proper divisors = number Eg: 6=divisor(1+2+3)
no=int(input("Enter a number: "))
sum=0
#print("Factor:",end=" ")
for i in range(1,int(no/2)+1):
    if no%i==0:
        print("Factor")
        print(i)
        sum=sum+i
    print("Loop")
    print(i)

if sum==no:
    print("\nThe given number is perfect number")
else:
    print("\nThe given number is not a perfect number")
