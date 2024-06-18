#genetic algorithm : study 
#here we are just seeing a small glimpse of the idea of genetic algorithms

#pic a random digit from a binary string 
#if the digit is 0 convert it to 1
#we will see that eventually all the digits are converted to 1 
import random

str=list(input("Enter the binary string"))
i=str.count('0')
c=0
while(i>0):
    x=random.randrange(len(str))
    if(str[x]=='0'):
        str[x]='1'
        i-=1
        print(str)
    c+=1
print(c)
str="".join(str)
print(str)
        
