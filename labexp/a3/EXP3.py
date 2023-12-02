#6th oct,2023
#3[a]
#str.isalpha()
st=input("Enter your string: ")
choice=0
print("Menu:\n1.Count the number of alphabets in the given string\n2.To extract the character in the given range\n3.To check if the string is alphanumeric\n4.End\n")
while(choice!=4):
    choice=int(input("\nEnter the choice: "))
    if choice==1:
        c=0
        for i in st:
            if i.isalpha(): 
                c+=1
        print("The no of alphabets in '",st,"': ",c)

    #3[c]
    elif choice==3:
        if st.isalnum(): #only alphabets/ numbers or both - no other character 
            print("Given string is alphanumeric ")
        else:
            print("Given string is not alphanumeric")

    #3[b] 
    #"Welcome to Python world"  #to extract python
    elif choice==2:
        s=int(input("Enter the start"))
        e=int(input("Enter the end"))
        print("The extracted string : ",st[s:e])
        '''
        ch=input("Enter your extracion word : ")
        if ch in st:
            print("The extraction sucessfull ")
            print(ch)
        else:
            print("The extraction not possible")
        '''


    elif choice==4:
        print("The program terminated")
        break

    else:
        print("Invalid choice ")

"""
for i in range(s,e+1):
          if st[i].isalpha():
               print(st[i],end="")
print("\n")"""
