print(bin(12))
b=int((input()))
s=""
while(b>0):
    r=b%2
    b=b//2
    s+=str(r)
print(s[::-1])