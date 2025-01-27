lis1= int(input("Enter the number of strings: "))
lis2 =int(input("Enter the number of numbers: "))

lis_num1 = []
lis_num2 =[]

for _ in range(lis1):
    lis_num1.append(input("Enter your string: "))
    print("Original list1 is : " + str(lis_num1))
for _ in range(lis2):
    lis_num2.append(int(input("Enter your number: ")))


    print("Original list2 is : " + str(lis_num2))

    merged_list =( lis_num1 + lis_num2)
    print("Your merged list is: ",merged_list)
    

