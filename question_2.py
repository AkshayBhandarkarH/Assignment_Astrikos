"""2. The user enters a string and a substring. You have to print the number of times that the 
substring occurs in the given string. String traversal will take place from left to right, not from 
right to left"""

def count(original_str,sub_str):
    l=len(sub_str)
    count=0
    for i in range(len(original_str)-len(sub_str)+1):
        if original_str[i:(i+l)]==sub_str:
             count+=1

    return count

original_str=input("Enter the string\n")
sub_str=input("Enter the Substring\n")


res=count(original_str,sub_str)
print(res)