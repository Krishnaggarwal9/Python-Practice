numb = int(input("Enter the digited number: "))
numb_str =str(numb)
total_sum = 0
for digit in numb_str:
    total_sum += int (digit)
print(f"The sum of digits in {numb} is: ",total_sum)    
