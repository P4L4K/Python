n=int(input())
max=0
ans=""
for i in range(n):
     h=input()
     if len(h)>max:
          max=len(h)
          ans=h
        
print(ans)