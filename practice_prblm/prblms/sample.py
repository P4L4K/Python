s=[278,576, 496, 727, 410 ,124, 338 ,149 ,209, 702, 282, 718, 771, 575, 436]
k=7

def fun(s,k):
    dict={}
    for i in range(len(s)):
        dict[s[i]]=[]
        for j in range(len(s)):
            if (s[i]+s[j])%k==0:
                dict[s[i]].append(s[j])
       
           
    print("\n\n")
    keys=[]
    for i in s:
        l=[]
        for k in s:
            if dict[i]==dict[k]:
                l.append(k)
        if l not in keys:
            keys.append(l)

    keys=(sorted(keys,key=len_s))

    for i in range(int(len(keys)/2)):
            if dict[keys[i][0]]==(keys[len(keys)-1-i]):
                keys.remove(keys[i])
    
    c=0
    for i in keys:
        c+=len(i)
            
    return  c

print(fun(s,k))