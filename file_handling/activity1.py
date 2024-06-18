text=input("Enter your txt")
text=list(set((text)))
text.sort()
print(text)
"""text.sort()
for i in text:
    if text.count(i)>1:
        while(text.count(i)!=1):
            text.remove(i)
"""

text="".join(text)
file=open("activity1.txt","w")
file.write(text)
file.close()


