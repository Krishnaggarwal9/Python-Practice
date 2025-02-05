list1 = int(input("Enter the number of strings you want: "))
even_list =[]
for i in range(1 ,2*list1+1):
    if i%2==0:
        even_list.append(i)
print("Your even list is: ",even_list)
    