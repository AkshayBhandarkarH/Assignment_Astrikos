#1. Check if the given string is a palindrome or not irrespective of case
def palindrome(str):
      str=str.lower()
      if str==str[::-1]:
    
       return 1

str=input("Enter a String\n")
result=palindrome(str)
if result==1:
    print(f'yes {str} is palindrome')
else:
    print(f'No {str} is not a palindrome')





