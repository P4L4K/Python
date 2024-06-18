k=int(input())
row=int(input())
col=int(input())
mat=[]
for i in range(row):
    h=input()
    h=h.split()
    if i==k-1:
        h.reverse()

    mat.append(h)

print(mat)