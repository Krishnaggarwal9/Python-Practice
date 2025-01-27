num_len= int(input("Enter the number of elements in list: "))
input_list = []
for _ in range(num_len):
     input_list.append(int(input("Enter the numbers:  ")))
res =[]     
for num in input_list:
    if num not in res:
        res.append(num)
print("Your removed duplicate list is: ",res)