num_len= int(input("Enter the number of elements in list: "))
input_list = []
for _ in range(num_len):
     input_list.append(int(input("Enter the numbers:  ")))
     for num in input_list:
          min_num = min(input_list)
print(("The minimum number in the list is: "),min_num)