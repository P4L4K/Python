#program to reverse the kth row of the matrix
print("\n\tReversing every kth row of the given matrix\n")
matrix=[[5,3,2],[8,6,3],[3,5,2],[3,6],[3,7,4],[2,9]]
res=[]
k=int(input("Enter k: "))
for indx,row in enumerate(matrix):
    if(indx+1)%k==0:
        rev=list(reversed(row))
        res.append(rev)
    else:
        res.append(matrix[indx])
print("The original matrix: ",*matrix,sep="\n")
print("The reversed matrix: ",*res,sep="\n")