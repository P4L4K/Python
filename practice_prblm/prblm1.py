#to perform addition of numbers without using "+"
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))

#method1 :incrementation operator
result=num2
for i in range(num1):
    result+=1
print("Result(1):",result)

#method2: subtraction
result=(-1)*((num1*(-1))-num2)
print("Result(2):",result)

#method3 : list size -> not optimal but still works
l=list(range(num1))
for i in range(num2):
    l.append(num2)
result=len(l)
print("Result(3):",result)

#method4 : bitwise operators -> not understood till now
a=num1
b=num2
while b!=0:
    carry=a&b
    a=a^b
    b=carry<<1
result=a
print("Result(4):",result)