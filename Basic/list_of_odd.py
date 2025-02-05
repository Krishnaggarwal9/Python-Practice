list1 = int(input("Enter the number of odd numbers you want:"))
odd_list =[]
for i in range(1,2*list1+1):
    if i%2!=0:
        odd_list.append(i)
print("Your odd list is: ",odd_list)
