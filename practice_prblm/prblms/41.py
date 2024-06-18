ar=[22,4,1,32,4,5,32,3]
ar2=[]
for i in ar:
    if i not in ar2:
        ar2.append(i)
    else:
        print(" duplicate ",i)
        ar.remove(i)