#printing right angled triangle
n=int(input("Enter n:")) #no of rows

#right faced
for i in range(1,n+1):
    print(i*("*"))
print("")

#left faced
for i in range(1,n+1):
    print((n-i)*(" ")+i*("*"))
print("")

#down faced
for i in range(n):
    print((n-i)*("*"))
print("")

#up faced
for i in range(n):
    print(i*(" ")+(n-i)*("*"))
