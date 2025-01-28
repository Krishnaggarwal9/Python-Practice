list1 = int(input("Enter the number of elements you want in list 1: "))
list2 = int(input("enter the number of elements you want in list 2: "))

input_list1 = []
input_list2 = []
for _ in range(list1):
   input_list1.append(input("Enter the number of list 1: "))
   print("Your list1: "+str(input_list1))
   
for _ in range(list2):     
    input_list2.append(input("Enter the number of list 2: "))
    print("Your list2: "+str(input_list2))


difference_list = list(set(input_list1) - set(input_list2))
print("Your union list is: ", difference_list)