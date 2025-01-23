list_len = int(input("Enter the number of elemnts to be added: "))

sum = 0

input_list= []


for _ in range(list_len):
   
   input_list.append(int(input("Enter the numbers: ")))


for num in input_list:
    sum = sum + num
print("The sum of numbers in the List is: ",(sum))