s=input("enter the string: ")
s1=""
for i in range(len(s)):
    if i%2==0:
        s1+=s[i].upper()
    else:
        s1+=s[i]
print(s1)