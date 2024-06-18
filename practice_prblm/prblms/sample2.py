l=[278,576, 496, 727, 410 ,124, 338 ,149 ,209, 702, 282, 718, 771, 575, 436]
k=7
pairs=[]
layer=[]
c=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if((l[i]+l[j])%k==0):
            c+=1
    if c>1:
        l.remove(l[i])

print(l,'\n')
print(len(l))

