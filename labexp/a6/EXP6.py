#roll: [name,class,marks]
record={}

#input
def create():
      r=input("enter roll no: ")
      name=input("enter the name: ")
      marks=int(input("marks: "))
      record[r]=[name,marks]
      print("\n")

def search():
    roll=input("Enter the roll no whose details to be searched: ")
    if(roll in record.keys()):
        print("name: ",record[roll][0])
        print("roll no: ",roll)
        print("Marks : ",record[roll][1])
        print("\n")
    else:
        print("roll no not found\n")

c=1
print("""Menu:
1. Enter student record
2. Search student record
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
        
