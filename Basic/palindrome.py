def isPalindrome(s):
    s = str.casefold(s)
    l = len(s)
    if l < 2:
        return True
    elif s[0] == s[l - 1]:
        return isPalindrome(s[1: l - 1])
    else:
        return False
s = input("Enter your string: ")
a = isPalindrome(s)
if a:
    print("Your string is Palindrome")
else:
    print("Your string is not Palindrome")
    