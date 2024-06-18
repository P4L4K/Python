'''stu=[]
for i in range(5):
    id=input("enter id")
    name=input("name")
    a=int(input("age"))
    g=input("gen")
    sub1=input("s1")
    sub2=input("s2")
    h=(id,name,a,g,(sub1,sub2))
    stu.append(h)
    print("\n")
stu=tuple(stu)'''
#managing student data
stu=[('101','antira',20,'f',('c','python','math')),
     ('103','Sukriti',19,'f',('c','python','DSA','math')),
     ('102','Laksh',19,'M',('c','DSA','math')),
     ('104','Preeti',18,'f',('c','python','DSA','math')),
     ('106','Ayaan',18,'f',('python','math'))]

def avg(stu):
    """
     
     avg=sum(h[2] for h in stu)/len(stu)
    """
    sum=0
    for i in range(5):
        sum+=(stu[i][2])
    return round(sum/5)

print("avg age: ",avg(stu))

def max(stu):
    max=0
    for i in range(5):
        if(len(stu[i][4])>len(stu[max][4])):
            max=i
    return stu[max][1]

print("max sub: ",max(stu))

def min(stu):
    m=0
    for i in range(5):
        if(len(stu[i][4])<len(stu[m][4])):
            m=i
    return stu[m][1]

print("min sub: ",min(stu))
