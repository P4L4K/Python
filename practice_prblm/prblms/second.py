#CHECKING FOR PASS BY REFERENCE & PASS BY VALUE
a=10
def value(a):
    a=20
    print(" value of a inside the function ",a)
    print(" adress :",id(a))
    return a

print(" value of a  before ",a)
print(" adress :",id(a))
a=value(a)
print(" value of a after  ",a)
print(" adress :",id(a))

print("\n\n")
# [b] checking for mutable data types like list


list=[1,2,3,4,5,6]
def list_fun(list):
    list[3]=30
    print(" value of a inside the function ",list)
    print(" adress :",id(list))
    
    '''print(" adress list[3] :",id(list[3]))
    list[3]=4
    print(" value of a inside the function ",list)
    print(" adress :",id(list))
    print(" adress list[3] :",id(list[3]))'''
    
    return list

print(" value of a  before ",list)
print(" adress :",id(list))
#print(" adress list[3] :",id(list[3]))

list_fun(list)
# the overall adress of the list remains same but the adress of the individual element changes 
print(" value of a after  ",list)
print(" adress :",id(list))
#print(" adress list[3] :",id(list[3]))

