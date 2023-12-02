#celsius to farenheit
def cel_to_fa(ce):
    ans=(ce*(9/5))+32
    print(ce,'°C is equal to ',ans,"F") #alt+0176

def fa_to_cel(f):  
    ans=(f-32)*(5/9)
    print(f,"F is equal to ",ans,"C")

while True:
    print('''Menu:
    1. Celsius to Farenheit
    2. Farenheit to Celsius
    3. End
    '''
    )
    c=int(input("Enter choice: "))
    if (c==1):
        ce=int(input("Celsius: "))
        cel_to_fa(ce)
    elif (c==2):
        f=int(input("Farenhiet: "))
        fa_to_cel(f)
    elif c==3:
        print("Terminating the program....")
        break
    else:
        print("Invalid choice!!")

