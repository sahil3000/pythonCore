# Arm Strong number
# sum of power of digit = number Eg: 153=1^3 + 5^3 + +3^3=1+125+27=153   
sum=0;power=0
no=int(input("Enter a number: "))
orginalNo=no
# print(pow(4,2))

# count power
while no!=0:
    power+=1
    no=int(no/10)

# print("Power = {}".format(power))

no=orginalNo        # set no= Original number
while no!=0:
    lastDigit=no%10
    sum=sum+pow(lastDigit,power)
    no=int(no/10)


if sum==orginalNo:
    print("The given number is ArmStrong number")
else:
    print("The given number is not a ArmStrong number")

