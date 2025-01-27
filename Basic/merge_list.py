lis1=int (input( "Enter the number of string: "))
lis2 = int(input("Enter the number of number: ")) 

input_list1=[]
input_list2=[]

for _ in range(lis1):
     input_list1.append(input("Enter the string:  "))

for _ in range(lis2):
     input_list2.append(int(input("Enter the numbers:  ")))

print("Original key list is : " + str(input_list1))
print("Original value list is : " + str(input_list2))


merged_dict = dict(zip(*[input_list1, input_list2]))
print("Your merged dictionary is: ",merged_dict)