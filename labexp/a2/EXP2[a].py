#5th oct
#2nd [a] different ways of printing a list
l=[10,10.5,"apple",34,47]
length=len(l)
print('''
1.Using for loop with range
2.Using for loop 
3.Using while loop
4.Using comprehension
5.Using enumeration
6.End
''')
choice=0
while choice!=6:
    choice=int(input("Enter your choice: "))
    if choice==3:
        i=0
        while i in range(length):
            print(l[i])
            i+=1
    elif choice ==1:
        for i in range(length):
            print(l[i])
    elif choice==2:
        for i in l:
            print(i)
    elif choice==4:
        [print(i) for i in l]#comprehension ->compact syntax
    elif choice==5:
        for i,val in enumerate(l):
            print(i," : ",val)
    elif choice==6:
        print("Program terminated!")
        break
    else:
        print("Invalid choice!")

#print(*l,sep="\n")