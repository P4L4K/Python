print(abs(2-4))
n=int(input("enter n: "))
s=set()
for i in range(n):
    s.add(input())
n1=int(input("enter no of commands:"))
for i in range(n1):
    c=input("enter command: ")
    c=c.split(" ")
    op=c[0]
    if c[0]=='pop':
        s.pop()
    elif c[0]=='remove':
        s.remove(c[1])
    elif c[0]=='discard':
        s.discard(c[1])
sum=0
for i in s:
    sum+=int(i)

print(sum,s)
