"""
ERROR:
  are unexpeccted events or conditions that prevent the normal xecution of a program
  3 types:
   syntax:
       code not written acc to the rules of the programming language.
       eg print("hello world "

   runtime: 
       occurs during the execution of a program. 
       often the result of invalid input or unexpected conditions
       eg : divide by zero

   logical:
       are most subtle type
       they occur when the code is syntactically correct and runs without erros, but it doesn't  produce the expected output

       eg we want to sum 2 no x,y but the code returns x+y

    try, except and finally: keywords for exception handling 
                             allows us to gracefully manage errors and unexpected situations 
      try : if an exception occurs within the try block, the control is transfered to the corresponding except block
      except : executed if an exception if the specific type occurs within the associated try block
      finally block: the finally  block contains code that will be executed whether an exception occurs or not 

    EXCEPTION HIERARCHY:
      relationship and inheritance 
      refers to the  organizatino of exception in hierarchical structure based on their relationships and inheritance. 
      this hierarchy allows for more specific handling of exceptions and provides a structured way to catch and manage errors

      base exception:     is the base for all built -in exceptions. it is at the top of the exception hierarchy

    Handling multiple exception:
    involves using multiple except blocks, each targeting a specific type of exception.
    this allows code to respond differently based on the type of error encountered
"""
try:
     
    r=[10]
    print(r[3])
except ZeroDivisionError as b: #r=10/0
     print(b)

except TypeError as b:   #r="a"+5
     print(b)

except ValueError as b:  #r=int("a")
    print(b)

except FileNotFoundError as b: #r=open("hello.txt")
    print(b)

except IndexError as b: # raised when sequence is out of range
    print(b)
    """r=[10]
    print(r[3])"""

finally:
    print("we are here")