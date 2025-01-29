list1 = int(input("Enter the number of elements in the list: "))
input_list =[]
for _ in range(list1):
    input_list.append(input("Enter the elements: "))
    print("Your list is: "+str(input_list))
int_a = (input("Enter the element you want to check it it exists: "))
index = input_list.index(int_a)
print("The index of your element is : ",index)