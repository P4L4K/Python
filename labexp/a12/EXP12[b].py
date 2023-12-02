#create a parameter function that checks whether a given number is Armstrong or not
def isarmstrong(n):
    n=str(n)
    p=len(n)
    sum=0
    for i in n:
        sum+=int(i)**p
    if (str(sum)==n):
        return True
    else:
        return False

#checking for armstrong no
n=int(input("Enter the no to chexk if its armstrong no or not : "))
if isarmstrong(n):
    print(f"{n} is armstrong no")
else:
    print(f"{n} is not an armstrong no")




