'''
relational operaters /comparision operators:
       relation / comparision b/w 2 values/variables
       boolean function

       Equality operator(==)
       Inequality Operator(!=)
       Greater Than operator(>)
       less than operator(<)
       greater than or equal to (>=)
       less than or equal to (<=)


a=5
b=6
print(a==(b-(abs(a-b))))
print(a!=(b))
print(a>(b-a))
print(a<(b+a))
print(a>=(b-a))
print(a<=(b+a))
'''
"""

logical operator 
 logical operations on boolean values 
 allows you to commbine and manipulate boolean values to make decisions and control the flow of your program
 and : both condition are ture 
 or  : either first or 2nd condition is true
 not : opposite of the value


x=1
str="hello"
if(x and str):
    print("True")
if(x or str):
    print('True')
if(not(not x)):
    print("True")

"""
"""
bitwise operators
       operates on bits
       treats integers as series of bits 
       allows to manipulate individual bits or grps of bits 

       bit: smallest unit of digit info in comp
        0 or 1
        building block of digital data
        used to represent or store information in comps or electronic devices

      byte:
          8 bits
          standard unit of storing data in comp

    why needed:
    efficient data manipulation
    memory optimization
    valuable in low level programming languages and tasks that require precise 

1.    or : 
      1001
      1100
ans:  1101
 
2.   and:(&) 
        return 1 if both are 1
      1001
      1100
ans   1000

3.   xor(^)
         return 1 if both are different
       1001
       1100
ans       0101   

# checking for even no
 
0100 --4        0101 --5
0001 --1        0001 --1
0000 --0        0001 --!(0)

(0==0)--true    (1==0) --false

bitwise not(~)
bitwise left shift (<<)
       the operator shifts the bits of the left operand to the left by specified no of position filling the vacancies with 0
bitwise right shift (>>)

"""
n=int(input("Enter the no"))
if(n&1==0):  # comparing the first bit form the right
    print("EVEN")
else:
    print("ODD")

