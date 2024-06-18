#printing diamond
r=4
for i in range(1,r+1):
    if i==r-1:
        print("")
    else:
        print(" "*(r-i),"* "*i)
for i in range(r-1,0,-1):
    if(i==r-1):
        print("")
    else:
        print(" "*(r-i),"* "*i)
