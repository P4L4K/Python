#anagram : characters of S
str1=input("str1 ")
str2=input("str2 ")
if(len(str2)>len(str1)):
      str=str1
      str1=str2
      str2=str

for i in str2:
    if i not in str1:
        print("no")
        break
else:
    print("yes")

#method 2
# not for the cases like of schoolmaster and classroom
st1=sorted(str1)
st2=sorted(str2)
if st2 == st1:
     print("yes")
else:
     print("no")