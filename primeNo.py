# prime no
flag=0
no=int(input("Enter a number : "))
for i in range(2,int(no/2)+1):
    if(no%i==0):
        flag=1

if no==1:
    print("The given number is neither a prime no. nor composite no.")
elif flag==1:
    print("The given number is not a prime no.")
else:
    print("The given number is a prime no.")
