
from itertools import permutations
s=input("enter string")
l=list(permutations(s))
for i in l:
    print("".join(i))
