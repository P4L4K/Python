print("\n\n10\n\n")
a=10;
b=10;
print(" value of a   ",a)
print(" adress :",id(a))
print(" value of b ",b)
print(" adress :",id(b))

print("\n\n20\n\n")
a=20
b=20
print(" value of a   ",a)
print(" adress :",id(a))

print("\n\nbefore\n\n")
list=[1,2,3,4,5,6]
print(" value of list ",list)
print(" adress :",id(list))
print(" value of list[3] ",list[3])
print(" adress :",id(list[3]))
print(" value of list[4] ",list[4])
print(" adress :",id(list[4]))

print("\n\nafter\n\n")
a=list[4]
list[4]=list[3]
list[3]=a
print(" value of list ",list)
print(" adress :",id(list))
print(" value of list[3] ",list[3])
print(" adress :",id(list[3]))
print(" value of list[4] ",list[4])
print(" adress :",id(list[4]))

print("\n\nbefore\n\n")
list=(1,2,3,4,5,6)
print(" value of list ",list)
print(" adress :",id(list))
print(" value of list[3] ",list[3])
print(" adress :",id(list[3]))
print(" value of list[4] ",list[4])
print(" adress :",id(list[4]))

print("\n\nafter\n\n")
a=list[4]
list[4]=list[3]
list[3]=a
print(" value of list ",list)
print(" adress :",id(list))
print(" value of list[3] ",list[3])
print(" adress :",id(list[3]))
print(" value of list[4] ",list[4])
print(" adress :",id(list[4]))
