st=input("enter")
i=ord(st[0])-ord('a')
j=8-int(st[1])
if((i+j)%2==0):
    print("White")
else:
    print("Black")