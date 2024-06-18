"""
special nxn matrix where the sum of all the numbers of any row, column or diagonal elements = a particular no num

n -> odd 
num=n*((n**2)+1)/2

rules : (index starting from 0 )
Ist : 1 is present at (n/2,n-1) or (p,q)
      next element at (p-1,q+1)
2nd : (-1) -> (n-1) and (n)->(0)
3rd : if the calulated position (p,q) already contains a value, then new value (p+1,q-2)
4th : if the calculated position is (-1,n), the the position is (0,n-2)

"""
def value(ele,n):
    if ele==-1:
        return (n-1)
    elif ele==n:
        return (0)
    else:
        return ele

n=int(input("Enter the value of n: "))
if (n%2==0):
    print("sorry! can't form a magic square with even value of n ")

else:
    # creating matrix
    '''matrix=[] 
    for row in range(n):
        row=[]
        for col in range(n):
            row.append("Null")
        matrix.append(row)
    '''
    #method 2
    matrix=[["Null" for col in range(n)] for row in range(n)]
    
    # adding elements
    p=n//2
    q=n-1
    i=1
    while(i<=(n*n)):
        if (matrix[p][q]=="Null"): # using Ist condition
            matrix[p][q]=i
            i+=1
            p=p-1
            q=q+1
        # calculating p and q
        else: # checking the  3rd condition
            p=p+1
            q=q-2

        if(p==(-1) and q==(n)): #checking the 4th condition
            p=0 
            q=n-2 
            continue

        if (p==-1 or p==n):  # for 2nd rule
            p=value(p,n)
        elif (q==-1 or q==n):
            q=value(q,n)
        

    print(* matrix,sep="\n") # printing the magic square

    #calculating sum
    print(" sum : ",(n*((n**2)+1)//2))
    rd=0 #right diagonal
    ld=0 #left diagonal
    for row in range(n):
        sumr=0
        sumc=0
        for col in range(n):
            sumr+=matrix[row][col]
            sumc+=matrix[col][row]
            if(row==col):
                rd+=matrix[row][col]
            if(row+col==n-1):
                ld+=matrix[row][col]
        print(row,"row : ",sumr,row,"column : ",sumc)

    print("rd : ",rd,"ld : ",ld)