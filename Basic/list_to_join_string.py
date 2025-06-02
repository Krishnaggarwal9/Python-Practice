strt = int(input("Enter the no. of string you want:- "))
list = []

for _ in range(strt):
    list.append(input("Enter the string: "))
    print("Your list: " +str(list))

    res = ' '.join(list)
print("Your joined string is:- ",res)
    
