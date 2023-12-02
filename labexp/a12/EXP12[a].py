#Create a function max_of_three that takes three numbers as arguments and returns the largest of them 
    #input
def find_max(ele):
    n=0
    for i in ele:
          if i>n:
                n=i
    return n

#input
ele=[]
for i in range(3):
        ele.append(int(input(f"Enter {i+1} digit: ")))
n=find_max(ele)
print(f"Max digit is among {[ele[i] for i in range(3)]} is {n}\n")