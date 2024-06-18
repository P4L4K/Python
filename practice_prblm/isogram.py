def iso_gram(string):
    list=[0]*26
    for i in string:
        i=i.lower()
        index=ord(i)-ord("a")
        list[index]+=1

    for i in list:
        
        if(i>1):
            return False

    return True

   
print("hello  ",iso_gram("isIsogram"))

            
