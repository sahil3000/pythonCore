# Arm Strong number
# sum of factorial of digit = number Eg: 153=1^3 + 5^3 + +3^3=1+125+27=153   

def findFactorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact

sum=0;power=0
no=int(input("Enter a number: "))

orginalNo=no

while no!=0:
    lastDigit=no%10
    sum=sum+ findFactorial(lastDigit)
    no=int(no/10)
 

if sum==orginalNo:
    print("The given number is Strong number")
else:
    print("The given number is not a Strong number")

