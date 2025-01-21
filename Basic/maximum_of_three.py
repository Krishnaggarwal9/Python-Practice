a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))
if (a>b) and (a>c) :
    print("Your first number is greatest") 
elif (b>c) and (b>a) :
    print("Your second number is greatest")
elif (c>a) and (c>b) :
    print("Your Third number is greatest")
else  :
    print("All numbers are equal")