#EXP 7
# CREATE A DATABASE USING LISTS AND TUPLES

#database
data=[] #list to store our data (id,name,city,age)

#function to add new data
def add_data():
    name=input("Enter name: ")
    id=input("Enter your id: ")
    city=input("Enter your city: ")
    age=int(input("Enter your age: "))
    data.append((id,name,city,age)) #adding data in the database as a tuple
    print("Record added successfully!\n")

#function to search data for a particular id
def search():
    id=input("Enter the id to be searched: ")
    for i in data:
        if i[0]==id: #checking for the id in the database
            print(f"id : {i[0]}")
            print(f"name : {i[1]}")
            print(f"city : {i[2]}")
            print(f"age : {i[3]}")
            print("Search successful!\n")
            break
    else:
        print("Record not found!\n") #id does not exist

#function to display all the data in the database
def display_all():
    print("Displaying the data:")
    if len(data)==0: #checking if there is not data in the database
        print("No data available!\n")
        return

    for i in data: #displaying the data
            print("\nRecord:")
            print(f"id : {i[0]}")
            print(f"name : {i[1]}")
            print(f"city : {i[2]}")
            print(f"age : {i[3]}")

    print("Display successful!\n")

#function to delete data for a particulat id 
def delete_data():
    id=input("Enter the id to be deleted: ") #input the id
    for i in data:
        if i[0]==id: #searching for the id in database
            data.remove(i) #deleting the data
            print("Deletion successfull!\n")
            break
    else:
        print("Record not found!\n") #id is not in the data

def main():
    #taking choice form the user
    choice=0
    while (choice!=5):
        print('''Menu:
1. add new data
2. search data
3. display all the data
4. delete data
5. end
''')
        choice=int(input("Enter your choice: "))
        if choice==1:
            add_data()
        elif choice==2:
            search()
        elif choice==3:
            display_all()
        elif choice==4:
            delete_data()
        elif choice==5:
            print("Terminating the program....\n")
            break
        else:
            print("Invalid choice!!")

main()      

         