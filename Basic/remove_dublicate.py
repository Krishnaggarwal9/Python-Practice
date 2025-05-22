num_len= int(input("Enter the number of elements in list: "))
input_list = []
for _ in range(num_len):
     input_list.append(input("Enter the numbers:  "))
removed_item =[]     
for items in input_list:
    if items not in removed_item:
        removed_item.append(items)
print("Your removed duplicate list is: ",removed_item)