m=[[1,3,4],[1,4,6],[-5,24,0]]
ma=0 #maximum
for i in m:
    if max(i)>ma:
        ma=max(i)
print(ma) 
mi=ma #minimum
for i in m:
    if min(i)<mi:
        mi=min(i)
print(mi)