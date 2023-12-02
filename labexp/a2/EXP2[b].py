#2nd b
#dictionary ->non primitive datatype
#store collections of data in a key value pairs
#type of array
#keys are acessed by index value and values are accessed by keys
#keys should be of immutable types
#dict ->mutables
#no 2 keys should be same

l={"key1":1,"key2":"red","key3":"apple","key1":2} 
# key1=1 , key2="red",....
#here the value of key1 would be 2,as the key is repeated the 2nd one would be considered as the first would be updated
print('''
1.Using dictionary values 
2.Using dictionary keys 
3.Using dictionary item
4.Without using built-in functions
5.End 
''')
'''
for k in enumerate(l.items()):
   # enumerate makes pairs of index and the values in the iterable
    print(k)
'''
choice=0
while choice!=5:
    choice=int(input("Enter your choice: "))

    if choice==3:
        print(l.items()) #list of both keys and values pairs
        print(type(l.items()))
        for i,v in l.items():
            print("keys :",i,"\tvalues :",v)

    elif choice ==1:
        print(l.values()) #list of all the values
        print(type(l.values()))
        for i in l.values():
            print(i)

    elif choice==2:
        print(l.keys()) #list of all the keys
        print(type(l.keys()))
        for i in l.keys():
            print("key : ",i,"\tvalue:",l[i])
    
    elif choice==4:
        for i in l:
           print(i," ",l[i]) #i would contain keys
    elif choice==5:
        print("Program terminated!")
        break
    else:
        print("Invalid choice!")

"""
# adding/appending new items
l["key4"]="city"
print(l)
# deleting the item
del l["key2"] #key should be in the dictionay or we will get error
print(l)
"""