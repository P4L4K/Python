#palindrom
# eg : malayalam, racecar, tenet, nitin, teet....
str=input("Enter your string")
for i in range(len(str)//2):
    if (str[i]!=str[len(str)-1-i]):
         print("It is not a palindrom")
         break
else:
     print(" It is a palindrom")



