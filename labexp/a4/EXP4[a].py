#linear search-> sequential search 
#simple searching algorithm used to find a particular element in a list,arrayy or other data structures
#we iterate over each element to check for the required element 
#time complexity o(n) -> more

#when to use
#unsorted list
#simplicity is more important than efficiency
#small list -> practical for small datasets or when the data set is rarely accessed
print("\n\tLINEAR SEARCH\n") 
l=[1,3,6,8,10,13,15]
ele=int(input("Enter the element to be searched"))
'''
try:
    for i in range(len(l)):
        # Your loop code here
        if l[i]==ele:
            print(i)
            raise StopIteration  # Raise an exception to indicate termination
            break
except StopIteration:
        print("element found")
else:
    print("not found")

'''

for i in range(len(l)):
         if l[i]==ele:
            print("found at index: ",i,"\n")
            break
else: # will execute only if the for loop is not terminated in between
    print("element not found\n")

'''In Python, the else block in a for or while loop is executed 
when the loop completes its iteration without being prematurely terminated by a break statement.
This is a somewhat unique feature of Python, and it is not found in all programming languages.'''
'''
flag=True
for i in range(len(l)):
    if l[i]==ele:
        print("found at index: ",i)
        flag=False
if flag:
    print("element not found")
'''