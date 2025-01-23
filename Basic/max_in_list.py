num_len= int(input("Enter the number of elements in list: "))
input_list = []
for _ in range(num_len):
     input_list.append(int(input("Enter the numbers:  ")))
     for num in input_list:
          max_num = max(input_list)
print(("The maximum number in the list is: "),max_num)
