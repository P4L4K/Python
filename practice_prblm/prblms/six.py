#calculator
print("WELCOME TO MY CALCULATOR\n")
o='0'
res=0
print("MENU:\n1. (+)\n2. (-)\n3. (*)\n4. (/)\n5. (%)\n6. power\n7. round\n8. hexadecimal conversion\n9. octal conversion\n10. binary conversion\n11. end\n")
a=float(input("Enter your first no: "))
o=input("Enter your operation : ")
b=float(input("Enter your second no: "))
while(0!="11"):
    if(o=="1"):
      res=a+b
    elif(o=="2"):
      res=a-b
    elif(o=="3"):
      res=a*b
    elif(o=="4"):
        if(b==0):
            print("Division by zero error")
        else:
           res=a/b
    elif(o=="5"):
        if(b==0):
            print("Division by zero error")
        else:
           res=a%b
    elif(o=="6"):
           res=a**b
    elif(o=="7"):
            res=round(a)
    elif(o=="9"):
            print("octal: ",int(res),"=",oct(int(res)))
    elif(o=="8"):
            print("hexa: ",int(res),"=",hex(int(res)))    
    elif(o=="10"):
            print("binary: ",int(res),"=",bin(int(res)))
    elif(o=="11"):
         break
    else:
        print("Invalid operation")
    print("Current value: ",res)
    a=res #will act as the first digit for the next operation
    o=input("\nEnter your operation : ")
    if(o not in ['7','8','9','10','11']):
        b=float(input("Enter 2nd digit: "))
   
print("\nThank you\n")

