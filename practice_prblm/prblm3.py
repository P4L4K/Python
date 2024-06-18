#Temperature conversion
# f=(9/5)c +32
# k=c+273.15
'''
print(ord("°"))
print(chr(176))
'''

def cf(c):
    f=((9/5)*c)+32
    return round(f,4)

def ck(c):
    k=c+273.15
    return round(k,4)

def fc(f):
    c=(f-32)*(5/9)
    return round(c,4)

def fk(f):
    c=fc(f)
    k=c+273.15
    return round(k,4)

def kc(k):
    c=k-273.15
    return round(c,4)

def kf(k):
    c=kc(k)
    f=cf(c)
    return round(f,4)

print('''
Menu:
1. C to F
2. C to K
3. F TO C
4. F TO K
5. K TO C
6. K TO F
''')

choice=1
while(choice<=6 and choice>0):
    choice=int(input("Enter choice: "))
    value=float(input("Enter the value: "))
    if choice==1:
        print("Result:",cf(value),chr(176)+"F")
    elif choice==2:
        print("Result:",ck(value),"K")
    elif choice==3:
        print("Result:",fc(value),chr(176)+"C")
    elif choice==4:
        print("Result:",fk(value),"K")
    elif choice==5:
        print("Result:",kc(value),chr(176)+"C")
    elif choice==6:
        print("Result:",kf(value),chr(176)+"F")
    
    



    