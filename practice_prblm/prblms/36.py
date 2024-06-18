#check if a valid magic square
n=3
M=[]
#input
for i in range(n):
    row=[]
    for j in range(n):
        h=int(input())
        row.append(h)
    M.append(row)

if n%2==0:
    print("False")

sum=[]
d1=0
d2=0
for i in range(n):
        c=0
        r=0
        for j in range(n):
             c+=M[j][i]
             r+=M[i][j]
             if i==j:
                  d1+=M[i][j]
             if (i+j)==(n-1):
                  d2+=M[i][j]
        if c!=r:
             print("false")
             break
        sum.append(c)
        sum.append(r)
else:
     if d1!=d2:
          print("false")
     else:
        sum.append(d1)
        sum.append(d2)
        if sum.count(sum[0])!= len(sum):
            print("false")
        else:
            print("True")              



