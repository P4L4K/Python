'''
n=int(input("size of list"))
l=input("enter list elements:")
m=int(input("enter m:"))
l=l.split(" ")
for i in l:
    if (int(i))%m==0:
        print(int(i)**2,end=" ")
    else:
        print(int(i)**3,end=" ")

'''
s=input("enter string: ")
s1=input("enter substring: ")
s2=input("new string: ")
if s1 in s:
    s=s.replace(s1,s2,1)
print(s)