#multiplication without using "*"
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
result=0
for i in range(num2):
    result+=num1
print("Result:",result)
print("Expected:",(num1*num2))