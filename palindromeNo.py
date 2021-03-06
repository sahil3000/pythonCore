# palindrome number
# number = reverse_number Eg 343=343

no=int(input("Enter a number: "))
reverse=0;originalNo=no
while no!=0:
    lastDigit=no%10
    reverse=reverse*10+lastDigit
    # restDigit
    no=int(no/10)

if originalNo==reverse:
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome")
    
