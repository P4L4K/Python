#database using lists and tuples
#(name,age,city)
record=[]

#input
def create():
      name=input("Enter Name: ")
      age=int(input("Enter Age: "))
      city=input("Enter City: ")
      record.append((name,age,city))
      print("\n")

def search(): 
    name=input("Enter the name whose details to be searched: ")
    flag=True
    for i in record:
        if name == i[0]:
            print("Name: ",i[0])
            print("Age: ",i[1])
            print("City : ",i[2])
            print("\n")
            flag=False
    if (flag):
        print("Name no not found\n")

c=1
print("""Menu:
1. Enter record
2. Search record
3. End
""")
while(c!=3):
    c=int(input("Enter the choice"))
    if c==1:
        create()
    elif c==2:
        search()
    else:
        break
        
