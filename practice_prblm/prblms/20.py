'''
string values

naming conventions
         matrix=[[],[]] #nested list
         Matric=[[],[]] #matrix

Integrated developmetn and learning 

dynamic typing: data type of a variable is determined during runtime, rather than being explicitly declared at the time of variable creation
                data type changes 
                code flexibility
    eg:
        a="hello"
        print(type(a)) #string
        a=3
        print(type(a)) #integer

'''
def func(char):
    if char=="8":
       return "8"
    if char=="1":
       return "1"
    if char=="0":
       return "0"
    if char=="6":
       return "9"
    if char=="9":
       return "6"
    else:
       return "*" #inverted digit doesnot makes a valid character

str=input()
re=""
for i in range(len(str)-1,-1,-1):
    re+=func(str[i]) 

if(re==str):
   print("yes the input no is strobogrammatic numbers")
else:
   print("no the input no is not strobogrammatic numbers")
   
    