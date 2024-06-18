"""
additional file methods 
     2 types : os and shutil 
                     are python modules that provide a wide range of functions for interacting with the os and performing various file and directory operations

   os module provides a way to use operating system -dependent functionality, such as readinf or writinf to the file system, interacting with underlying

"""
import os  
import shutil
#create 2 files sample 1 and sample 2
#delete sample1
#rename sample2 as resample2
#os.rename("new_file.txt","samp.txt")
#os.remove("samp.txt")


#activity 4
#create 2 files sample1, sample2 (give any sentense as input for sampele1)
#2. copy sample1 paste in sample2
#3.move sample1 file to any other drive locations

file1=open("sample1.txt","w")
file=open("sample2.txt","w")
text=input("enter your input text")
file1.write(text)
file1.close()
shutil.copy("sample1.txt","sample2.txt")
shutil.move("sample1.txt","D:\\neptel\\file_handling\\new")
