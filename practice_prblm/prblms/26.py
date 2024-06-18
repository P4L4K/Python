n=9
r=(n*2)-1
c=r
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==i:
             print(r*(str(i)+" "),end="")
        else:
             print(j,end=" ")
    for j in reversed(range(1,i)):
         print(j,end=" ")
    print("")
    r=r-2
r=r+4
for i in reversed(range(1,n)):
    for j in range(1,i+1):
        if j==i:
             print(r*(str(i)+" "),end="")
        else:
             print(j,end=" ")
    for j in reversed(range(1,i)):
         print(j,end=" ")
    print("")
    r=r+2
   