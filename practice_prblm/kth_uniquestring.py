'''
n=int(input("enter the no of strings"))
l=[]
for i in range(n):
    l.append(input())

k=int(input("enter k: "))
c=0
for i in l:
    if l.count(i)==1:
        c+=1
        if c==k:
            print(i)
            break
'''
import inflect

def ordinary(n):
    p=inflect.engine()
    return p.ordinal(n)
for i in range(20,40):
    print(ordinary(i))