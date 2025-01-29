list1 = int(input("Enter the number of elements in the list: "))
input_list =[]
for _ in range(list1):
    input_list.append(input("Enter the elements: "))
    print("Your list is: "+str(input_list))
    occu_list = set(input_list)
occurrences = {item: input_list.count(item) for item in occu_list}
print("The number of occurrences of each element in the list is: ",occurrences)