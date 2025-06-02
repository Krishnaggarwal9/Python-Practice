str1 = int(input("Enter the no. of string you want in your list: "))

list=[]

for _ in range(str1):
     list.append((input("Enter the letters:  ")))

seen = set()
duplicates = set()

for item in list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)     

print("Original List: ",list)
print("dublicate items",duplicates)
