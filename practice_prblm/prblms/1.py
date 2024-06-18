"""num=input("give me a number")
if int(num)%2==0 or int(num)%3==0:
    print(True)"""

#problem 3 to print the sum of 100 digits
sum=0
for i in range(101):
    sum=sum+i
    print("the current sum is " + str(sum)+ "  for integers 0 to"+ str(i))
