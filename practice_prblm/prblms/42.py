#palindrom
st=input("enter hte string: ")
for i in range(len(st)//2):
    if st[i]!=st[len(st)-1-i]:
        print("not a palindrom")
        break
else:
    print("palindrom")