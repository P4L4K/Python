#you are given a list of student names and their corresponding scores in a class. Write a python program to find the student wiht the highest score and print their name.
'''
alice 91
bob 85
charlie 78
david 95
eve 88

#scores are different
rec={}
n=int(input("Enter the total no of entries"))
for i in range(n):
    name=input("Enter the name : ")
    score=int(input("Score :"))
    rec[score]=name

print(rec)
print(rec[max(rec.keys())])
'''
#names are different
rec={}
n=int(input("Enter the total no of entries"))
max=0
for i in range(n):
    name=input("Enter the name : ")
    score=int(input("Score :"))
    rec[name]=score
    if(max<score):
        max=score

for i in rec:
    if rec[i]==max:
        print(i," ",rec[i])
