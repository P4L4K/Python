g=input("enter: ")
l=[]
for i in g:
    if i.isdigit():
        l.append(int(i))
target=int(input())
ans=[]
for i in range(len(l)):
    if l[i]==target:
        ans.append(i)
print("The target value",target,"is found at positions:",ans)
