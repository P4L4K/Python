"""
there exactly one similarity b/w 2 lists find ??

"""
import string
import random
symbol=list(string.ascii_letters)
card1=[]
card2=[]
for i in range(5):
    x=random.choice(symbol)
    symbol.remove(x)
    card1.append(x)
    x=random.choice(symbol)
    symbol.remove(x)
    card2.append(x)

pos=random.randint(0,4)
card2[pos]=random.choice(card1)
print(card1,card2)
ans=input("Enter the same symbol: ")
if ans==card2[pos]:
    print("Hurray! you get it right :) ")
else:
    print("Oops! you get it wrong :( ")