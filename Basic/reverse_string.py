def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

original_string = input("Enter yout word/sentence: ")
reversed_string = reverse_string(original_string)
print("Your reversed string is: ",reversed_string) 