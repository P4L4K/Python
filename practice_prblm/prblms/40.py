f=open("40.txt","r")
val=f.read()
val=val.split(" ")
print((val))
sum=0
for i in val:
    sum+=int(i)

print("missing no ",45-sum)
'''val=list(val)
for i in range(1,10):
    if str(i) not in val:
        print("missing value",i)
        break
else:
   print("no missing no")'''
