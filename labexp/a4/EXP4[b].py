# binary search 
# efficient searching algorithm 
# divide and conquere approach
# less time complexity compared to linear search
# sorted elements 
# time complexity->o(logn)
#print(20//3) #int-> floar division
#print(20/3)  #decimal
print("\n\tBINARY SEARCH\n") 
def bsearch(a,target):
    l=0
    u=len(a)-1
    while(l<=u):
        mid=(l+u)//2
        if(target==a[mid]):
            print("Element found\n ")
            break
        elif(target>a[mid]):
            l=mid+1
        else:
            u=mid-1
    else:
        print("Element not found \n")


a=[1,3,4,6,8,9,34]
target=int(input('Enter the target: '))
bsearch(a,target)