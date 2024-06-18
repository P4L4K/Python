#copying content of one file to another
name=input("enter your name: ")

f1=open("sample.txt","w")
f1.write(f"Hello\nMY name is {name} ")
f1.close()

f1=open("sample.txt","r")
f2=open("sample_cpy.txt","w")
x=f1.read()
#print(content)
f2.write(x)
age=input("enter your age: ")
f2.write(f"\nMY age is {age} years")


'''
for line in f1:
    f2.write(line)

#copying image file (binary file)
f1=open("image1.jpg","rb")
f2=open("image1_cpy.jpg","wb")
for line in f1:
    print(line)
    f2.write(line)
'''
f1.close()
f2.close()

f1=open("D:\\neptel\\file_handling\\basic_file.py","r")
f2=open("D:\\neptel\\file_handling\\sample_inherit.py","w")
x=f1.read()
f2.write(x)
f2.close()
f1.close()