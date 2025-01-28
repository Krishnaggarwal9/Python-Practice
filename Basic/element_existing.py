list1 = int(input("Enter the number of elements in list: "))
input_list =[]
for _ in range(list1) :
    input_list.append(input("Enter the element: "))
    print("Your list is: "+str(input_list))
int_a = input("Enter the element you want to check it it exists: ")
if int_a in input_list:
    print("Your element exist in the list")
else:
    print("Your element does not exist in the loop")    