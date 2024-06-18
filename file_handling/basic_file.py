'''
avoid creating files in c drive (why??)
Why?
   RAM : volatile
     thus a program once executed - data is lost
   we can store the program's data in a file - disk - non volatile
   file could also act as a input - as it would be difficult to type a large amount of data on console sometimes

types of files:
   1. Text: human readable file (.txt / .csv / .py)
   2. Binary: contains data - non human readable (images, videos, audios, zip files) - can not be opend using text editors

main operations on files:
   1. Open :  
        file_object = open("file_path","mode") # returns a pointer to the file
                    it acts as a pointer to the file
   2. read
   3. write
   4. close: 
         file_object.close() # closes the opened file

file modes:
  (text files)
   r -> read 
         default mode
         gives error if file doesn't exit
         file handler/cursor at the beginning
   r+ -> read and write
         it modifies the content as we write over it
         it does not overwites all the content unless we write over that content 
         can not create a new file - gives file not exist error
   w -> write 
         overwrites the previous text
         can create a file
         file handler at the beginning
   w+ -> write and read
         ovewrites all the content
         can create a new file
   a -> adds new text while retaining the previous (append)
        file handler at the end
        can create a new file
   a+ -> append and read
        cursor at the end
        can create a new file
   x -> to create a file - we can write in it 

   for binary file add b in front of all the mode like r -> rb, w -> wb , a->ab....
   fy*
as we perform operations the cursor/ file handler changes it's position

tell()- function to tell the position of the file pointer/cursor in the file
seet()- to move cursor to a specific position
'''

file_path="D:/neptel/file_handling/sample.txt"  # if  the file in same folder we may only give the file name

'''
# creating a new file
file=open("sampe.txt","x")


# reading form a file
#reading one line at a time end Of line character "\n" would also be read

#method 1:
with open(file_path) as file:  # by default file is opened in read mode
        for line in file:
            print(line) 
#outside the with : the file is closed but we need to  close it for safety
file.close()

#method 2:
file = open(file_path, "r")  # file object
for line in file:
            print(line)
file.close()  # need to close the file

# read() function : reads all the contents of the file at a time 
file = open(file_path, "r") 
print(file.read())
'''

#Writing text in the file
file=open(file_path,"w")  # file object , overwrites the previous content
file.write("""writing here! 
what do you think it looks like\nwonderfull
   it's python""") 


'''
#modifying the content of the file
file=open(file_path,"r+")  
print(file.tell())  # cursor at the beginning
file.write("hello") # will write hello at the begining overwriting the first 5 words 
print(file.tell())  # the curor would reach at the end of 'o' in "hello"
print(file.read())  # will read all the content after hello
print(file.tell())  # cursor at the end 
print(file.read())  # since the cursor already at end - nothing to read 
file.seek(0)        # setting pointer at the start
print(file.tell())
print(file.read())
'''