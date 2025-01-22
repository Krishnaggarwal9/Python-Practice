import random
nand_num = int(input("Enter the total number of random numbers you want: "))
rand_num = []
for _ in range(nand_num) :
    rand_num.append(random.uniform(1.0, 100.0))
print("Your random numbers are: ",rand_num)