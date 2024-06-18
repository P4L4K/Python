#removing the duplicate elements in the given string
str=input("Enter string")
result=""
for i in str:
    if i not in result:
        result+=i

print("Result:",result)